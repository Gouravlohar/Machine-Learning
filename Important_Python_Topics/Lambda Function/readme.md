
### Most Asked Interview Question: Lambda Function

A lambda function, also known as an anonymous function, is a small, single-line function that does not have a name. It is commonly used in Python for simple and concise operations.

### 1. What is a lambda function in Python?

A lambda function in Python is a small anonymous function defined using the `lambda` keyword. It can have any number of parameters but can only have one expression. Lambda functions are often used as inline functions.

### 2. How do you define a lambda function in Python?

You define a lambda function in Python using the `lambda` keyword followed by parameters, a colon, and an expression. For example:
   ```python
   lambda x: x * 2
   ```

### 3. What are the advantages of using lambda functions?

Lambda functions are concise and can be defined in a single line. They are useful for writing small, throwaway functions, especially in situations where a full function definition is unnecessary.

### 4. Can lambda functions have multiple expressions?

No, lambda functions in Python can only have a single expression.

### 5. How are lambda functions different from regular functions?

Lambda functions are anonymous and can only consist of a single expression. They are usually used for simple operations and are not named like regular functions defined using the `def` keyword.

### 6. In what situations are lambda functions commonly used?

Lambda functions are commonly used in scenarios where a short, simple function is needed, such as when working with higher-order functions like `map()`, `filter()`, and `sorted()`, or when passing a function as an argument to another function.

### 7. Can lambda functions access variables outside their scope?

Yes, lambda functions can access variables from the surrounding scope, similar to regular functions defined using the `def` keyword.

### 8. How do you sort a list of dictionaries by a specific key using a lambda function?

You can use the `sorted()` function with a lambda function as the `key` parameter. For example, to sort a list of dictionaries by the 'age' key:
   ```python
   sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
   ```

### 9. What is the difference between `map()` and a list comprehension?

`map()` applies a function to every item in an iterable and returns an iterator, while a list comprehension constructs a new list by evaluating an expression for each item in an iterable.

### 10. Can lambda functions be used recursively?

No, lambda functions cannot be used recursively because they cannot refer to themselves within their own definition.

