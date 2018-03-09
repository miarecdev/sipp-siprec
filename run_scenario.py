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
    for line in lines[-100:]:   # Print last 50 lines
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

    # Note: I tried to use subprocess.poll(), but this makes the underlying SIPP process extremely slow (x10 or so).
    # Probably, it is a bug in SIPP, which gets timing values from non-accurate source, and supprocess.poll() has influence on those timing values
    # Now, we j

    for i, proc in enumerate(running_procs):
        output, errors = proc.communicate(timeout=timeout)
        if proc.returncode != 0:
            print("SIPP ERROR: %s" % errors)
            return proc.returncode
        # elif errors:
        #     print("SIPP WARNING: %s" % errors)

        print('Process [%d] finished' % i)

        output = output.decode('utf-8').replace('\r', '')
        lines = output.split('\n')
        for line in lines[-100:]:   # Print last 50 lines
            print(line)

    print('FINISHED')
    return 0


if __name__ == '__main__':
    # Handle CTRL-C by printing newline instead of ugly stack trace
    if sys.stdin.isatty():
        sys.excepthook = cli_exception

    # Parse command line arguments
    args = parse_command_line_arguments()

    start_time = datetime.now()

    exit_code = run_scenario(**vars(args))

    print('Execution time: %s' % (datetime.now() - start_time))

    sys.exit(exit_code)
