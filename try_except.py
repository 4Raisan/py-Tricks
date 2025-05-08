# For Specific Errors / processes must be under the [ try: & except (): ] sections 
try:
    num = 100 / 4
    print("Answer is :::", num)
except (ValueError, TypeError):    # Errors must be case sensitive
    print("Error: Invalid input!")



