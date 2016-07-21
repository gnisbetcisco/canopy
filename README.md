# Canopy n. A python SDK for Cisco Acano.

The full documentation can be viewed here:
http://canopy.readthedocs.io/en/latest/

Getting started, quickly:

```python

acano_vm_ip = "192.168.12.100"
username = "admin"
password = "admin"

a = Acano(acano_vm_ip, username, password)

coSpace_id = a.create_coSpace()["@id"]

print(a.modify_coSpace(coSpace_id, payload = {
	"name" : "George"
	}))
print(a.get_coSpace(coSpace_id))
print(a.delete_coSpace(coSpace_id))
```