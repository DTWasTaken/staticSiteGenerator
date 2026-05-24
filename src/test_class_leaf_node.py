import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            leaf_node.to_html(),
            "<p>This is a paragraph of text.</p>"
        )

    def test_to_html_with_props(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            leaf_node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(None, "This is plain text.")
        self.assertEqual(leaf_node.to_html(), "This is plain text.")

    def test_without_value(self):
        leaf_node = LeafNode("a", None)
        with self.assertRaises(ValueError) as cm:
            leaf_node.to_html()
        self.assertEqual(
            str(cm.exception),
            "All leaf nodes must have a value"
        )


if __name__ == "__main__":
    unittest.main()
