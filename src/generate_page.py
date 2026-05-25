import os

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown = f.read()
        f.close()

    with open(template_path, 'r') as f:
        template = f.read()
        f.close()

    html_node = markdown_to_html_node(markdown)

    html_content = html_node.to_html()

    html_title = extract_title(markdown)

    html_page = template.replace(
        "{{ Title }}", html_title
        ).replace(
            "{{ Content }}", html_content
        ).replace(
            'href="/', f'href="{basepath}'
        ).replace(
            'src="/', f'src="{basepath}'
        )

    dest_dir_path, _ = dest_path.split("/index.html")

    os.makedirs(dest_dir_path, exist_ok=True)

    with open(f"{dest_path}", 'w') as f:
        f.write(html_page)
        f.close()
