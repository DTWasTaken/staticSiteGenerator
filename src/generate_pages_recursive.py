import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    md_files = find_all_md_docs_in_tree(dir_path_content)
    for md_file in md_files:
        _, file_name = md_file.split(dir_path_content)
        destination_file = dest_dir_path + file_name[:-3] + ".html"
        generate_page(md_file, template_path, destination_file)

def find_all_md_docs_in_tree(start_dir: str) -> list[str]:
    visited = []
    md_files_found = []
    find_all_md_docs_in_tree_r(visited, start_dir, md_files_found)
    return md_files_found

def find_all_md_docs_in_tree_r(
    visited: list[str],
    working_dir: str,
    md_files_found: list[str],
    ) -> list[str]:

    visited.append(working_dir)
    # get sorted list of working dirs children
    children = sorted(os.listdir(working_dir))

    for child in children:
        child_path = working_dir + "/" + child
        # if child is named index.md, add path to md_files_found
        if child.endswith(".md") and os.path.isfile(child_path):
            md_files_found.append(child_path)
            continue

        # if child is not a dir nor an .md file, ignore
        if not os.path.isdir(child_path):
            continue

        # if child is not in visited, recurse into child
        if child_path not in visited:
            find_all_md_docs_in_tree_r(visited, child_path, md_files_found)
