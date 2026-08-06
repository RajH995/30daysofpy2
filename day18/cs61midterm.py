# sixty_seven = lambda x : lambda y: (print(x+y) and 67)

# seventy_six = lambda x : lambda y: (76 and print (x+2*y))

# print(sixty_seven(7)(6) or seventy_six(6)(7))

# print(76 and 67)

myNums = [0, 0 , 0, 1,1, 2, 3]

def fliter(nums):
    for i in range(len(nums)):
        if i > 0 and i < len(nums)-1 and nums[i] == nums[i+1]:
            i +=1
        else:
            print(nums[i])

print(fliter(myNums))


