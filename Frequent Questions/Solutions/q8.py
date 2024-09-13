def q8(brackets: str) -> bool:
    balance_counter = 0
    for char in brackets:
        if char == '(':
            balance_counter += 1
        elif char == ')':
            balance_counter -= 1
        
        if balance_counter < 0:
            return False
    
    return balance_counter == 0    