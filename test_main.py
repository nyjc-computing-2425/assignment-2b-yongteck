import sys
import unittest

# autograding submodule might not be successfully pulled on init
# if unsuccessful, we have to pull it manually
# limit number of retries
MAX_RETRIES = 5
retries = 0
while "autograding" not in sys.modules:
    try:
        import autograding
        from autograding.case import FuncCall, InOut
    except ImportError:
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
        retries += 1
    if retries >= MAX_RETRIES:
        sys.exit("[import autograding] Too many retries, exiting")


class TestSF(autograding.TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="2.345", output="The number 2.345 has 3 decimal placess."),
            InOut(input="02.345", output="The number 02.345 has 3 decimal places."),
            InOut(input="0.0023", output="The number 0.0023 has 4 decimal places."),
            InOut(input="2.3400", output="The number 2.3400 has 4 decimal places."),
        ]


if __name__ == '__main__':
    unittest.main()
