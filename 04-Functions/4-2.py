A function is defined using the def keyword, followed by the function name, parentheses, and a colon. Inside the parentheses, you can specify parameters that the function can accept. The function's code block is indented.

def function_name(parameters):
    # Code block (function body)
    return result  # Optional: Returns a value
Components of a Function:

def: Keyword used to define a function.
function_name: The name of the function. It should be descriptive of the task the function performs.
parameters: Optional inputs that the function accepts. They are defined inside the parentheses.
Function Body: Code block that contains the logic of the function. This code is executed whenever the function is called.
return: Optional statement that specifies the value to be returned by the function.
Take a look at the function below that allows you to sum two numbers. The add function takes two parameters, a and b, and returns their sum. The returned value is stored in the variable sum_value and then printed.

def add(a, b):
    result = a + b
    return result

sum_value = add(5, 3)
print(sum_value)  # Output: 8