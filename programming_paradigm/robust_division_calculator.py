def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for division by zero and non-numeric inputs.
    
    Args:
        numerator: The numerator as string or numeric
        denominator: The denominator as string or numeric
    
    Returns:
        str: Result message or error message
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."