load_file_in_context("script.py")

function_defined("lots_of_math")

given = lots_of_math(1, 2, 3, 4)
expected = 0

if given != expected:
  fail_tests("`lots_of_math(1, 2, 3, 4)` returned {given}, expected {expected}.".format(given=given, expected=expected))

given = lots_of_math(1, 1, 1, 1)
expected = 0

if given != expected:
  fail_tests("`lots_of_math(1, 1, 1, 1)` returned {given}, expected {expected}.".format(given=given, expected=expected))
  
pass_tests()
