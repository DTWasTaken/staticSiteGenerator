from copy_dir_to_fresh import copy_dir_to_fresh
from generate_page import generate_page


def main():
    copy_dir_to_fresh("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

if __name__ == "__main__":
    main()
