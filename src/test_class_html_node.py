import unittest

from html_node import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
