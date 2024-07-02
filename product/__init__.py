
import check50
import check50.c

@check50.check()
def exists():
    """product.c exists"""
    check50.exists("product.c")
    check50.include("product_2_3_4_input.txt", "product_2_3_4_output.txt")
    check50.include("product_10_20_30_input.txt", "product_10_20_30_output.txt")

@check50.check(exists)
def compiles():
    """product.c compiles"""
    check50.c.compile("product.c", lcs50=False)


@check50.check(compiles)
def product_2_3_4():
    """product_2_3_4"""
    test_input_output("./product", "product_2_3_4_input.txt", "product_2_3_4_output.txt")


@check50.check(compiles)
def product_10_20_30():
    """product_10_20_30"""
    test_input_output("./product", "product_10_20_30_input.txt", "product_10_20_30_output.txt")


# Helpers
def test_input_output(executable, input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
