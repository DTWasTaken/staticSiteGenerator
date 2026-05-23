import unittest

from src.types.parent_node import ParentNode
from src.types.leaf_node import LeafNode


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
