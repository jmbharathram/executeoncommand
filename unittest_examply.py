import unittest 

class TestStringMethods(unittest.TestCase): 
	
	def setUp(self): 
		pass

	# Returns True if the string contains 4 a. 
	def test_strings_a(self): 
		self.assertEqual( 'a'*4, 'aaaa') 

	# Returns True if the string is in upper case. 
	def test_upper(self):		 
		self.assertEqual('foo'.upper(), 'FOO') 

	# Returns TRUE if the string is in uppercase 
	# else returns False. 
	def test_isupper(self):		 
		self.assertTrue('FOO'.isupper()) 
		self.assertFalse('Foo'.isupper()) 

	# Returns true if the string is stripped and 
	# matches the given output. 
	def test_strip(self):		 
		s = 'geeksforgeeks'
		self.assertEqual(s.strip('geek'), 'sforgeeks') 

	# Returns true if the string splits and matches 
	# the given output. 
	def test_split(self):		 
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world']) 
		with self.assertRaises(TypeError): 
			s.split(2) 

if __name__ == '__main__': 
	unittest.main()
