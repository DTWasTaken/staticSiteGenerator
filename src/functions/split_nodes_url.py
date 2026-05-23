import re

from src.classes.text_node import TextNode
from src.classes.text_type import TextType
from src.classes.markdown_url_type import MarkdownURLType


def split_nodes_url(url_type: MarkdownURLType, old_nodes: list[TextNode]) -> list[TextNode]:
    # New list of nodes to build and return
    return_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Node type is already set and doesn't need to be processed
            return_nodes.append(node)
            continue

        urls = extract_markdown_urls(url_type, node.text)

        if len(urls) < 1:
            # No urls found in node, add it and move on
            return_nodes.append(node)
            continue

        # temp list to hold newly created nodes
        new_nodes = []

        node_text = node.text

        if url_type is MarkdownURLType.IMAGE:
            prefix = "!"
            text_type = TextType.IMAGE
        elif url_type is MarkdownURLType.LINK:
            prefix = ""
            text_type = TextType.LINK

        for text, url in urls:
            split = node_text.split(f"{prefix}[{text}]({url})", 1)
            if len(split[0]) > 0:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(text, text_type, url))
            node_text = split[1]

        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))

        # Add temp list to return list
        return_nodes.extend(new_nodes)

    return return_nodes


def extract_markdown_urls(url_type: MarkdownURLType, text: str) -> list[tuple[str]]:
    match url_type:
        case MarkdownURLType.IMAGE:
            prefix = r'(?<=!)'
        case MarkdownURLType.LINK:
            prefix = r'(?<!!)'
        case _:
            raise ValueError(f'Markdown URL Type "{url_type}" is invalid')

    return re.findall(rf"{prefix}\[(.*?)\]\((.*?)\)", text)
