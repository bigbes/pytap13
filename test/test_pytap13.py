import unittest

import sys
import os
sys.path.append(os.path.realpath(os.path.join(os.path.split(__file__)[0], '../')))
import pytap13

test_data = """TAP version 13
1..2
ok 1 Input file opened
not ok 2 First line of the input valid
"""

class TAP13Test(unittest.TestCase):

    def test_simple(self):
        test_data = """
            TAP version 13
            1..3
            ok 1 Input file opened
            not ok 2 First line invalid
            ok Third result
          """
        t = pytap13.TAP13()
        t.parse(test_data)

        self.assertEqual(len(t.tests), t.tests_planned)

        self.assertEqual(t.tests_planned, 3)
        self.assertEqual(len(t.tests), 3)

        tx = t.tests[0]
        self.assertEqual(tx.result, 'ok')
        self.assertEqual(tx.description, 'Input file opened')
        self.assertEqual(tx.directive, None)
        self.assertEqual(tx.comment, None)
        self.assertEqual(tx.yaml, None)

        tx = t.tests[1]
        self.assertEqual(tx.result, 'not ok')
        self.assertEqual(tx.description, 'First line invalid')

        tx = t.tests[2]
        self.assertEqual(tx.id, 3)
        self.assertEqual(tx.description, 'Third result')


    def test_yaml(self):
        test_data = """
            TAP version 13
            1..1
            not ok First line of the input valid
                ---
                message: 'First line invalid'
                data:
                    got:
                        - 1
                        - 2
                    expect:
                        - 2
                        - 2
                ...
          """
        t = pytap13.TAP13()
        t.parse(test_data)

        yaml_data = {"message": "First line invalid",
                "data": {
                        "got": [1,2],
                        "expect": [2,2]
                        }
                }
        self.assertEqual(t.tests[0].yaml, yaml_data)


if __name__ == "__main__":
    unittest.main()
