def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# Example of an uncommon TypeError
result1 = function_with_uncommon_error(10, 0)  # ZeroDivisionError
result2 = function_with_uncommon_error(10, 'a') # TypeError
result3 = function_with_uncommon_error(10, 2)  # Normal case

print(result1) # Output: inf
print(result2) # Output: None
print(result3) # Output: 5.0