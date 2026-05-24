import re

from html_node import HTMLNode
from parent_node import ParentNode
from leaf_node import LeafNode
from block_to_block_type import block_to_block_type
from block_type import BlockType
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import textnode_to_htmlnode
from text_node import TextNode
from text_type import TextType


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                block_node = ParentNode("pre", [])
                cleaned_text = _clean_code_md(block)
            case BlockType.HEADING:
                heading_depth = len(block) - len(block.lstrip("#"))
                block_node = ParentNode(f"h{str(heading_depth)}", [])
                cleaned_text = _clean_h_md(block, heading_depth)
            case BlockType.ORDERED_LIST:
                block_node = ParentNode("ol", [])
                cleaned_text = _clean_list_md(block)
            case BlockType.PARAGRAPH:
                block_node = ParentNode("p", [])
                cleaned_text = _clean_p_md(block)
            case BlockType.QUOTE:
                block_node = ParentNode("blockquote", [])
                cleaned_text = _clean_blockquote_md(block)
            case BlockType.UNORDERED_LIST:
                block_node = ParentNode("ul", [])
                cleaned_text = _clean_list_md(block)

        if block_type is BlockType.CODE:
            text_node = TextNode(cleaned_text, TextType.CODE)
            child = textnode_to_htmlnode(text_node)
            block_node.children.append(child)
            block_nodes.append(block_node)
            continue

        children = _text_to_children(cleaned_text)
        block_node.children.extend(children)
        block_nodes.append(block_node)

    parent_node = ParentNode("div", block_nodes)

    return parent_node

def markdown_to_blocks(markdown: str) -> list[str]:
    return_list = []
    split_strings = markdown.split("\n\n")
    for string in split_strings:
        if len(string) < 1:
            continue
        return_list.append(string.strip())

    return return_list

def _text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    return_list = []
    for text_node in text_nodes:
        return_list.append(textnode_to_htmlnode(text_node))

    return return_list

def _clean_code_md(text: str) -> str:
    return text[4:-3]

def _clean_p_md(text: str) -> str:
    return text.replace("\n", " ")

def _clean_h_md(text: str, heading_depth: int) -> str:
    return text[heading_depth + 1:]

def _clean_list_md(text: str) -> str:
    text_split = text.split("\n")
    return_str = ""

    for item in text_split:
        _, rest_of_text = item.split(" ", 1)
        return_str += "<li>" + rest_of_text + "</li>"

    return return_str

def _clean_blockquote_md(text: str) -> str:
    text_split = text.split("\n")
    temp_list = []

    for item in text_split:
        _, rest_of_text = item.split(">", 1)
        if rest_of_text.startswith(" "):
            _, rest_of_text = rest_of_text.split(" ", 1)
        temp_list.append(rest_of_text)

    return_str = "\n".join(temp_list)

    return return_str

