from src.types.text_node import TextNode
from src.types.text_type import TextType
from src.functions.split_nodes_delimiter import split_nodes_delimiter
from src.functions.split_nodes_url import split_nodes_url
from src.types.markdown_url_type import MarkdownURLType


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)

    return_list = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    return_list = split_nodes_delimiter(return_list, "_", TextType.ITALIC)
    return_list = split_nodes_delimiter(return_list, "`", TextType.CODE)
    return_list = split_nodes_url(MarkdownURLType.IMAGE, return_list)
    return_list = split_nodes_url(MarkdownURLType.LINK, return_list)

    return return_list
