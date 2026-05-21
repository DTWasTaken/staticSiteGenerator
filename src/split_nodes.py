import re

from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
    ) -> list[TextNode]:

    # New list of nodes to build and return
    return_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Node type is already set and doesn't need to be processed
            return_nodes.append(node)
            continue

        if delimiter not in node.text:
            # Node is either plain text or a different delimiter
            #  and also doesn't need to be processed
            return_nodes.append(node)
            continue

        # Split the text by delimiter
        text_list = node.text.split(delimiter)

        if len(text_list) != 3:
            # Node doesn't have a matching closing delimiter
            #  or had multiple more than one pair of delimiters
            #  which is unsupported
            raise ValueError(f'Node has invalid syntax:\n{node.text}')

        # temp list to hold newly created nodes
        new_nodes = []

        # indexes 0 and 2 may be empty if the sting started with a delim
        if len(text_list[0]) > 0:
            new_nodes.append(TextNode(text_list[0], TextType.TEXT))

        # index 1 should always be the string to format
        new_nodes.append(TextNode(text_list[1], text_type))

        if len(text_list[2]) > 0:
            new_nodes.append(TextNode(text_list[2], TextType.TEXT))

        # Add temp list to return list
        return_nodes.extend(new_nodes)

    return return_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    # New list of nodes to build and return
    return_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Node type is already set and doesn't need to be processed
            return_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) < 1:
            # No images found in node, add it and move on
            return_nodes.append(node)
            continue

        # temp list to hold newly created nodes
        new_nodes = []

        text = node.text

        for image_alt, image_link in images:
            split = text.split(f"![{image_alt}]({image_link})", 1)
            if len(split[0]) > 0:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text = split[1]

        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))

        # Add temp list to return list
        return_nodes.extend(new_nodes)

    return return_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    # New list of nodes to build and return
    return_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Node type is already set and doesn't need to be processed
            return_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if len(links) < 1:
            # No links found in node, add it and move on
            return_nodes.append(node)
            continue

        # temp list to hold newly created nodes
        new_nodes = []

        text = node.text

        for link_text, link_url in links:
            split = text.split(f"[{link_text}]({link_url})", 1)
            if len(split[0]) > 0:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text = split[1]

        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))

        # Add temp list to return list
        return_nodes.extend(new_nodes)

    return return_nodes
