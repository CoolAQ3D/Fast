import os

def tools(value):
  if value in "clear":
    cls = lambda: print("\033c\033[3J", end='')
    cls()
  elif value in "pycache":
    os.system("find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete")