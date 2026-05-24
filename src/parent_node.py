from html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str]|None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have at least one child")
        return_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            return_string += child.to_html()
        return_string += f"</{self.tag}>"
        return return_string

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
