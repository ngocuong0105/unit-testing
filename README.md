## Unit testing

Framework for automated testing. Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human.

**Definition** A unit test is a smaller test, one that checks that a single component operates in the right way.

### Notes
- name of test files and methods should follow the convention test_*
- best practices: tests should be isolated from each other. Running a  test should not depend on other tests.

unittest requires that:
- You put your tests into classes as methods
- You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement


### Commands
-run script
```
python -m unittest test_calc.py
```