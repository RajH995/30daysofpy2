# # # # # # # # my_list = [1, 2, 3, 4, 5]

# # # # # # # # for i in range(len(my_list)//2):
# # # # # # # #     my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]

# # # # # # # # print(my_list)  # Output: [5, 4, 3, 2, 1]

# # # # # # # def romantoint(roman_num):
# # # # # # #     roman_dict = {
# # # # # # #         'I': 1,
# # # # # # #         'V': 5,
# # # # # # #         'X': 10,
# # # # # # #         'L': 50,
# # # # # # #         'C': 100,
# # # # # # #         'D': 500,
# # # # # # #         'M': 1000
# # # # # # #     }
# # # # # # #     total = 0
# # # # # # #     prev_value = 0

# # # # # # #     for char in reversed(roman_num):
# # # # # # #         value = roman_dict[char]
# # # # # # #         if value < prev_value:
# # # # # # #             total -= value
# # # # # # #         else:
# # # # # # #             total += value
# # # # # # #         prev_value = value

# # # # # # #     return total


# # # # # # # def letterCombinations(digits):
# # # # # # #     if not digits:
# # # # # # #         return []

# # # # # # #     digit_to_letters = {
# # # # # # #         '2': 'abc',
# # # # # # #         '3': 'def',
# # # # # # #         '4': 'ghi',
# # # # # # #         '5': 'jkl',
# # # # # # #         '6': 'mno',
# # # # # # #         '7': 'pqrs',
# # # # # # #         '8': 'tuv',
# # # # # # #         '9': 'wxyz'
# # # # # # #     }

# # # # # # #     def backtrack(index, path):
# # # # # # #         if index == len(digits):
# # # # # # #             combinations.append("".join(path))
# # # # # # #             return
# # # # # # #         possible_letters = digit_to_letters[digits[index]]
# # # # # # #         for letter in possible_letters:
# # # # # # #             path.append(letter)
# # # # # # #             backtrack(index + 1, path)
# # # # # # #             path.pop()

# # # # # # #     combinations = []
# # # # # # #     backtrack(0, [])
# # # # # # #     return combinations

# # # # # # # def isPalindrome(x):
# # # # # # #         my_x = str(x)
# # # # # # #         reversed_x = "".join(reversed(my_x))
# # # # # # #         for i in range(len(my_x)):
# # # # # # #             print(my_x[i], reversed_x[i])
# # # # # # #             if my_x[i] == reversed_x[i]:
# # # # # # #                 pass
# # # # # # #             else:
# # # # # # #                 return False
# # # # # # #         return True


# # # # # # # print(isPalindrome(121))

# # # # # # my_list = [1, 2, 3, 4, 5, 6]

# # # # # # firstHalf = my_list[0:len(my_list)//2]
# # # # # # secondHalf = my_list[len(my_list)//2::]

# # # # # # print(firstHalf)
# # # # # # print(secondHalf)

# # # # # def myAtoi(s):
# # # # #     s = s.strip()

# # # # #     result = 0 

# # # # #     if not s:
# # # # #         return result

# # # # #     if s[0] in ['-', '+']:
# # # # #         sign = -1 if s[0] == '-' else 1
# # # # #         s = s[1:]
# # # # #     else:
# # # # #         sign = 1

# # # # #     for char in s:
# # # # #         if char.isdigit():
# # # # #             result = result * 10 + int(char)
# # # # #         else:
# # # # #             break

# # # # #     result *= sign

# # # # #     if result < -2**31:
# # # # #             result = -2**31
# # # # #         elif result > 2**31 - 1:
# # # # #             result = 2**31 - 1

# # # # #     return result

# # # # # print(myAtoi("42"))

# # # # def concatenatedBinary(n: int) -> int:
# # # #         binary = ""
# # # #         for num in range(n + 1):
# # # #             binary += bin(num)[2:]

# # # #         print(binary)
# # # #         decimal = int(binary, 2)
# # # #         print(decimal)
# # # #         return decimal

# # # # # concatenatedBinary(3)  # Output: 27

# # # def battleship(board, attacks):
# # #     rows = len(board)
# # #     cols = len(board[0]) if rows > 0 else 0
# # #     hits = 0

# # #     for attack in attacks:
# # #         row, col = attack
# # #         if 0 <= row < rows and 0 <= col < cols:
# # #             if board[row][col] == 'X':
# # #                 hits += 1
# # #                 board[row][col] = 'H'  # Mark as hit
# # #             elif board[row][col] == 'O':
# # #                 board[row][col] = 'M'  # Mark as miss

# # #     return hits

# # # print(battleship([['O', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']], [(0, 2), (1, 0), (2, 1), (0, 0)]))  # Output: 3




# # # def longestPalindrome(s: str) -> str:
# # #     if (s.strip() == "") :
# # #         return ""

# # #     start, maxlen = 0, 0

# # #     def expandFromMiddle(left, right):
# # #         while left >= 0 and right < len(s) and s[left] == s[right]:
# # #             left -= 1
# # #             right += 1
# # #         return right - left - 1

# # #     for i in range(len(s)):
# # #         len1 = (expandFromMiddle(i, i))
# # #         len2 = (expandFromMiddle(i, i+1))
# # #         currentlen = max(len1, len2)

# # #         if currentlen > maxlen:
# # #             maxlen = currentlen
# # #             start = i - (currentlen-1)//2

# # #     return s[start: maxlen + start]


# # # print(longestPalindrome("       "))

# # nums = [1, 2, 3, 4, 5]
# # target = 9

# # my_dict = dict(zip(nums, list(map(lambda x: target - x, nums))))


# # def my_func(i=0):
# #     for key in my_dict:
# #         i = list(my_dict.keys()).index(key)
# #         for key2 in my_dict:
# #             if list(my_dict.keys()).index(key2) != i:
# #                 my_dict[key] = my_dict[key] - key2
# #                 i += 1
# #             else:
# #                 i += 1
# #                 pass


# # my_func()


# # print(my_dict)  




# def fourSum(nums, target):
#     if len(nums) < 3:
#         return []

#     nums.sort()
#     res = []

#     for num in range(len(nums)-3):
#         if num > 0 and num<len(nums)-1 and nums[num] == nums[num-1]:
#             continue
#         for num1 in range(num+1, len(nums)-2, 1):
#             left = num1 + 1
#             right = len(nums)-1
#             # if num1 > 1 and num1<len(nums)-1 and nums[num1] == nums[num1-1]:
#             #     continue
#             current = nums[num] + nums[num1] + nums[left] + nums[right]
#             while left < right:
#                 if current < target:
#                     left += 1
#                 elif current > target:
#                     right -= 1
#                 elif current == target:
#                     if ([nums[num], nums[num1], nums[left], nums[right]] not in res):
#                         res.append([nums[num], nums[num1], nums[left], nums[right]])
#                         left += 1
#                         right -= 1
#                     else:
#                         left += 1
#                         right -= 1



#                         while left < right and nums[left] == nums[left-1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right+1]:
#                             right -= 1

#                 current = nums[num] + nums[num1] + nums[left] + nums[right]

            

#     return res


# print(fourSum([-2,-1,-1,1,1,2,2], 0))
# print(fourSum([1,0,-1,0,-2,2], 0))
# print(fourSum([2,2,2,2,2], 8))


# # def threeSum(nums):
# #     nums.sort()
# #     res = []

# #     for i in range(len(nums)-2):
# #         if i>0 and nums[i] == nums[i-1]:
# #             continue

# #         if nums[i]>0:
# #             break

# #         left, right = i+1, len(nums) -1

# #         while left < right:
# #                 total = nums[i] +nums[left] + nums[right]
# #                 if total < 0:
# #                     left += 1
# #                 elif total > 0:
# #                     right -= 1
# #                 else:
# #                         res.append([nums[i], nums[left], nums[right]])
# #                         left += 1
# #                         right -= 1



# #                         while left < right and nums[left] == nums[left-1]:
# #                             left += 1
# #                         while left < right and nums[right] == nums[right+1]:
# #                             right -= 1
# #     return res

# # print(threeSum([2,2,2,2,2,2,0,1,-1,-2, -2, -2, -2, -2]))




def maxArea(height):
#         biggest = 0
#         for num in range(len(height)):
#             right = num + 1
#             while right < len(height):
#                 shortest = min(height[num], height[right])
#                 current = shortest * (right-num)
#                 if current > biggest:
#                     biggest = current
#                 right += 1
#         return biggest

#O(n) below

        biggest = 0
        left = 0
        right = len(height) - 1
        while left < right:
            shortest = min(height[left], height[right])
            current = shortest * (right-left)
            
            if current > biggest:
                biggest = current

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return biggest