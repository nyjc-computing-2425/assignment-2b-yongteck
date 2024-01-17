import subprocess
import unittest


def strip_prompt(stdout: str) -> str:
    """Strip the prompt from stdout.
    The prompt is assumed to end with a colon (:), followed by zero or more
    whitespace characters.
    """
    if stdout.strip():
        stdout = stdout[stdout.find(':') + 1:].lstrip()
    return stdout


def invoke_main(input_: str) -> str:
    """Invoke main.py and return its output."""
    proc = subprocess.Popen(["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True)
    try:
        stdout, stderr = proc.communicate(input=input_, timeout=1)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    finally:
        # Strip prompt from stdout; use colon to detect
        if stdout.strip():
            stdout = stdout[stdout.find(':') + 1:].lstrip()
        return stdout


class TestInputOutput(unittest.TestCase):

    def test_part1(self):
        testcase = "2.345\n"
        testans = "The number 2.345 has 3 decimal places.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part2(self):
        testcase = "02.345\n"
        testans = "The number 02.345 has 3 decimal places.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part3(self):
        testcase = "0.0023\n"
        testans = "The number 0.0023 has 4 decimal places.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part4(self):
        testcase = "2.3400\n"
        testans = "The number 2.345 has 4 decimal places.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")


if __name__ == '__main__':
    unittest.main()
