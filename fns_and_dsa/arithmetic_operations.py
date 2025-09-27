def perform_operation(num1, num2, operation):   

    if "add" == operation:
        result = num1 + num2
        return result
                
    elif "subtract" == operation:
        result = num1 - num2
        return result
        
    elif "multiply" == operation:
        result = num1 * num2
        return result
        
    elif "divide" == operation:
        if num2 == 0:
            return f"Cannot divide by zero."
        else:
            result = num1 / num2
            return result
                
    else:
        return f"Unknown operation"
    
    # match operation:
    #     case "add":
    #         result = num1 + num2
    #         return result
                  
    #     case "subtract":
    #         result = num1 - num2
    #         return result
            
    #     case "multiply":
    #         result = num1 * num2
    #         return result
            
    #     case "divide":
    #         if num2 == 0:
    #             return f"Cannot divide by zero."
    #         else:
    #             result = num1 / num2
    #             return result
                
    #     case _:
    #         return f"Unknown operation"
     
            