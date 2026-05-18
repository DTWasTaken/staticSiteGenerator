import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
        props_to_html = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props_to_html, expected)

    def test_props_to_html_none(self):
        node = HTMLNode()
        props_to_html = node.props_to_html()
        expected = ""
        self.assertEqual(props_to_html, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        props_to_html = node.props_to_html()
        expected = ""
        self.assertEqual(props_to_html, expected)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        to_html = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(to_html, expected)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        to_html = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(to_html, expected)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is plain text.")
        to_html = node.to_html()
        expected = "This is plain text."
        self.assertEqual(to_html, expected)

if __name__ == "__main__":
    unittest.main()
