



## Test Casse A

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start participant B
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/19a_shared_line_callB.xml -m 1
```

Start participant A
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/19a_shared_line_callA.xml -m 1
```


## Test Casse B

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start participant B
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/19b_shared_line_callB.xml -m 1
```

Start participant A
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_19_shared_line/19b_shared_line_callA.xml -m 1
```

