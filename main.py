import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from operations.advanced import nth_root, square, square_root, percentage, exponentiate, log_base, log10, ln
from operations.history import HistoryManager

class CalculatorLayout(BoxLayout):
    history_data = StringProperty("")  # Kivy property for history data

    """
    Main calculator layout and logic.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history_manager = HistoryManager()
        self.exponent_mode = False
        self.exponent_base = ""
        self.history_data = ""  # Initialize history data

    def calc_symbol(self, symbol):
        """Append a symbol to the calculator field."""
        self.ids.calc_field.text += symbol

    def backspace(self):
        """Remove the last character from the calculator field."""
        self.ids.calc_field.text = self.ids.calc_field.text[:-1]

    def get_result(self):
        """
        Evaluate the current expression and update the result.
        Handles exponentiation mode and normal evaluation.
        """
        expression = self.ids.calc_field.text

        # Exponentiation mode
        if self.exponent_mode and "^" in expression:
            try:
                base, exponent = expression.split("^")
                result = exponentiate(base, exponent)
                self.ids.calc_field.text = result
                self.history_manager.add_entry(f"{base}^{exponent} = {result}")
            except Exception:
                self.ids.calc_field.text = "Error"
            finally:
                self.exponent_mode = False
                self.exponent_base = ""
                self.update_history_display()
                return

        # Fallback: normal evaluation (should use safe eval in production)
        try:
            # Consider using a safe eval or parser here
            result = str(eval(expression))
            self.ids.calc_field.text = result
            self.history_manager.add_entry(f"{expression} = {result}")
        except Exception:
            self.ids.calc_field.text = "Error"
        self.update_history_display()

    def square(self):
        """Find the square of the number."""
        value = self.ids.calc_field.text
        result = square(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"{value}² = {result}")
        self.update_history_display()

    def square_root(self):
        """Find square root of a number."""
        value = self.ids.calc_field.text
        result = square_root(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"√{value} = {result}")
        self.update_history_display()

    def percentage(self):
        """Calculate percentage of a number."""
        value = self.ids.calc_field.text
        result = percentage(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"{value}% = {result}")
        self.update_history_display()

    def clear(self):
        """Clear the calculator field."""
        self.ids.calc_field.text = ""

    def update_history_display(self):
        """Update the history display."""
        self.history_data = self.history_manager.get_history()
        # Optionally, also update the label directly if needed:
        # self.ids.history_label.text = self.history_data

    def power(self):
        """Prepare for exponent input."""
        self.exponent_base = self.ids.calc_field.text
        if not self.exponent_base:
            self.ids.calc_field.text = "Enter base first"
            return
        self.exponent_mode = True
        self.ids.calc_field.text += "^"

    def calculate_log10(self):
        """Calculate log base 10."""
        value = self.ids.calc_field.text
        result = log10(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"log10({value}) = {result}")
        self.update_history_display()

    def calculate_ln(self):
        """Calculate natural logarithm."""
        value = self.ids.calc_field.text
        result = ln(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"ln({value}) = {result}")
        self.update_history_display()

    def calculate_log_base(self, base):
        """Calculate logarithm with a custom base."""
        value = self.ids.calc_field.text
        result = log_base(value, base)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"log base {base} ({value}) = {result}")
        self.update_history_display()

    def calculate_factorial(self):
        """Calculate factorial of a number."""
        try:
            value = self.ids.calc_field.text
            number = int(float(value))
            if number < 0:
                self.ids.calc_field.text = "Error: Negative!"
            else:
                result = math.factorial(number)
                self.ids.calc_field.text = str(result)
                self.history_manager.add_entry(f"{number}! = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        except OverflowError:
            self.ids.calc_field.text = "Error: Too Large"
        self.update_history_display()

    def calculate_nth_root(self):
        """Calculate the nth root of a number (format: nⁿ√x)."""
        expression = self.ids.calc_field.text
        if 'ⁿ√' in expression:
            try:
                num, value = [part.strip() for part in expression.split('ⁿ√')]
                result = nth_root(num, value)
                self.ids.calc_field.text = str(result)
                self.history_manager.add_entry(f"{num}ⁿ√{value} = {result}")
            except Exception as e:
                self.ids.calc_field.text = f"Error: {str(e)}"
        else:
            self.ids.calc_field.text = "Error: Use format nⁿ√x"
        self.update_history_display()

    def calculate_sin(self):
        """Calculate sine of the input (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            result = math.sin(math.radians(value))
            self.ids.calc_field.text = str(result)
            self.history_manager.add_entry(f"sin({value}) = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_cos(self):
        """Calculate cosine of the input (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            result = math.cos(math.radians(value))
            self.ids.calc_field.text = str(result)
            self.history_manager.add_entry(f"cos({value}) = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_tan(self):
        """Calculate tangent of the input (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            result = math.tan(math.radians(value))
            self.ids.calc_field.text = str(result)
            self.history_manager.add_entry(f"tan({value}) = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_asin(self):
        """Calculate arcsine (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            if -1 <= value <= 1:
                result = math.degrees(math.asin(value))
                self.ids.calc_field.text = str(result)
                self.history_manager.add_entry(f"asin({value}) = {result}")
            else:
                self.ids.calc_field.text = "Error: Out of domain"
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_acos(self):
        """Calculate arccosine (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            if -1 <= value <= 1:
                result = math.degrees(math.acos(value))
                self.ids.calc_field.text = str(result)
                self.history_manager.add_entry(f"acos({value}) = {result}")
            else:
                self.ids.calc_field.text = "Error: Out of domain"
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_atan(self):
        """Calculate arctangent (degrees)."""
        try:
            value = float(self.ids.calc_field.text)
            result = math.degrees(math.atan(value))
            self.ids.calc_field.text = str(result)
            self.history_manager.add_entry(f"atan({value}) = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_inverse(self):
        """Calculate the multiplicative inverse."""
        try:
            value = float(self.ids.calc_field.text)
            if value == 0:
                self.ids.calc_field.text = "Error: Division by 0"
            else:
                result = 1 / value
                self.ids.calc_field.text = str(result)
                self.history_manager.add_entry(f"1/({value}) = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error: Invalid Input"
        self.update_history_display()

    def calculate_abs(self):
        """Calculate the absolute value."""
        try:
            value = float(self.ids.calc_field.text)
            result = abs(value)
            self.ids.calc_field.text = str(result)
            self.history_manager.add_entry(f"|{value}| = {result}")
        except ValueError:
            self.ids.calc_field.text = "Error"
        self.update_history_display()

class FocusCalc(App):
    """Main App class."""
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    MyCalculator = FocusCalc()
    MyCalculator.run()
