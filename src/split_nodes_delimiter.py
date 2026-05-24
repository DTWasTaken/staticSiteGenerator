from text_type import TextType
from text_node import TextNode


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

        if len(text_list) % 2 == 0:
            # Node doesn't have a matching closing delimiter
            #  or had multiple more than one pair of delimiters
            #  which is unsupported
            raise ValueError(f'Node has invalid syntax:\n{node.text}')

        # temp list to hold newly created nodes
        new_nodes = []

        for i in range(len(text_list)):
            if i % 2 == 0:
                # even indexes should be text
                if len(text_list[i]) > 0:
                    new_nodes.append(TextNode(text_list[i], TextType.TEXT))
            else:
                # odd indexes should be formatted
                new_nodes.append(TextNode(text_list[i], text_type))

        # Add temp list to return list
        return_nodes.extend(new_nodes)

    return return_nodes
