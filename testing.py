import Canopy
import pprint as pp
import unittest

a = Canopy.Acano("192.168.12.201", "admin", "admin")

class TestAcano(unittest.TestCase):
	def setUp(self):
		coSpaces = a.get_coSpaces()
		print()
		if(coSpaces["coSpaces"]["@total"] != "0"):
			coSpaces = coSpaces["coSpaces"]["coSpace"]
			for cs in coSpaces:
				a.delete_coSpace(cs["@id"])

	def test_no_coSpaces(self):
		self.assertEqual(a.get_coSpaces()["coSpaces"]["@total"], "0")


if __name__ == '__main__':
	unittest.main()
	input()


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
