# # # # # # my_list = [1, 2, 3, 4, 5]

# # # # # # for i in range(len(my_list)//2):
# # # # # #     my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]

# # # # # # print(my_list)  # Output: [5, 4, 3, 2, 1]

# # # # # def romantoint(roman_num):
# # # # #     roman_dict = {
# # # # #         'I': 1,
# # # # #         'V': 5,
# # # # #         'X': 10,
# # # # #         'L': 50,
# # # # #         'C': 100,
# # # # #         'D': 500,
# # # # #         'M': 1000
# # # # #     }
# # # # #     total = 0
# # # # #     prev_value = 0

# # # # #     for char in reversed(roman_num):
# # # # #         value = roman_dict[char]
# # # # #         if value < prev_value:
# # # # #             total -= value
# # # # #         else:
# # # # #             total += value
# # # # #         prev_value = value

# # # # #     return total


# # # # # def letterCombinations(digits):
# # # # #     if not digits:
# # # # #         return []

# # # # #     digit_to_letters = {
# # # # #         '2': 'abc',
# # # # #         '3': 'def',
# # # # #         '4': 'ghi',
# # # # #         '5': 'jkl',
# # # # #         '6': 'mno',
# # # # #         '7': 'pqrs',
# # # # #         '8': 'tuv',
# # # # #         '9': 'wxyz'
# # # # #     }

# # # # #     def backtrack(index, path):
# # # # #         if index == len(digits):
# # # # #             combinations.append("".join(path))
# # # # #             return
# # # # #         possible_letters = digit_to_letters[digits[index]]
# # # # #         for letter in possible_letters:
# # # # #             path.append(letter)
# # # # #             backtrack(index + 1, path)
# # # # #             path.pop()

# # # # #     combinations = []
# # # # #     backtrack(0, [])
# # # # #     return combinations

# # # # # def isPalindrome(x):
# # # # #         my_x = str(x)
# # # # #         reversed_x = "".join(reversed(my_x))
# # # # #         for i in range(len(my_x)):
# # # # #             print(my_x[i], reversed_x[i])
# # # # #             if my_x[i] == reversed_x[i]:
# # # # #                 pass
# # # # #             else:
# # # # #                 return False
# # # # #         return True


# # # # # print(isPalindrome(121))

# # # # my_list = [1, 2, 3, 4, 5, 6]

# # # # firstHalf = my_list[0:len(my_list)//2]
# # # # secondHalf = my_list[len(my_list)//2::]

# # # # print(firstHalf)
# # # # print(secondHalf)

# # # def myAtoi(s):
# # #     s = s.strip()

# # #     result = 0 

# # #     if not s:
# # #         return result

# # #     if s[0] in ['-', '+']:
# # #         sign = -1 if s[0] == '-' else 1
# # #         s = s[1:]
# # #     else:
# # #         sign = 1

# # #     for char in s:
# # #         if char.isdigit():
# # #             result = result * 10 + int(char)
# # #         else:
# # #             break

# # #     result *= sign

# # #     if result < -2**31:
# # #             result = -2**31
# # #         elif result > 2**31 - 1:
# # #             result = 2**31 - 1

# # #     return result

# # # print(myAtoi("42"))

# # def concatenatedBinary(n: int) -> int:
# #         binary = ""
# #         for num in range(n + 1):
# #             binary += bin(num)[2:]

# #         print(binary)
# #         decimal = int(binary, 2)
# #         print(decimal)
# #         return decimal

# # # concatenatedBinary(3)  # Output: 27

# def battleship(board, attacks):
#     rows = len(board)
#     cols = len(board[0]) if rows > 0 else 0
#     hits = 0

#     for attack in attacks:
#         row, col = attack
#         if 0 <= row < rows and 0 <= col < cols:
#             if board[row][col] == 'X':
#                 hits += 1
#                 board[row][col] = 'H'  # Mark as hit
#             elif board[row][col] == 'O':
#                 board[row][col] = 'M'  # Mark as miss

#     return hits

# print(battleship([['O', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']], [(0, 2), (1, 0), (2, 1), (0, 0)]))  # Output: 3

print(3+3)