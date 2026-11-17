
"""
AST Visualizer Module.

This module converts an Abstract Syntax Tree (AST), represented
as nested Python dictionaries, into a graphical diagram using Graphviz.
"""

from pathlib import Path

from graphviz import Digraph


class ASTVisualizer:
    """Convert AST dictionaries into graphical tree diagrams."""

    def __init__(self, output_format="pdf"):
        """
        Initialize the AST visualizer.

        Args:
            output_format (str): Output format, either 'pdf' or 'png'.
        """
        if output_format not in ("pdf", "png"):
            raise ValueError("Output format must be 'pdf' or 'png'.")

        self.output_format = output_format
        self.graph = None
        self.node_count = 0

    def _create_label(self, ast_node):
        """
        Create a readable label for an AST node.

        The label includes the node type and its scalar properties.
        """
        node_type = ast_node.get("type", "UnknownNode")
        label_lines = [node_type]

        for key, value in ast_node.items():
            if key == "type":
                continue

            if not isinstance(value, (dict, list)):
                label_lines.append(f"{key}: {value}")

        return "\n".join(label_lines)

    def _add_node(self, ast_node, parent_id=None, edge_label=""):
        """
        Create a graph node and recursively process its children.

        Args:
            ast_node (dict): The current AST dictionary.
            parent_id (str): ID of the parent graph node.
            edge_label (str): Label for the connecting edge.

        Returns:
            str: ID of the created graph node.
        """
        if not isinstance(ast_node, dict):
            raise TypeError("AST nodes must be dictionaries.")

        node_id = f"node_{self.node_count}"
        self.node_count += 1

        # Create the current graph node.
        self.graph.node(
            node_id,
            label=self._create_label(ast_node)
        )

        # Connect the current node to its parent.
        if parent_id is not None:
            self.graph.edge(
                parent_id,
                node_id,
                label=edge_label
            )

        # Recursively process dictionary and list children.
        for key, value in ast_node.items():

            if isinstance(value, dict):
                self._add_node(
                    value,
                    parent_id=node_id,
                    edge_label=key
                )

            elif isinstance(value, list):
                self._process_list(
                    value,
                    parent_id=node_id,
                    edge_label=key
                )

        return node_id

    def _process_list(self, items, parent_id, edge_label):
        """
        Process lists containing dictionaries or nested lists.
        """
        for index, item in enumerate(items):
            current_label = f"{edge_label}[{index}]"

            if isinstance(item, dict):
                self._add_node(
                    item,
                    parent_id=parent_id,
                    edge_label=current_label
                )

            elif isinstance(item, list):
                self._process_list(
                    item,
                    parent_id=parent_id,
                    edge_label=current_label
                )

    def render(self, ast_dict, filename="ast_output"):
        """
        Render an AST dictionary into a PDF or PNG diagram.

        Args:
            ast_dict (dict): The AST dictionary to visualize.
            filename (str): Name of the output file.

        Returns:
            str: Path to the generated diagram.
        """
        if not isinstance(ast_dict, dict):
            raise TypeError("The AST must be a dictionary.")

        output_path = Path(filename)
        output_format = self.output_format

        # Allow users to specify the output extension.
        if output_path.suffix.lower() in (".pdf", ".png"):
            output_format = output_path.suffix.lower()[1:]
            output_path = output_path.with_suffix("")

        # Initialize the Graphviz directed graph.
        self.graph = Digraph(
            name="AST",
            format=output_format,
            graph_attr={
                "rankdir": "TB",
                "label": "Abstract Syntax Tree",
                "labelloc": "t"
            },
            node_attr={
                "shape": "box",
                "style": "rounded,filled",
                "fontname": "Arial",
                "fillcolor": "lightblue"
            },
            edge_attr={
                "fontname": "Arial"
            }
        )

        # Reset the node counter for each new diagram.
        self.node_count = 0

        # Build the complete AST graph.
        self._add_node(ast_dict)

        # Render and save the diagram.
        rendered_file = self.graph.render(
            filename=str(output_path),
            cleanup=True
        )

        return rendered_file
