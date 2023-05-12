

## Test Case A

### Summary
Transferred to party is recorded
### Setup
A and C provisioned on Recording Server
### Description
	1. Action: Set up call from B to G
	2. Confirm: Two way media
	3. Action: Put G on hold and call A from B
	4. Confirm: 2-way media between B and A
	5. Confirm: 0-way media between B and G
	6. Action: Transfer A to G
	7. Confirm: B drops out of call, 2-way media between G and A
	8. Action: End call
Confirm: Single recording including A - B and G – A

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address


```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_02_attended_xfer/02a_attended_xfer.xml -m 1
```


## Test Case B

### Summary
Both parties recorded

### Setup
A and C provisioned on Recording Server

### Description
    1. Action: Set up call from A to C
    2. Coinfirm: Two way media
    3. Action: Put C on hold and call B from A
    4. Confirm: 2-way media between B and A
    5. Confirm: 0-way media between A and C
    6. Action: Transfer C to B
    7. Confirm: A drops out of call, 2-way media between C and B
    8. Action: Hang up call
    9. Confirm: Three recordings:
      - A - C
      - A - B
      - C - A and C - B

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start slave1
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -slave slave1 -sf scenarios/metaswitch_02_attended_xfer/02b_attended_xfer_slave1_callA.xml -m 1
```

Start slave2
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -slave slave2 -sf scenarios/metaswitch_02_attended_xfer/02b_attended_xfer_slave2_callC.xml -m 1
```

Start master
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -master master -sf scenarios/metaswitch_02_attended_xfer/02b_attended_xfer_master_callB.xml -m 1
```


