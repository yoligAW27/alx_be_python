def safe_divide(numerator, denominator):
    try:
        num= float(numerator)
        den= float(denominator)

        result = num/den
        return f"result of the division is:{result}"
    except ZeroDivisionError:
        return f"error: cannot divide by zero."
    except ValueError:
        return"error: enter numeric value only." 
   
