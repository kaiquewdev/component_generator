'''Tags Test'''

import os
import unittest
import generate_component

class LinkTest(unittest.TestCase):
    def setUp(self):
        self.link = generate_component.Link()

    def test_link_instantiation(self):
        self.assertEqual(self.link.__class__,generate_component.Link)

    def test_link_str(self):
        self.assertEqual(self.link.__str__(),'<link rel="stylesheet" href="./css/component-example-standalone.css">')

class HeaderTest(unittest.TestCase):
    def setUp(self):
        self.header = generate_component.Header()

    def test_header_instantiation(self):
        self.assertEqual(self.header.__class__,generate_component.Header)

    def test_header_str(self):
        self.assertEqual(self.header.__str__(),'<h1>Component Example Standalone</h1>')

class ParagraphTest(unittest.TestCase):
    def setUp(self):
        self.paragraph = generate_component.Paragraph()

    def test_paragraph_instantiation(self):
        self.assertEqual(self.paragraph.__class__,generate_component.Paragraph)

    def test_paragraph_str(self):
        self.assertEqual(self.paragraph.__str__(),'<p>Modularized architecture</p>')

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
