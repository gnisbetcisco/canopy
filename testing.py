import AcanoPy
import pprint as pp

a = AcanoPy.Acano("192.168.12.200", "admin", "admin")
print(a.get_coSpaces())

print(a.get_user_profiles())

#print(a.add_ldap_server())











































'''

try:
	if(root["@total"] == "1"): # Attempt to find a 'total' of items 

		li = list()
		childName = list(root.keys())[1]
		print(childName)

		print(root[childName])
		print("-------------")
		print(type(root[childName]))

		li.append(root[childName].copy())

		root[childName] = li

		response[rootName] = root

		pp.pprint(response)

		print(csid)

		#pp.pprint(root)
		#We need to make it a list
except KeyError:
	print("Nothing to do")

'''

#childName = list(root.keys())[0]


input()
