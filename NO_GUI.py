import random
import time
def ran_gen():
   value =  random.randrange(1, 20)
   print(value)
   time.sleep(random.uniform(1, 1.9))
   return value

def check(nums, user_nums):
    for i in range(len(nums)):
        if nums[i] != user_nums[i]: return False
    return True




#main
print("Memerize the numbers in the correct order")
i = 5
while True:  
    nums = []
    j = i
    while j > 0:
       nums.append(ran_gen())
       j -= 1
    j = i
    print("Enter the", i, "numbers in the correct order:")
    user_nums = []
    while j > 0:
        user_nums.append(int(input()))
        j -= 1 

    if check(nums, user_nums): print("GNZ, IT WAS CORRECT")
    else: 
        print("the numbers were wrong")
        break    


    i += 1

