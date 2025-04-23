from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from operations.arithmetic import evaluate_expression
from operations.advanced import square, square_root, percentage
from operations.history import History_Manager
from operations.advanced import square_root, percentage 
from operations.advanced import exponentiate, log_base, log10, ln
from operations.history import History_Manager

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import kivy


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history_manager = History_Manager()
        self.exponent_mode = False
        self.base_value = ""
     

    def calc_symbol(self, symbol):
        self.ids.calc_field.text += symbol
    
    def backspace(self):
        """Clear the screen"""
        self.ids.calc_field.text = self.ids.calc_field.text[:-1]

    def get_result(self):
        """Get result of an operation"""
        expression = self.ids.calc_field.text

        # Check exponentiation mode
        if self.exponent_mode and "^" in expression:
            try:
                base, exponent = expression.split("^")
                result = exponentiate(base, exponent)
                self.ids.calc_field.text = result
                self.history_manager.add_entry(f"{base}^{exponent} = {result}")
            except Exception as e:
                self.ids.calc_field.text = "Error"
            finally:
                self.exponent_mode = False
                self.exponent_base = ""
                self.update_history_display()
                return
            
        # Fallback: normal evaluation
        try:
            result = str(eval(expression))
            self.ids.calc_field.text = result
            self.history_manager.add_entry(f"{expression} = {result}")
        except Exception:
            self.ids.calc_field.text = "Error"
        self.update_history_display()


    def square(self):
        """Find the square of the number"""
        self.ids.calc_field.text = square(self.ids.calc_field.text)
        self.history_manager.add_entry(f"{self.ids.calc_field.text}2")

    def square_root(self):
        """Find square root of a number"""
        self.ids.calc_field.text = square_root(self.ids.calc_field.text)
        self.history_manager.add_entry(f"√{self.ids.calc_field.text}")

    def percentage(self):
        """Calculate percentage of a number"""
        self.ids.calc_field.text = percentage(self.ids.calc_field.text)
        self.history_manager.add_entry(f"{self.ids.calc_field.text}%")

    def clear(self):
        """Clear the screen"""
        self.ids.calc_field.text = ""
    
    def update_history_display(self):
        """Update user data to history list"""
        self.history_data = self.history_manager.get_history()

    def power(self):
        """Find the power / exponent of a number"""
        self.exponent_base = self.ids.calc_field.text
        if not self.exponent_base:
            self.ids.calc_field.text = "Enter base first"
            return
        self.exponent_mode = True
        self.ids.calc_field.text += "^"
    
    def calculate_log(self):
        """Find the logarith at base 10"""
        value = self.ids.calc_field.text
        result = log10(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"log10({value}) = {result}")
        self.update_history_display()
    

    def calculate_ln(self):
        """Find natural log"""
        value = self.ids.calc_field.text
        result = ln(value)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"ln({value}) = {result}")
        self.update_history_display()
    

    def calculate_log_base(self, base):
        value = self.ids.calc_field.text
        result = log_base(value, base)
        self.ids.calc_field.text = result
        self.history_manager.add_entry(f"log base {base} ({value}) = {result}")
        self.update_history_display()


class FocusCalc(App):
    def build(self):
        return CalculatorLayout()
    
if __name__ == '__main__':
    MyCalculator = FocusCalc()
    MyCalculator.run()
