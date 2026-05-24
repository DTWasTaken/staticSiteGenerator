import re


def extract_title(markdown: str) -> str:
    match = re.search(r"^# (?P<title>.+)\n?", markdown, re.MULTILINE)

    no_title_error_message = "No title found in markdown document"

    if match is None:
        raise ValueError(no_title_error_message)

    try:
        title = match.group("title")
    except IndexError:
        raise ValueError(no_title_error_message)

    return title.strip()
