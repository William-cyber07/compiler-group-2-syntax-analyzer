# syntax_analyzer/ast_builder.py

"""
AST Builder Module.
This module contains pure functions to construct nodes for the Abstract Syntax Tree (AST).
The AST is represented as nested Python dictionaries.
"""

def create_program_node(statements: list) -> dict:
    """
    Creates the root node of the AST.
    :param statements: A list of statement nodes.
    """
    return {
        "type": "Program",
        "body": statements
    }

def create_assignment_node(variable_name: str, value_node: dict) -> dict:
    """
    Creates a node for variable assignment (e.g., x = 5).
    """
    return {
        "type": "Assignment",
        "variable": variable_name,
        "value": value_node
    }

def create_print_node(expression_node: dict) -> dict:
    """
    Creates a node for a print statement (e.g., print(x)).
    """
    return {
        "type": "PrintStatement",
        "value": expression_node
    }

def create_binary_op_node(left_node: dict, operator: str, right_node: dict) -> dict:
    """
    Creates a node for mathematical operations (e.g., 5 + y).
    """
    return {
        "type": "BinaryOp",
        "operator": operator,
        "left": left_node,
        "right": right_node
    }

def create_number_node(value: int) -> dict:
    """
    Creates a node for a number literal (e.g., 5).
    """
    return {
        "type": "NumberLiteral",
        "value": value
    }

def create_identifier_node(name: str) -> dict:
    """
    Creates a node for a variable identifier (e.g., x).
    """
    return {
        "type": "Identifier",
        "name": name
    }