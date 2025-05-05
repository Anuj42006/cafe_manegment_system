def validate_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def format_currency(amount):
    return f"${amount:.2f}"

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')