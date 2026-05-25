import sys

from copy_dir_to_fresh import copy_dir_to_fresh
from generate_pages_recursive import generate_pages_recursive


def main():
    if len(sys.argv) == 1:
        basepath = "/"
    elif len(sys.argv) == 2:
        basepath = str(sys.argv[1])
    else:
        raise Exception("Please pass zero or one arguments only")

    copy_dir_to_fresh("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)


if __name__ == "__main__":
    main()
