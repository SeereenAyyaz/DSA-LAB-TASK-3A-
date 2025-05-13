def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        else: 
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right)) 
            else:
                return "Unsupported operator"

    return stack.pop() 

# Test cases
# Test Case 1
expression1 = "5 1 2 + 4 * + 3 -"
print("Expression 1 Result:", evaluate_postfix(expression1))  

# Test Case 2
expression2 = "2 3 1 * + 9 -"
print("Expression 2 Result:", evaluate_postfix(expression2))  

# Test Case 3
expression3 = "4 13 5 / +"
print("Expression 3 Result:", evaluate_postfix(expression3))  

# Test Case 4
expression4 = "6 2 / 3 - 4 2 * +"
print("Expression 4 Result:", evaluate_postfix(expression4))  

