# Execute All Test Case
 - $ pytest

# Execute with all verbose arguments {-v}
 - $ pytest -v

# Execute with all console output arguments
  - $ pytest -s
  - $ pytest -v -s # Execute both arguments in single command line

# Execute with Specific Test File
    -$ pytest <path>/test_testCase_001.py -v -s # Execute Specific Test File
#Maintain State & Run Failed first Approach
  - #pytest -q --ff (Failed first) Failed first after others 
  - #pytest -q --lf (last Failed) only Failed others are diselected
  - #pytest --cache-show  (Show Caches while running tests)
  - pytest --cache-clear

  - The -q/--quiet flag keeps the output brief in this and following examples.
  -  pytest src/test/  # Run Specific Directory
  -  pytest -k 001  # Run Test Contains Specific Phraases here like its Execute all Contain 001 in his method name

[Autopep8 packages installation]
  - install via pip -> pip install --upgrade autopep8
  - Apply pep8 format via cli -> autopep8 --in-place --aggressive --aggressive src/**/*.py
  - autopep8 depends on pycodestyle package


[Pytest Fixture]
  -  Test functions request fixtures they require by declaring them as arguments.
  - Fixtures can be requested more than once per test (return values are cached)
  - Autouse fixtures (fixtures you don’t have to request) Sometimes you may want to have a fixture (or even several) that you know all your tests will depend on. “Autouse” fixtures are a convenient way to make all tests automatically request them. This can cut out a lot of redundant requests, and can even provide more advanced fixture usage (more on that further down).We can make a fixture an autouse fixture by passing in autouse=True to the fixture’s decorator. Here’s a simple example for how they can be used:
 - Sometimes you may want to have a fixture (or even several) that you know all your tests will depend on. “Autouse” fixtures are a convenient way to make all tests automatically request them. This can cut out a lot of redundant requests, and can even provide more advanced fixture usage (more on that further down).

[Fixture Scope] 
- function: the default scope, the fixture is destroyed at the end of the test.
- class: the fixture is destroyed during teardown of the last test in the class.
- module: the fixture is destroyed during teardown of the last test in the module.
- package: the fixture is destroyed during teardown of the last test in the package.
- session: the fixture is destroyed at the end of the test session.

[Teardown/Cleanup (AKA Fixture finalization)]

- “Yield” fixtures yield instead of return. With these fixtures, we can run some code and pass an object back to the requesting fixture/test, just like with the other fixtures. The only differences are:
- Refer file tests/test_teardown_finalization.py

[How to mark test functions with attributes]
- Check Pytest Markers -> pytest --markers

  [Next]: https://docs.pytest.org/en/7.1.x/how-to/parametrize.html