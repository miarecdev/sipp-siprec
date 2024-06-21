# 05 - Call Park

## Test Case A
Recorded party A parks call and recorded party B C is parked

### Description
	1. Action: Set up call from A to C
	2. Action Speak into both phones
	3. Action: From A call park C into orbit (*301)   - using Attended Transfer to *301.
	4. Confirm: A drops out of call and C hears music on hold
	5. Action: From A retrieve parked call (*302 followed by orbit code, for example *302100 for orbit 100)
	6. Action: Speak into both phones
	7. Action: End call
	8. Confirm: Three call recordings
- Initial A - C call
- Final A - C call after call has been retreived
- Initial A - C call, C hears music on hold, final A - C call


### Run scenario - Call A
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_05_call_park/05a_call_park_callA.xml -m 1
```

### Run scenario - Call B
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_05_call_park/05a_call_park_callB.xml -m 1
```

### Run scenario - Call C
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_05_call_park/05a_call_park_callC.xml -m 1
```


## Test Case A - 3PCC
Recorded party A parks call and recorded party B C is parked

### Description
	1. Action: Set up call from A to C
	2. Action Speak into both phones
	3. Action: From A call park C into orbit (*301)   - using Attended Transfer to *301.
	4. Confirm: A drops out of call and C hears music on hold
	5. Action: From A retrieve parked call (*302 followed by orbit code, for example *302100 for orbit 100)
	6. Action: Speak into both phones
	7. Action: End call
	8. Confirm: Three call recordings
- Initial A - C call
- Final A - C call after call has been retreived
- Initial A - C call, C hears music on hold, final A - C call


### Run scenario
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start `slave2`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -slave slave2 -sf scenarios/metaswitch_05_call_park/3pcc_05a_call_park_slave2.xml -m 1
```

Start `slave1`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -slave slave1 -sf scenarios/metaswitch_05_call_park/3pcc_05a_call_park_slave1.xml -m 1
```

Start `master`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -slave_cfg 2slaves.cfg -master master -sf scenarios/metaswitch_05_call_park/3pcc_05a_call_park_master.xml -m 1
```

## Test Case B
Call parked by recorded party and retreived by nonrecorded pary

### Description
1. Action: Set up call from A to B
2. Action: Speak into both phones
3. Action: From A park B into orbit (*301)
4. Confirm: A drops out of call and B hears music on hold
5. Action: From G retreive B from orbit (*302 followed by orbit code, for example *302100 for orbit 100)
6. Action: Speak into both phones
7. Action: End call



### Run scenario
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_05_call_park/05b_call_park.xml -m 1
```


## Test Case C
Call parked by nonrecorded party and retreived by recorded pary

### Description
1. Action: Set up call from G to B
2. Confirm: Two way media
3. Action: From G park B into orbit (*301)
4. Confirm: G drops out of call and B hears music on hold
5. Action: From A retreive B from orbit (*302 followed by orbit code, for example *302100 for orbit 100)
6. Action: Speak into both phones
7. Action: End call



### Run scenario
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_05_call_park/05c_call_park.xml -m 1
```




