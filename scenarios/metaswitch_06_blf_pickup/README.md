## Test Case A
### Summary
Call intercepted by recorded party
### Setup
A configured to monitor B
### Description
	1. Action: From G call B
	2. Confirm: Enhanced Monitored Extension (EME) key on A flashes
	3. Action: Press EME key on A
	4. Confirm: A is now in call with G
	5. Confirm: Two way media
	6. Action: End call
Confirm: Call recorded A - G

### Run scenario

`1.1.1.1` = miarec IP address
`2.2.2.2` = local ip address

```
sipp 1.1.1.1:5080 -i 2.2.2.2 -t t1 -inf scenarios/tenant-users.csv -sf scenarios/metaswitch_06_blf_pickup/06a_blf_pickup.xml -m 1
```
