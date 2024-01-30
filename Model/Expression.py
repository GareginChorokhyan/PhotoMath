import re
import math
import sympy as sp

class Expression:
    def __init__(self):
        self.functions = None
        self.exp = "0"
        self.current_exp = ""
        self.add_function_mappings()

    def add_function_mappings(self):
        self.functions = {
            "sqrt": math.sqrt,
            "pow": pow,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "ctg": lambda x: 1 / math.tan(x),
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
            "ctgh": lambda x: 1 / math.tanh(x),
            "arcsin": math.asin,
            "arccos": math.acos,
            "arctan": math.atan,
            "arcctg": lambda x: math.pi / 2 - math.atan(x),
            "ln": math.log,
            "log": math.log10,
            "exp": math.exp,
            "logy": lambda x, y: math.log(y, x),
            "abs": abs,
            "ceil": math.ceil,
            "floor": math.floor,
            "round": round,
            "yroot": lambda x, y: sp.root(x, y),
            "mod": lambda x, y: x % y,
            "square": lambda x: x ** 2,
            "fact": math.factorial,
            "deg": math.degrees,
            "rad": math.radians,
        }

    def add_digit(self, digit: str):
        if self.exp == "0":
            self.exp = digit
        else:
            self.exp += digit
        return self.exp

    def clear(self):
        self.exp = "0"
        return self.exp

    def negate(self):
        if self.exp.startswith('-'):
            self.exp = self.exp[1:]
        else:
            self.exp = '-' + self.exp

        return self.exp

    def add_operations(self, operation: str):
        if operation == "%":
            self.add_percentage()
            return self.exp
        if self.exp == "0" and operation == "-":
            self.exp = operation
        if self.exp[-1].isdigit() or self.exp[-1] == ")":
            self.exp += operation
        elif operation == "-" and self.exp[-1] == "(":
            self.exp += operation
        return self.exp

    def add_math_operations(self, operation: str):
        mathematical_functions = list(self.functions.keys())
        basic_operations = ['+', '-', '*', '/']

        if self.exp == "0" and operation in mathematical_functions:
            self.exp = operation
            return self.exp

        if operation in mathematical_functions and (self.exp[-1] in basic_operations or self.exp[-1] == '(' or self.exp[-1] == ','):
            self.exp += operation
            return self.exp

        if operation == "%" and self.exp[-1].isdigit():
            self.exp += operation
            return self.exp

        return self.exp

    def sqrt_symbol(self):
        if self.exp == "0":
            self.exp = "√"
        else:
            self.exp += "√"
        return self.exp

    def add_open_parentheses(self):
        if self.exp == "0":
            self.exp = "("
        else:
            self.exp += "("
        return self.exp

    def add_close_parentheses(self):
        open_paren_count = self.exp.count('(')
        close_paren_count = self.exp.count(')')

        if open_paren_count > close_paren_count and self.exp[-1] not in ('(', '+', '-', '*', '/'):
            self.exp += ")"

        return self.exp

    def add_point(self):
        if self.exp[-1] not in ('(', ')', '+', '-', '*', '/'):
            if '.' not in self.exp:
                self.exp += '.'
        return self.exp

    def add_e(self):
        if self.exp == "0":
            self.exp = str(math.e)
        else:
            self.exp += str(math.e)
        return self.exp

    def add_pi(self):
        if self.exp == "0":
            self.exp = "3.14"
        else:
            self.exp += "3.14"
        return self.exp

    # def add_app(self):
    #     prev_function = self.exp.split("(")[0] if "(" in self.exp else ""
    #
    #     if prev_function in ["yroot", "logy", "mod"]:
    #         if len(self.exp) > 0 and self.exp[-1] != "(":
    #             self.exp += ","
    #     return self.exp

    def add_app(self):
        prev_function = self.exp.split("(")[0] if "(" in self.exp else ""
        if prev_function in ["yroot", "logy", "mod"]:
            self.exp += ","
        return self.exp

    def backspace_entry(self):
        if self.exp is None or len(self.exp) == 0:
            self.exp = "0"
        else:
            new_text = self.exp[:-1]
            self.exp = new_text if new_text else "0"

        return self.exp

    def add_percentage(self):
        try:
            print(self.exp)
            if self.exp[-1] in (')'):
                return self.exp
            self.exp += "%"
            if not self.exp:
                return None

            parts = re.findall(r'(\d+\.?\d*|\+|\-|\*|\/|\(|\)|%)', self.exp)
            idx = 0

            while idx < len(parts):
                if parts[idx] == '%':
                    percentage_idx = idx - 1

                    while parts[percentage_idx] == '':
                        percentage_idx -= 1

                    while parts[percentage_idx] == '':
                        percentage_idx -= 1

                    if parts[percentage_idx] == '-':
                        parts[percentage_idx] = ''
                        percentage_idx -= 1

                    result = float(parts[percentage_idx]) / 100
                    result = '{:.10g}'.format(result)
                    parts[percentage_idx] = str(result)
                    del parts[idx]

                idx += 1

            self.exp = ''.join(parts)
            return eval(self.exp) if self.exp else None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def calculate(self):
        try:
            exp_for_eval = self.exp

            # Add '*' between number and function or '('
            exp_for_eval = re.sub(r'(\d+)([a-z(√])', r'\1*\2', exp_for_eval)
            exp_for_eval = re.sub(r'([)a-z√])(\d+)', r'\1*\2', exp_for_eval)
            exp_for_eval = re.sub(r'(\d+)(\()', r'\1*\2', exp_for_eval)
            exp_for_eval = re.sub(r'(\))([a-z√(])', r'\1*\2', exp_for_eval)

            exp_for_eval = exp_for_eval.replace('√', 'sqrt')
            exp_for_eval = exp_for_eval.replace('^', '**')

            for func_name, func in self.functions.items():
                exp_for_eval = re.sub(r'\b' + func_name + r'\b', 'self.functions["' + func_name + '"]', exp_for_eval)

            result = eval(exp_for_eval)
            self.current_exp = self.exp

            if isinstance(result, int):
                self.exp = str(result)
            else:
                self.exp = '{:.10f}'.format(result).rstrip('0').rstrip('.') if '.' in str(result) else str(result)

            self.exp = self.exp.replace('**', '^')        
            return self.exp
        except Exception as e:
            print(f"Error: {e}")
            return None



