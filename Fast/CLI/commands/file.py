
import os, pathlib, sys

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


from rich.console import Console

console = Console()


#Shows file info
def file(value, args, start_location="/home/runner"):
  
  if value in "create":
    filename = args
    open(filename, "w")
    print(f'Created {filename}')
  
  elif value in "path":
    result = []
    filename = args

    if start_location in "home":
      start_location = "/home/runner"
    elif start_location in "library":
      start_location = "/opt/virtualenvs/python3/lib/python3.8/site-packages"
    
    print(f"Searching from {start_location}")

    # Wlaking top-down from the root
    for root, dir, files in os.walk(start_location):
      if filename in files:
         result.append(os.path.join(root, filename))
  
    if len(result) == 0:
      print("File not found! Probably doesn't exist!")
      return None
    else:
      print(result)
      return result

  elif value in "view":
    path = args
    tree = Tree(
      f"Main File Area - {os.getcwd()}",
      guide_style="bold bright_blue",
      )
    walk_directory(path, tree)
    console.print(tree)



def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
    """Recursively build a Tree with directory contents."""
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue
        if path.parts[-1] == "venv":
            continue
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, branch)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            icon = "🐍 " if path.suffix == ".py" else "📄 "
            tree.add(Text(icon) + text_filename)

