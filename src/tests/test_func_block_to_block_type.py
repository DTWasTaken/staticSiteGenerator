import unittest

from src.functions.block_to_block_type import block_to_block_type
from src.classes.block_type import BlockType


class TestBlockToBlockType(unittest.TestCase):
    # md.strip() because we only expext strings that come from markdown_to_blocks()
    def test_paragraph(self):
        md = "Test"
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        md = """
Test
Line 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_h1(self):
        md = "# Test"
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.HEADING)

    def test_h6(self):
        md = "###### Test"
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.HEADING)

    def test_h7(self):
        md = "####### Test"
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_multiline(self):
        md = """
# multiline
not supported
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_invalid(self):
        md = "######test"
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code(self):
        md = """
```
this is some code
```
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_multiline(self):
        md = """
```
this is some code


this is some more code
```
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_invalid(self):
        md = """
```invalid
this is some code


this is some more code
```
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote(self):
        md = """
> This is a quote
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_multiline(self):
        md = """
> This is a quote
>The space isn't required
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_invalid(self):
        md = """
> This is a quote
 >The space isn't required
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = """
- This is a list
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_multiline(self):
        md = """
- This is a list
- item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid(self):
        md = """
- This is a list
-item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        md = """
1. This is a list
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_multiline(self):
        md = """
1. This is a list
2. item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_no_space(self):
        md = """
1. This is a list
2.item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_no_period(self):
        md = """
1. This is a list
2 item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_non_sequential(self):
        md = """
1. This is a list
3. item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_not_start_at_1(self):
        md = """
2. This is a list
3. item 2
"""
        block_type = block_to_block_type(md.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
