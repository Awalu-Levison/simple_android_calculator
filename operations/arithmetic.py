import ast

class SafeExpressionChecker(ast.NodeVisitor):
    """
    AST NodeVisitor to ensure only safe arithmetic expressions are allowed.
    """
    def visit_Constant(self, node):
        # Allow only numeric constants
        if not isinstance(node.value, (int, float)):
            raise ValueError("Only numeric constants are allowed.")


    def visit_BinOp(self, node):
        # Allow only safe binary operations
        if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)):
            raise ValueError("Unsupported operator")
        self.visit(node.left)
        self.visit(node.right)


    def visit_UnaryOp(self, node):
        # Allow unary operations (+, -)
        if not isinstance(node.op, (ast.UAdd, ast.USub)):
            raise ValueError("Unsupported unary operator")
        self.visit(node.operand)


    def visit_Tuple(self, node):
        for elem in node.elts:
            self.visit(elem)


    def visit_List(self, node):
        for elem in node.elts:
            self.visit(elem)
            

    def visit_Call(self, node):
        raise ValueError("Function calls are not allowed")

    def visit_Name(self, node):
        raise ValueError("Variable names are not allowed")

    # Add other visit_ methods as needed for unsupported nodes

def is_safe_expression(expression):
    """
    Checks if the given expression is safe for evaluation.
    Returns True if safe, False otherwise.
    """
    try:
        tree = ast.parse(expression, mode='eval')
        checker = SafeExpressionChecker()
        checker.visit(tree)
        return True
    except (SyntaxError, ValueError):
        return False

class Calculator:
    """
    Calculator class with safe expression evaluation.
    """
    def nth_root(self, n, x):
        """
        Calculates the nth root of x.
        """
        try:
            n = float(n)
            x = float(x)
            if n == 0:
                raise ValueError("Root degree cannot be zero.")
            if x < 0 and int(n) % 2 == 0:
                raise ValueError("Cannot compute even root of a negative number.")
            return x ** (1.0 / n)
        except Exception as e:
            raise ValueError(f"Invalid nth root input: {e}")

    def evaluate_expression(self, expression):
        """
        Evaluates the given expression safely.
        Handles nth root and normal arithmetic expressions.
        """
        # Handle nth root first
        if 'ⁿ√' in expression:
            try:
                n, x = expression.split('ⁿ√')
                n = n.strip()
                x = x.strip()
                result = self.nth_root(n, x)
                return str(result)
            except Exception as e:
                return f"Error: {str(e)}"

        # Otherwise, normal evaluation
        if not is_safe_expression(expression):
            return "Error: Unsafe or invalid expression"
        try:
            tree = ast.parse(expression, mode='eval')
            result = eval(compile(tree, filename="", mode="eval"))
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
