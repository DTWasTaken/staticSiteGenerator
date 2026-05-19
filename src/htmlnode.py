class HTMLNode:
    def __init__(self, tag: str|None = None, value: str|None = None, children: list[HTMLNode]|None = None, props: dict[str]|None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        return_string = ""

        if self.props is None or self.props == {}:
            return return_string

        for key, value in self.props.items():
            return_string += f" {key}=\"{value}\""

        return return_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str|None, value: str, props: dict[str]|None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        elif self.tag is "img":
            return f"<{self.tag}{self.props_to_html()} />"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

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
