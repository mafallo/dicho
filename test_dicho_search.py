import unittest
import my_search

class TestDicho(unittest.TestCase):
	

	def test_do_nothing(self):
		self.assertEqual(my_search.default_search(0, 0), False)
	
	def test_shouldReturnFalseIfNotFound(self):
		self.assertEqual(my_search.default_search(5, 3), False)
		self.assertEqual(my_search.dicho(5, list(range(3)),0), False)
	
	def test_shouldReturnTrueFound(self):
		self.assertEqual(my_search.default_search(5000, 100_000), True)

	def test_shouldReturnTrueIfFoundWithDico(self):
	 	result = my_search.dicho(5000, list(range(100_000)), 0)
	 	self.assertEqual(result, 5000)

if __name__ == '__main__':
	unittest.main()