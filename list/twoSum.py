def twoSum(**data):
    nums, target = [], 0
    res = []
    nums = list(data['nums'])
    target = int(data['target'])
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([i,j])
    for val in res:
        print(val)

twoSum(nums=[2, 7, 3, 11, 15, 7, 6], target=9)
