# syntax_analyzer/exceptions.py

class SyntaxErrorException(Exception):
    """
    Custom exception raised when the parser encounters invalid syntax.
    """
    def __init__(self, expected: str, found: str, line_number: int = None):
        self.expected = expected
        self.found = found
        self.line_number = line_number
        super().__init__(self.__str__())

    def __str__(self) -> str:
        # If we know the line number, include it in the message
        if self.line_number is not None:
            return f"Syntax Error on line {self.line_number}: Expected '{self.expected}', but found '{self.found}'."
        else:
            # Otherwise, just print the expected and found tokens
            return f"Syntax Error: Expected '{self.expected}', but found '{self.found}'."