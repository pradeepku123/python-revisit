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


  [Next]: https://docs.pytest.org/en/7.1.x/how-to/fixtures.html