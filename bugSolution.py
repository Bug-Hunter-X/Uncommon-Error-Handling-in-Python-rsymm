def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return float('inf')  #or raise the exception
    except TypeError:
        print("Error: Type mismatch")
        return None  #or raise the exception
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example of an uncommon TypeError
result1 = function_with_uncommon_error(10, 0)  # ZeroDivisionError
result2 = function_with_uncommon_error(10, 'a') # TypeError
result3 = function_with_uncommon_error(10, 2)  # Normal case
result4 = function_with_uncommon_error(10, [1,2])

print(result1) # Output: inf
print(result2) # Output: None
print(result3) # Output: 5.0
print(result4) # Output: None