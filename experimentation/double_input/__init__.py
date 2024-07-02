import check50
import check50.c
import re


@check50.check()
def exists():
    """double_input.c exists"""
    check50.exists("double_input.c")


@check50.check(exists)
def compiles():
    """double_input.c compiles"""
    check50.c.compile("double_input.c", lcs50=False)


@check50.check(compiles)
def test():
    """sum of 2 and 3"""
    obj = check50.run("./double_input")
    # stdin(line, str_line=None, prompt=True, timeout=3)
    obj = obj.stdin(line="2", str_line="entered first number", prompt=True, timeout=3)
    obj = obj.stdin(line="3", str_line="entered second number", prompt=True, timeout=3)
    # stdout(output=None, str_output=None, regex=True, timeout=3, show_timeout=False)
    obj = obj.stdout(output="The sum of 2 and 3 is 5.\n", str_output="Display the sum", regex=True, timeout=3, show_timeout=True)
    obj.exit(0)
