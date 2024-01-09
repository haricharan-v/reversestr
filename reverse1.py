from typing import List


def reverseString(s: List[str]) -> None:
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        # Swap the left char and right char
        s[left_index], s[right_index] = s[right_index], s[left_index]
        left_index += 1
        right_index -= 1


def try_again():
    return input("Do you want to try again? (yes/no): ").lower() == 'yes'


while True:
    user_input = input("Enter a string as an array (e.g., 'abcde'): ")
    input_array = list(user_input)

    reverseString(input_array)

    print("Reversed string:", ''.join(input_array))

    if not try_again():
        break
