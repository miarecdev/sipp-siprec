# 01 - 3 way calling

## Test Case A
3-way call - recorded party in initial call
### Setup
Provision A on the Recording Server
### Description
1. Action: Setup call B calling A
2. Action: Talk into both phones
3. Action: Put B on hold and call G from A
4. Action: Conference B into 3 way call
5. Action: Talk into all phones
6. Confirm: 3 way media
7. Action: End call
8. Confirm: Two recordings:
    - B - A call and final A,B,G call
    - A - G call and final A,B,G call

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start participant B
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_01_3way_call/01a_3way_call_callB.xml -m 1
```

Start participant A
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_01_3way_call/01a_3way_call_callA.xml -m 1
```
