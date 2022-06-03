
from brane_visualization import visualization
import unittest


class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual( visualization(('/data', '/data')), "Visualization is done, all the files are saved to the directory -> ./data/")


if __name__=="__main__":
    unittest.main()
