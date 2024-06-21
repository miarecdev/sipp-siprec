
# 19 - Shared Line

## Test Case A
Multiple call appearances recorded

### Setup
Two phones registered to E (E1 and E2)

### Description:
1. Action: Set up a call from G to E1
2. Confirm: Two way media
3. Action: While G to E1 call is active set up a call between B and E and answer on E2 (on the other phone sharing E)
4. Confirm: Two way media on both calls
5. Action: Hang up call B to E2
6. Confirm: Two way media in G to E1 call
7. Action: End call G to E1
8. Confirm: Two call recordings:
    - One for G and E1 call
    - One for B and E2 call

Confirm: Entirety of both calls is recorded

### Run scenario - Call A
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_19_shared_line/19a_shared_line_callA.xml -m 1
```

### Run scenario - Call B
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_19_shared_line/19a_shared_line_callB.xml -m 1
```

## Test Case A - 3PCC
Multiple call appearances recorded

### Setup
Two phones registered to E (E1 and E2)

### Description:
1. Action: Set up a call from G to E1
2. Confirm: Two way media
3. Action: While G to E1 call is active set up a call between B and E and answer on E2 (on the other phone sharing E)
4. Confirm: Two way media on both calls
5. Action: Hang up call B to E2
6. Confirm: Two way media in G to E1 call
7. Action: End call G to E1
8. Confirm: Two call recordings:
    - One for G and E1 call
    - One for B and E2 call

Confirm: Entirety of both calls is recorded

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start `call B`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -sf scenarios/metaswitch_19_shared_line/3pcc_19a_shared_line_callB.xml -m 1
```

Start `call A`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -sf scenarios/metaswitch_19_shared_line/3pcc_19a_shared_line_callA.xml -m 1
```


## Test Case B
Public call hold with a shared line is recorded

### Setup
Two phones registered to E (E1 and E2)

### Description:
1. Action: Set up a call between B and E1
2. Confirm: Two way media
3. Action: From E1 put B on hold
4. Confirm: A hears music on hold
5. Action: From E2 take B off hold
6. Confirm: Two way media
7. Action: End call
8. Confirm: Two recordings made:
  - B - E1
  - B - E2


### Run scenario - Call A

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_19_shared_line/19b_shared_line_callA.xml -m 1
```

### Run scenario - Call B

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_19_shared_line/19b_shared_line_callB.xml -m 1
```


## Test Case B - 3PCC
Public call hold with a shared line is recorded

### Setup
Two phones registered to E (E1 and E2)

### Description:
1. Action: Set up a call between B and E1
2. Confirm: Two way media
3. Action: From E1 put B on hold
4. Confirm: A hears music on hold
5. Action: From E2 take B off hold
6. Confirm: Two way media
7. Action: End call
8. Confirm: Two recordings made:
  - B - E1
  - B - E2

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start `call B`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/3pcc_19b_shared_line_callB.xml -m 1
```

Start `call A`
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/3pcc_19b_shared_line_callA.xml -m 1
```


## Test Case C
Public call hold with a shared line is recorded part b

### Setup
Two phones registered to H (H1 and H2)

### Description:
1. Action: Set up a call between A and H1
2. Confirm: Two way media
3. Action: From H1 put A on hold
4. Confirm: A hears music on hold
5. Action: From H2 take A off hold
6. Confirm: two way media
7. Action: Hang up call
Confirm: One recording made with three parts. A - H1, MoH, A - H2 -->


### Run scenario - Call A
`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -sf scenarios/metaswitch_19_shared_line/19c_shared_line.xml -m 1
```
