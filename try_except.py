# For Specific Errors / processes must be under the [ try: & except (): ] sections 
try:
    num = 100 / 4
    print("Answer is :::", num)
except (ValueError, TypeError):    # Errors must be case sensitive
    print("Error: Invalid input!")


# For ALL Errors / processes must be under the [ try: & except (): ] sections 
try:
    num = 100 / a
    print("Answer is :::", num)
except Exception as e:   # Unexpected error: ZeroDivisionError: division by zero
    print(f"Unexpected error: {type(e).__name__}: {e}")

'''
except Exception:    # Unexpected error: type: <class 'Exception'>
    print(f"Unexpected error: {type(Exception).__name__}: {Exception}")
'''
