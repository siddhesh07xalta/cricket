def validate_input(prompt, data_type, min_value=None, max_value=None, allowed_values=None):

    while True:
        try:
            user_input = input(prompt)
            
            if data_type is int:
                user_input = int(user_input)
            elif data_type is float:
                user_input = float(user_input)
            elif data_type is str:
                if user_input.isalpha():
                    user_input = str(user_input).strip()
                else:
                    raise ValueError

            if min_value is not None and user_input < min_value:
                print(f"Input must be greater than or equal to {min_value}.")
                continue
            if max_value is not None and user_input > max_value:
                print(f"Input must be less than or equal to {max_value}.")
                continue
            if allowed_values is not None and user_input not in allowed_values:
                print(f"Input must be one of: {allowed_values}.")
                continue

            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a value of type {data_type.__name__}.")
        except Exception as e:
             print(f"An unexpected error occurred while taking input: {e}")
