import unittest
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.boot.dev"}
        )

    def test_image(self):
        node = TextNode(
            "This is a image node",
            TextType.IMAGE,
            "/link/to/image.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "/link/to/image.png", "alt": "This is a image node"}
        )

    def test_nonexistant_text_type(self):
        node = TextNode("This is a nonexistant node", "nonexistant")
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(
            str(cm.exception),
            "nonexistant is not a valid text type"
        )


if __name__ == "__main__":
    unittest.main()
