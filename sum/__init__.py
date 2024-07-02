
import check50
import check50.c

@check50.check()
def exists():
    """sum.c exists"""
    check50.exists("sum.c")
    check50.include("sum_2_3_input.txt", "sum_2_3_output.txt")
    check50.include("sum_20_22_input.txt", "sum_20_22_output.txt")
    check50.include("sum_10_20_input.txt", "sum_10_20_output.txt")

@check50.check(exists)
def compiles():
    """sum.c compiles"""
    check50.c.compile("sum.c", lcs50=False)


@check50.check(compiles)
def sum_2_3():
    """sum_2_3"""
    test_input_output("./sum", "sum_2_3_input.txt", "sum_2_3_output.txt")


@check50.check(compiles)
def sum_20_22():
    """sum_20_22"""
    test_input_output("./sum", "sum_20_22_input.txt", "sum_20_22_output.txt")


@check50.check(compiles)
def sum_10_20():
    """sum_10_20"""
    test_input_output("./sum", "sum_10_20_input.txt", "sum_10_20_output.txt")


# Helpers
def test_input_output(executable, input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
