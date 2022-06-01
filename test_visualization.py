
from brane_visualization import visualization
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual( visualization(),"Visualization is done, all the files are saved to the directory -> ./data/")

    # def test_add():
    #     assert 1+1 == 2 '1+1 == 2 is right'

if __name__=="__main__":
    unittest.main()