
import check50
import check50.c

@check50.check()
def exists():
    """oddupton.c exists"""
    check50.exists("oddupton.c")
    check50.include("test_1_input.txt", "test_1_output.txt")
    check50.include("test_2_input.txt", "test_2_output.txt")
    check50.include("test_3_input.txt", "test_3_output.txt")

@check50.check(exists)
def compiles():
    """oddupton.c compiles"""
    check50.c.compile("oddupton.c", lcs50=True)


@check50.check(compiles)
def test_1():
    """test_1"""
    test_input_output("./oddupton", "test_1_input.txt", "test_1_output.txt")


@check50.check(compiles)
def test_2():
    """test_2"""
    test_input_output("./oddupton", "test_2_input.txt", "test_2_output.txt")


@check50.check(compiles)
def test_3():
    """test_3"""
    test_input_output("./oddupton", "test_3_input.txt", "test_3_output.txt")


# Helpers
def test_input_output(executable, input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
