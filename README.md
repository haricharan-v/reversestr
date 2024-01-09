# Reverse String

This Python script provides a simple function, `reverseString`, to reverse a list of strings. The user is prompted to enter a string as an array, and the program reverses the characters in the array using the `reverseString` function. The reversed string is then displayed, and the user has the option to try again.

## How to Use

1. Run the script in a Python environment.
2. Enter a string when prompted.
3. The script will reverse the characters in the string and display the result.
4. Optionally, choose to try again by entering 'yes' when prompted.

## Code Explanation

The main functionality of the code is contained in the `reverseString` function, which takes a list of strings as input and modifies it in place to reverse the order of its elements.

The `try_again` function is used to check whether the user wants to input another string. If the user enters 'yes,' the program continues to prompt for input; otherwise, it terminates.

The main loop (`while True`) allows the user to interact with the script continuously until they choose to exit.

## Example

```
Enter a string as an array (e.g., 'abcde'): hello
Reversed string: olleh
Do you want to try again? (yes/no): yes
Enter a string as an array (e.g., 'abcde'): python
Reversed string: nohtyp
Do you want to try again? (yes/no): no
```

Feel free to use and modify this code as needed.
