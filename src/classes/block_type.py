from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code block"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
