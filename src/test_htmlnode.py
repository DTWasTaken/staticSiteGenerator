import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("p", "1")
        child_node2 = LeafNode("p", "2")
        child_node3 = LeafNode("p", "3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>1</p><p>2</p><p>3</p></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node], {"class": "test"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="test"><a href="https://www.google.com">Click me!</a></div>'
        )

    def test_without_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(
            str(cm.exception),
            "All parent nodes must have at least one child"
        )

    def test_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(
            str(cm.exception),
            "All parent nodes must have a tag"
        )

if __name__ == "__main__":
    unittest.main()
