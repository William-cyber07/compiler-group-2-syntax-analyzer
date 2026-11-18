from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

"""
Test script for the AST Visualizer.
"""

from syntax_analyzer import visualizer
from syntax_analyzer import ast_builder as ast


# Create a NumberLiteral node representing 5.
num = ast.create_number_node(5)

# Create an Assignment node representing x = 5.
assign = ast.create_assignment_node("x", num)

# Create the complete Program node.
program = ast.create_program_node([assign])

# Initialize the AST Visualizer.
viz = visualizer.ASTVisualizer()

# Generate the AST diagram.
output_file = viz.render(program, "my_first_tree")

print("AST visualization generated successfully!")
print(f"Output file: {output_file}")


# Test a binary expression: x = 5 + y

left = ast.create_number_node(5)
right = ast.create_identifier_node("y")

expression = ast.create_binary_op_node(
    left,
    "+",
    right
)

assignment = ast.create_assignment_node(
    "x",
    expression
)

program = ast.create_program_node([assignment])

# Generate the binary expression diagram.
viz.render(program, "binary_expression")

print("Binary expression visualization generated successfully!")


# Test a print statement: print(x + 5)

identifier = ast.create_identifier_node("x")
number = ast.create_number_node(5)

expression = ast.create_binary_op_node(
    identifier,
    "+",
    number
)

print_node = ast.create_print_node(expression)

program = ast.create_program_node([print_node])

# Generate the print statement diagram.
viz.render(program, "print_statement")

print("Print statement visualization generated successfully!")


# Test PNG output format.
png_viz = visualizer.ASTVisualizer(output_format="png")

png_file = png_viz.render(
    program,
    "print_statement_png"
)

print("PNG visualization generated successfully!")
print(f"PNG file: {png_file}")