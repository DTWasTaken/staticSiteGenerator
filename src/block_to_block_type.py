import re
from block_type import BlockType


def block_to_block_type(md_block: str) -> BlockType:
    match True:
        case _ if re.match(r"^#{1,6} .*?$", md_block):
            return BlockType.HEADING

        case _ if _is_code_block(md_block):
            return BlockType.CODE

        case _ if _each_line_matches_regex(r"^> ?.*?$", md_block):
            return BlockType.QUOTE

        case _ if _each_line_matches_regex(r"^- .*?$", md_block):
            return BlockType.UNORDERED_LIST

        case _ if _is_ordered_list(md_block):
            return BlockType.ORDERED_LIST

        case _:
            return BlockType.PARAGRAPH


def _is_code_block(block: str) -> bool:
    if not (
        block.startswith("```\n")
        and block.endswith("```")
    ):
        return False

    return True


def _each_line_matches_regex(expression: str, block: str) -> bool:
    lines = block.split("\n")

    if len(lines) == 0:
        return False

    for line in lines:
       if not re.match(expression, line):
           return False

    return True


def _is_ordered_list(block: str) -> bool:
    lines = block.split("\n")

    if len(lines) == 0:
        return False

    number = 1

    for line in lines:
        if not re.match(rf"^{str(number)}\. .*?$", line):
            return False
        number += 1

    return True
