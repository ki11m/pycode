nums = [5,3,6,9,7,4,1,2]
def shellsort(nums):
    step = len(nums)//2
    while step > 0:
        for i in range(step, len(nums)):
            index = i
            while index >= step and nums[index-step] > nums[index]:
                nums[index], nums[index - step] = nums[index - step], nums[index]
                index -= step
        step //= 2
    print(nums)
shellsort(nums)