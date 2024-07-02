import check50
import check50.c
import re


@check50.check()
def exists():
    """namasthey.c exists"""
    check50.exists("namasthey.c")


@check50.check(exists)
def compiles():
    """namasthey.c compiles"""
    check50.c.compile("namasthey.c", lcs50=True)


@check50.check(compiles)
def rama():
    """responds to name Rama"""
    check_name("Rama")


@check50.check(compiles)
def krishna():
    """responds to name Krishna"""
    check_name("Krishna")


@check50.check(compiles)
def hanuman():
    """responds to name Hanuman"""
    check_name("Hanuman")

@check50.check(compiles)
def shiva():
    """responds to name Shiva"""
    check_name("Shiva")

def check_name(name):
    # Define expected, actual outputs
    expected = f"Namasthey, {name}\n"
    actual = check50.run("./namasthey").stdin(name).stdout()

    # Check output
    if not re.match(regex(name), actual):
        try:
            last_character = actual[-1]
        except IndexError:
            raise check50.Mismatch(expected=expected, actual=actual)

        if last_character != "\n":
            raise check50.Mismatch(
                expected=expected,
                actual=actual,
                help=r"Forgot to print a newline at the end of your output?",
            )
        raise check50.Mismatch(expected=expected, actual=actual)


def regex(string):
    return f"Namasthey, {re.escape(string)}\n$"
