def markdown_to_blocks(markdown: str) -> list[str]:
    return_list = []
    split_strings = markdown.split("\n\n")
    for string in split_strings:
        if len(string) < 1:
            continue
        return_list.append(string.strip())

    return return_list
