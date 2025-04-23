import ast

class SafeExpressionChecker(ast.NodeVisitor):
    def visit_Constant(self, node):
        # Allow numbers
        pass
    

    def visit_BinOp(self, node):
        # Allow binary operations
        if not isinstance(node.op(ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)):
            raise ValueError("Unsupported operator")
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        # Allow unary operations
        self.visit(node.operand)

    def visit_Tuple(self, node):
        # Allow tuples if needed
        for elem in node.elts:
            self.visit(elem)

    def visit_List(self, node):
        # Allow lists if needed
        for elem in node.elts:
            self.visit(elem)

    def visit_Call(self, node):
        # Function calls are not allowed
        raise ValueError("Function calls are not allowed")

    def visit_Name(self, node):
        # Variable names are not allowed
        raise ValueError("Variable names are not allowed")

    # And so on for other node types that are not allowed

def is_safe_expression(expression):
    try:
        tree = ast.parse(expression, mode='eval')
        checker = SafeExpressionChecker()
        checker.visit(tree)
        return True
    except (SyntaxError, ValueError):
        return False

def evaluate_expression(expression):
    """Evaluate mathematical expression after validating it's safe"""
    if not is_safe_expression:
        return "Error: Invalid expression"
    try:
        return str(eval(expression))
    except ZeroDivisionError:
        return "Error: Division by 0"
    except Exception as e:
        return f"Error: {str(e)}"