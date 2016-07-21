import Canopy
import pprint as pp
import unittest

a = Canopy.Acano("192.168.12.200", "admin", "admin")

#a.get_coSpaces(self, parameters = {})

print(a.get_coSpaces())
if(a.get_coSpaces()["coSpaces"]["@total"] != "0"):
	for cs in a.get_coSpaces()["coSpaces"]["coSpace"]:
		a.delete_coSpace(cs["@id"])

print("coSpaces in memory: ", a.get_coSpaces()["coSpaces"]["@total"])

print("coSpace methods ###############################################")

csid = a.create_coSpace()["@id"]
print(a.modify_coSpace(csid, payload = {
	"name" : "George"
	}))
print(a.get_coSpace(csid))
print(a.delete_coSpace(csid))

csid = a.create_coSpace()["@id"]

print("User profile methods ###############################################")


a.get_user_profiles()

up = a.create_user_profile()["@id"]
print(a.modify_user_profile(up, payload = {
	'cancreateCoSpaces' : True,
	'userJid' : 'george@cisco.com'
	}))
print(a.get_user_profile(up))

print("Add user profile to coSpace###############################################")

pp.pprint(a.get_user_profiles())







































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
