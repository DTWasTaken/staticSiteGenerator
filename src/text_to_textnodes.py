from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)

    return_list = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    return_list = split_nodes_delimiter(return_list, "_", TextType.ITALIC)
    return_list = split_nodes_delimiter(return_list, "`", TextType.CODE)
    return_list = split_nodes_image(return_list)
    return_list = split_nodes_link(return_list)

    return return_list
