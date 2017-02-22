'''Tags Test'''

import unittest
import generate_component

class LinkTest(unittest.TestCase):
    def setUp(self):
        self.link = generate_component.Link()

    def test_link_instantiation(self):
        self.assertEqual(self.link.__class__,generate_component.Link)

    def test_link_str(self):
        self.assertEqual(self.link.__str__(),'<link rel="stylesheet" href="./css/component-example-standalone.css">')

if __name__ == '__main__':
    unittest.main(verbosity=2)
