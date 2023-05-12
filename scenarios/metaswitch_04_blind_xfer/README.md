





### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

Start participant B
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_04_blind_xfer/04c_blind_xfer_callB.xml -m 1
```

Start participant A
```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -3pcc 2.2.2.2:7777 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_04_blind_xfer/04c_blind_xfer_callA.xml -m 1
```
