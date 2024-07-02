import check50
import check50.c
import re


@check50.check()
def exists():
    """default.c exists"""
    check50.exists("default.c")


@check50.check(exists)
def compiles():
    """default.c compiles"""
    check50.c.compile("default.c", lcs50=False)


@check50.check(compiles)
def test1():
    """input of 1 outputs 1"""
    obj = check50.run("./default")
    # stdin(line, str_line=None, prompt=True, timeout=3)
    obj = obj.stdin(line="44", str_line="entered age 44", prompt=True, timeout=3)
    # stdout(output=None, str_output=None, regex=True, timeout=3, show_timeout=False)
    obj = obj.stdout(output="You are 44 years old.\n", str_output="Display the age", regex=True, timeout=3, show_timeout=True)
    obj.exit(0)

