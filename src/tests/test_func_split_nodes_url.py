import unittest

from src.functions.split_nodes_url import extract_markdown_urls
from src.functions.split_nodes_url import split_nodes_url
from src.classes.markdown_url_type import MarkdownURLType
from src.classes.text_node import TextNode
from src.classes.text_type import TextType


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_urls(
            MarkdownURLType.IMAGE,
            "This is text with an ![image](https://test.com/test.png)"
        )
        self.assertListEqual([("image", "https://test.com/test.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_urls(
            MarkdownURLType.IMAGE,
            "This is text with two images ![image](https://test.com/test.png) and ![image2](https://test.com/test2.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://test.com/test.png"),
                ("image2", "https://test.com/test2.png"),
            ], matches)

    def test_extract_markdown_with_link(self):
        matches = extract_markdown_urls(
            MarkdownURLType.IMAGE,
            "This is text with not an [image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [], matches
        )

    def test_extract_markdown_with_both(self):
        matches = extract_markdown_urls(
            MarkdownURLType.IMAGE,
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [("image", "https://test.com/test.png")], matches
        )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_urls(
            MarkdownURLType.LINK,
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")], matches
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_urls(
            MarkdownURLType.LINK,
            "This is text with two links [to boot dev](https://www.boot.dev)  and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ], matches
        )

    def test_extract_markdown_with_image(self):
        matches = extract_markdown_urls(
            MarkdownURLType.LINK,
            "This is not text with a link ![to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [], matches
        )

    def test_extract_markdown_with_both(self):
        matches = extract_markdown_urls(
            MarkdownURLType.LINK,
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")], matches
        )


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_and_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a [link](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_multi(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is another text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is another text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This is text without an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("This is text without an image", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_with_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                    TextType.TEXT
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_image_alt(self):
        node = TextNode(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_image_link(self):
        node = TextNode(
            "This is text with an ![image]()",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, ""),
            ],
            new_nodes,
        )

    def test_split_images_no_other_text(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.IMAGE, [node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_images_and_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links_multi(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is another text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode("This is another text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode(
            "This is text without a link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("This is text without a link", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_with_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                    TextType.TEXT
                ),
            ],
            new_nodes,
        )

    def test_split_links_no_link_text(self):
        node = TextNode(
            "This is text with a link [](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_links_no_link_url(self):
        node = TextNode(
            "This is text with a link [to boot dev]()",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, ""),
            ],
            new_nodes,
        )

    def test_split_links_no_other_text(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_url(MarkdownURLType.LINK, [node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
