import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_startswith(self):
        node = TextNode("**This** is text with a bold word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This", TextType.BOLD),
            TextNode(" is text with a bold word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_endswith(self):
        node = TextNode("This is text with a bold **word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a bold ", TextType.TEXT),
            TextNode("word", TextType.BOLD),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic(self):
        node = TextNode("This is text with an _italicized_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_multi(self):
        node = TextNode(
            "This is text with a `code block`, **bold**, and _italics_ words",
            TextType.TEXT
            )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", and ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" words", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_none(self):
        node = TextNode("This is text with no formatted words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with no formatted words", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_match(self):
        node = TextNode("This is an invalid `markdown syntax", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_too_many_matches(self):
        node = TextNode("This `is `an invalid `markdown syntax", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
