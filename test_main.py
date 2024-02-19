import contextlib
import subprocess
import sys
import unittest

# limit number of retries
MAX_RETRIES = 5
retries = 0

# Force reload of autograding submodule
# This allows it to be updated even after students have accepted an assignment
# It would otherwise require them to delete and re-accept the assignment
# (or alternatively update the submodule manually)
def unload():
    global autograding
    if "autograding" in sys.modules:
        del sys.modules["autograding"]
    with contextlib.suppress(NameError):
        del autograding

unload()
subprocess.run(["git", "submodule", "update", "--init", "--remote"])
import autograding
from autograding.case import FuncCall, InOut


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
