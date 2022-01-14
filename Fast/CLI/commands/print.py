from rich.console import Console
from Fast.CLI import add_help

console = Console()

def print(args, style=None):

  add_help(
    name = "print",
    description = "print with stylies",
    usage = "fast print (optional: rich style)",
    subcommands = []
  )

  console.print(args, style=style)