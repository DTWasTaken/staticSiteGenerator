from copy_dir_to_fresh import copy_dir_to_fresh
from generate_pages_recursive import generate_pages_recursive


def main():
    copy_dir_to_fresh("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
