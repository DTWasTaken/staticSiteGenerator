from src.types.html_node import HTMLNode
from src.functions.block_to_block_type import block_to_block_type
from src.types.block_type import BlockType


def mardown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                pass
            case BlockType.HEADING:
                pass
            case BlockType.ORDERED_LIST:
                pass
            case BlockType.PARAGRAPH:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass

def markdown_to_blocks(markdown: str) -> list[str]:
    return_list = []
    split_strings = markdown.split("\n\n")
    for string in split_strings:
        if len(string) < 1:
            continue
        return_list.append(string.strip())

    return return_list

def text_to_children(text: str) -> list[HTMLNode]:
    pass
