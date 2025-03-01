class Solution:
    def decodedString(self, s: str) -> str:
        stack = []  # Stack to keep track of characters and numbers
        current_num = 0  # Variable to store the current number
        current_str = ""  # Variable to store the current string
        
        for char in s:
            if char.isdigit():
                # If it's a digit, update the current number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number to stack and reset them
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == ']':
                # Pop from the stack and repeat the string accordingly
                last_str, num = stack.pop()
                current_str = last_str + num * current_str
            else:
                # Append character to the current string
                current_str += char
        
        return current_str
