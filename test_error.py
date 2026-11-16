from syntax_analyzer.exceptions import SyntaxErrorException

print("--- Testing Error Formatting ---")

# Let's pretend the parser expected an '=' sign but found a ';' on line 3
try:
    raise SyntaxErrorException(expected="=", found=";", line_number=3)
except SyntaxErrorException as e:
    print(f"CAUGHT ERROR: {e}")

# Let's test one without a line number
try:
    raise SyntaxErrorException(expected="NUMBER", found="EOF")
except SyntaxErrorException as e:
    print(f"CAUGHT ERROR: {e}")