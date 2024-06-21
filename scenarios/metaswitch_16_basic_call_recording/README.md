# 16 - Basic Calling

## Test Case A
Inbound Call

### Description
1. Action: Call A from B, answer call
2. Confirm: Two way media
3. Action: End call

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_16_basic_call_recording/16a_basic_call_inbound.xml -m 1
```

## Test Case B
Outbound Call

### Description
1. Action: Call B from A, answer call
2. Confirm: Two way media
3. Action: End Call

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_16_basic_call_recording/16b_basic_call_outbound.xml -m 1
```

## Test Case C
Both parties subscribed to recording
### Setup
These tests should be done with the Recording Server set up to prefer G.711 codec, and to use SIP over UDP Provision A and C on the recording server
### Description:
1. Action: Call A from C, answer call
2. Confirm: Two way media
3. Action: End call
4. Confirm: Two recordings made:
    - one from perspective of A, start and end time accurate
    - one from perspective of C, start and end time accurate (media should be identical in both recordings

### Run scenario - Call A
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_16_basic_call_recording/16c_basic_call_callA.xml -m 1
```

### Run scenario - Call B
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_16_basic_call_recording/16c_basic_call_callB.xml -m 1
```



## Test Case C - 3PCC
Both parties subscribed to recording
### Setup
These tests should be done with the Recording Server set up to prefer G.711 codec, and to use SIP over UDP Provision A and C on the recording server
### Description:
1. Action: Call A from C, answer call
2. Confirm: Two way media
3. Action: End call
4. Confirm: Two recordings made:
    - one from perspective of A, start and end time accurate
    - one from perspective of C, start and end time accurate (media should be identical in both recordings

### Run scenario
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start `call B`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_16_basic_call_recording/3pcc_16c_basic_call_callB.xml -m 1
```

Start `call A`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_16_basic_call_recording/3pcc_16c_basic_call_callA.xml -m 1
```

## Test Case G
Music on Hold - non-recorded party held

### Description
1. Action: Call A from B, answer call
2. Confirm: Two way media
3. Action: From A put B on hold
4. Confirm: A hears music on hold
5. Action: From A take B off hold
6. Confirm: Two way media
7. Action: End call
8. Confirm: Single call recording including the three parts of the call:
        - Two way media
        - Silence while call was on hold
        - Two way media  --

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_16_basic_call_recording/16g_basic_call_hold.xml -m 1
```
