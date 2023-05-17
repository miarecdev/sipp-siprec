## Test case A

### Summary
Call waiting on recorded party
### Setup
Recording not enabled on A G.
Recording not enabled on B
Recording enabled on E
### Description
	1. Action: From E call G
	2. Confirm: Two way media
	3. Action: From B call E
	4. Action: Answer B on E
	5. Confirm: Two way media E - B, G is on hold
	6. Action: On E switch back to first call
	7. Confirm: Two way media G - E, B is on hold
	8. Action: End calls
	9. Confirm: Two recordings:
            - G - E both parts of call (before G is on hold and after E resumes call with G)
            - E - B


### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start participant B
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_07_call_waiting/07a_call_waiting_callB.xml -m 1
```

Start participant A
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_07_call_waiting/07a_call_waiting_callA.xml -m 1
```
