# 04 - Blind Transfer

## Test Case C
Both parties recorded

### Description
1. Action: Set up call A from B
2. Confirm: Two way media
3. Action: Blind transfer B to C
4. Confirm: A drops out of call
5. Confirm: Two way media
6. Action: End call
7. Confirm: Two call recordings
  - A - B
  - B - C -->

### Run scenario - Call A

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_04_blind_xfer/04c_blind_xfer_callA.xml -m 1
```

### Run scenario - Call B

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_04_blind_xfer/04c_blind_xfer_callB.xml -m 1
```


## Test Case C - 3PCC
Both parties recorded

### Description
1. Action: Set up call A from B
2. Confirm: Two way media
3. Action: Blind transfer B to C
4. Confirm: A drops out of call
5. Confirm: Two way media
6. Action: End call
7. Confirm: Two call recordings
  - A - B
  - B - C -->

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start `call B`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_04_blind_xfer/3pcc_04c_blind_xfer_callB.xml -m 1
```

Start `call A`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_04_blind_xfer/3pcc_04c_blind_xfer_callA.xml -m 1
```
