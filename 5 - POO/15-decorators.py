from decorator import my_decorator, uppercase_decorator, split_string

# Example 1 

@my_decorator
def my_function():
    print('Dentro da function')

my_function()

#Example 2
@uppercase_decorator
def text():
    return "Hello World"


print(text())


#Example 3
@split_string
@uppercase_decorator
def example():
    return "Aprendendo python e criando decorators"


print(example())