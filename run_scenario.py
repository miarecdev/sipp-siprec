import os
from datetime import timedelta, datetime
import io
import time
import sys
import signal
import subprocess
import argparse
import socket
from subprocess import Popen, PIPE


def get_local_ip(remote_host):
    """
    Get IP-address of local network interface, that is routable to remote_host.

    Args:
        remote_host (str): IP-address or DNS name

    Returns:
        str: IP address
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((remote_host, 80))
    ip = s.getsockname()[0]
    s.close()

    return ip


# From http://www.pixelbeat.org/talks/python/spinner.py
def cli_exception(typ, value, traceback):
    """Handle CTRL-C by printing newline instead of ugly stack trace"""
    if not issubclass(typ, KeyboardInterrupt):
        sys.__excepthook__(typ, value, traceback)
    else:
        sys.stdout.write("\n")
        sys.stdout.flush()


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description='Run SIPP call scenario towards SIPREC recorder',
        epilog='Example: %(prog)s --recorder 192.168.1.5:5060 scenario.xml [scenario2.xml]'
    )

    parser.add_argument(
        '-r', '--recorder',
        required=True,
        dest='recorder_addr',
        metavar='IP:PORT',
        help='SIPREC recorder IP:PORT'
    )

    parser.add_argument(
        '-t', '--timeout',
        required=False,
        default=None,
        type=int,
        dest='timeout',
        metavar='SECONDS',
        help='Timeout for scenario execution'
    )

    parser.add_argument(
        'scenarios',
        metavar='SCENARIO',
        nargs='+',
        help='SIPP scenario XML file'
    )

    return parser.parse_args()


def run_scenario(recorder_addr, scenarios, timeout):

    remote_ip, remote_port = recorder_addr.split(':')

    local_ip = get_local_ip(remote_ip)

    if isinstance(timeout, int):
        timeout = timedelta(seconds=timeout)

    if len(scenarios) == 1:
        return run_single_scenario(recorder_addr, local_ip=local_ip, scenario=scenarios[0], timeout=timeout)
    elif len(scenarios) == 2:
        return run_3pcc_scenario(recorder_addr, local_ip=local_ip, scenario1=scenarios[1], scenario2=scenarios[0], timeout=timeout)
    else:
        print("Unsupported number of scenarios: %d" % len(scenarios))
        return 2



def run_single_scenario(recorder_addr, local_ip, scenario, timeout):

    proc_args = [
        'sipp',
        recorder_addr,   # Endpoint (recorder) IP:PORT
        '-i', local_ip,  # Local IP address
        '-m', '1',       # Maximum 1 call
        '-t', 't1',      # TCP transport
        '-sf', scenario  # Scenario file
    ]


    proc = Popen(proc_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    print('Running SIPP...')

    output, errors = proc.communicate(timeout=timeout)
    if proc.returncode != 0:
        print("SIPP ERROR: %s" % errors)
        return proc.returncode
    # elif errors:
    #     print("SIPP WARNING: %s" % errors)

    print('COMPLETED')

    output = output.decode('utf-8').replace('\r', '')
    lines = output.split('\n')
    for line in lines[-50:]:   # Print last 50 lines
        print(line)

    return 0


def run_3pcc_scenario(recorder_addr, local_ip, scenario1, scenario2, timeout):

    proc_args_1 = [
        'sipp',
        recorder_addr,   # Endpoint (recorder) IP:PORT
        '-i', local_ip,  # Local IP address
        '-3pcc', '%s:7777' % local_ip,    # 3PCC communication
        '-m', '1',       # Maximum 1 call
        '-t', 't1',      # TCP transport
        '-sf', scenario1  # Scenario file
    ]

    proc_args_2 = [
        'sipp',
        recorder_addr,   # Endpoint (recorder) IP:PORT
        '-i', local_ip,  # Local IP address
        '-3pcc', '%s:7777' % local_ip,    # 3PCC communication
        '-m', '1',       # Maximum 1 call
        '-t', 't1',      # TCP transport
        '-sf', scenario2  # Scenario file
    ]


    print('Running SIPP...')

    running_procs = [
        Popen(proc_args_1, stdin=PIPE, stdout=PIPE, stderr=PIPE),
        Popen(proc_args_2, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    ]

    start_time = datetime.now()

    retcode = 0
    while running_procs:
        for proc in running_procs:
            retcode = proc.poll()
            if retcode is None:  # Process finished.
                time.sleep(1)
                continue
            else:

                if retcode:
                    # Exit with error.
                    print("SIPP ERROR: ")
                    for line in io.TextIOWrapper(proc.stderr, encoding="utf-8"):
                        print(line.replace('\r', ''))
                else:
                    # Exit normally
                    print('One of process exited')
                    print("================ STD OUT (last 50 lines) =============")
                    lines = [line for line in io.TextIOWrapper(proc.stdout, encoding="utf-8")]
                    for line in lines[-100:]:   # Print last 50 lines
                        line = line.replace('\r', '').strip()
                        if line:
                            print(line)

                running_procs.remove(proc)
                break

        if timeout and datetime.now() - start_time > timeout:
            print("Timeout expired")
            for proc in running_procs:
                proc.kill()
                print("================ STD OUT (last 50 lines) =============")
                lines = [line for line in io.TextIOWrapper(proc.stdout, encoding="utf-8")]
                for line in lines[-100:]:   # Print last 50 lines
                    line = line.replace('\r', '').strip()
                    if line:
                        print(line)

                print("================= STD ERR (last 50 lines) =============")
                lines = [line for line in io.TextIOWrapper(proc.stderr, encoding="utf-8")]
                for line in lines[-100:]:   # Print last 50 lines
                    line = line.replace('\r', '').strip()
                    if line:
                        print(line)

            break

    print('FINISHED')
    return retcode or 0


if __name__ == '__main__':
    # Handle CTRL-C by printing newline instead of ugly stack trace
    if sys.stdin.isatty():
        sys.excepthook = cli_exception

    # Parse command line arguments
    args = parse_command_line_arguments()

    exit_code = run_scenario(**vars(args))

    sys.exit(exit_code)
