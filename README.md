# Start call generator

Build docker image with SIPP:

    docker build -t sipp .

Run the existing scenario:

    docker run -it sipp -t t1 -inf scenarios/tenant-users.csv -inf scenarios/callee.csv -sf scenarios/16b_basic_calls_outbound.xml -m 1000 -r 5 -rp 1s -l 50 1.2.3.4:5080

This scenarios loads a list of tenants/subsribers from file `tenant-users.csv` and a random remote phone numbers from file `callee.csv`.

With these settings, it will generate maximum 5 calls per second (see `-r 5 -rp 1`) and limit to 50 concurrent sessions (see `-l 50`), maximum 1000 calls (see `-m 1000`).

Replace:

   - 1.2.3.4:5080 with your MiaRec ip-address (IP and port)



# Start single call scenario

    sipp 192.168.1.5:5080 -i 192.168.1.106 -t t1 -inf scenarios/tenant-users.csv -inf scenarios/callee.csv -sf scenarios/16b_basic_calls_outbound.xml -m 1000 -r 5 -rp 1s -l 50

This scenarios loads a list of tenants/subsribers from file `tenant-users.csv` and a random remote phone numbers from file `callee.csv`.

With these settings, it will generate maximum 5 calls per second (see `-r 5 -rp 1`) and limit to 50 concurrent sessions (see `-l 50`), maximum 1000 calls (see `-m 1000`).

Replace:

   - 192.168.1.5 with your MiaRec ip-address
   - 192.168.1.106 with local machine ip-address (where SIPP is running)



# Start 3PCC scenario    

    sipp 192.168.1.106:5080 -i 192.168.1.106 -m 1 -t t1 -3pcc 192.168.1.106:7777 -sf scenarios/01a_3way_call_initiator_recorded_2.xml
    sipp 192.168.1.106:5080 -i 192.168.1.106 -m 1 -t t1 -3pcc 192.168.1.106:7777 -sf scenarios/01a_3way_call_initiator_recorded_1.xml
    
Where:

- `192.168.1.106:5080` is IP:PORT of SIPREC recorder
- `192.168.1.106:7777` is a listening port of twin SIPP instance (Side B)
- `127.0.0

# Extended 3PCC scenario

    sipp 192.168.1.106:5080 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 1slave.cfg -slave slave1 -sf scenarios/01a_3way_call_initiator_recorded_ext_2.xml
    sipp 192.168.1.106:5080 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 1slave.cfg -master master -sf scenarios/01a_3way_call_initiator_recorded_ext_1.xml

# Extended 3PCC scenario (Cisco BiB scenario)

With Cisco BIB, we need to create two separte SIP sessions. Each session includes voice of one of two participants.

SIPP capabilities are quite limited. It is doable, but not 100% accurate.

First, run the slave instance:

    sipp 192.168.1.111:5070 -m 1 -t t1 -slave_cfg 1slave.cfg -slave slave1 -sf scenarios/cisco_bib_call_slave1.xml


Then, start a master instance:

    sipp 192.168.1.111:5070 -m 1 -t t1 -slave_cfg 1slave.cfg -master master -sf scenarios/cisco_bib_call_master.xml

    
# Run python script (basic 3PCC)

    python3 run_scenario.py -r 192.168.1.106:5080 scenarios/01a_3way_call_initiator_recorded_1.xml scenarios/01a_3way_call_initiator_recorded_2.xml 

# Extended 3PCC scenario (master + 3 slaves)

    sipp 192.168.1.106:5070 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 3slaves.cfg -slave slave1 -sf scenarios/cisco_bib_call_slave1.xml
    sipp 192.168.1.106:5070 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 3slaves.cfg -slave slave2 -sf scenarios/cisco_bib_call_slave2.xml
    sipp 192.168.1.106:5070 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 3slaves.cfg -slave slave3 -sf scenarios/cisco_bib_call_slave3.xml
    sipp 192.168.1.106:5070 -i 192.168.1.106 -m 1 -t t1 -slave_cfg 3slaves.cfg -master master -sf scenarios/cisco_bib_call_master.xml


# Cisco CUBE Network-based recording

## Normal call

    sipp 192.168.1.5:5080 -i 192.168.1.106 -m 1 -t t1 -sf scenarios/cisco_cube_network_based_normal_1.xml

## Outbound call, transferred to another party

CUBE sends re-INVITE with the updated call participants info

    sipp 192.168.1.5:5080 -i 192.168.1.106 -m 1 -t t1 -sf scenarios/cisco_cube_network_based_1.xml

    
# Some important command-line options:
	-sf filename
		Load test scenario from specified file.
	-inf filename
		Use CSV file to insert data substituted for [field0], [field1], etc into XML scenario. First line of file describes order of inserting field sets (SEQUENTIAL/RANDOM/USE).
	-sn name
		Use one of the embedded, predefined scenarios like "uac", "uas".
	-r rate
		Scenario execution rate, default value = 10 times per period, default period = 1000 ms.
	-rp period
		Scenario execution period [ms], combined with execution rate. Execution rate is combined of rate and period parameters, i.e. if period = 3500 and rate = 7 there will be 7 calls in 3.5 s.
	-t transport mode
		Set the transport mode: "u1" - UDP, one socket (default), "un" - UDP, one socket per call, other modes (TCP and with compression) available.
	-max_socket max
		Set the limit for simultaneously used sockets (for one socket per call mode). If limit is reached, sockets are reused.
	-m calls
		Stop and exit after specified tests count.
	-s service
		Set user part of the request URI (default: 'service'). Replaces [service] tag in XML scenario file.
	-ap pass
		Set password used for auth challenges (default: 'password').
	-l limit
		Limit simultaneous calls (default: 3 * call_duration (s) * rate).
	-recv_timeout
		Global receive timeout (miliseconds). By default call is aborted, use ontimeout attribute to take other action.
	-trace_msg
		Log sent and received SIP messages (file: scenario_pid_messages.log).
	-trace_err
		Log error message to file (like "Discarding message which can't be mapped to a known SIPp call").
	-sd
Dumps one of the default scenarios. Usage example: sipp -sd uas > uas.xml.   


# Tips

## How to create very long audio file

Use sox utility, like:

    sox input.wav output.wav repeat 10



