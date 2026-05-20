import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://test.com/test.png)"
        )
        self.assertListEqual([("image", "https://test.com/test.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with two images ![image](https://test.com/test.png) and ![image2](https://test.com/test2.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://test.com/test.png"),
                ("image2", "https://test.com/test2.png"),
            ], matches)

    def test_extract_markdown_with_link(self):
        matches = extract_markdown_images(
            "This is text with not an [image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [], matches
        )

    def test_extract_markdown_with_both(self):
        matches = extract_markdown_images(
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [("image", "https://test.com/test.png")], matches
        )

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")], matches
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with two links [to boot dev](https://www.boot.dev)  and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ], matches
        )

    def test_extract_markdown_with_image(self):
        matches = extract_markdown_links(
            "This is not text with a link ![to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [], matches
        )

    def test_extract_markdown_with_both(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://test.com/test.png)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")], matches
        )

if __name__ == "__main__":
    unittest.main()
