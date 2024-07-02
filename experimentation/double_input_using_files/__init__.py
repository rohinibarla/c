import check50
import check50.c

@check50.check()
def exists():
    """double_input.c exists"""
    check50.exists("double_input.c")
    check50.include("input1.txt", "output1.txt")

@check50.check(exists)
def compiles():
    """double_input.c compiles"""
    check50.c.compile("double_input.c", lcs50=False)

@check50.check(compiles)
def test_sum1():
    """sum test#1"""
    test_input_output("./double_input", "input1.txt", "output1.txt")

# Helpers
def test_input_output(executable, input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()

