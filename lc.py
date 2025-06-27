def twoSum(nums, target: int) -> int:
    hashMap = dict()
    for i, num in enumerate(nums):
        complement = target-num
        if complement in hashMap:
            return [i, hashMap[complement]]
        else:
            hashMap[nums[i]] = i 
    return []



def isAnagram(s: str, t: str) -> bool:
    # sorted(s) == sorted(t)
    if len(s) != len(t):
        return False
    hashMap = dict() 
    for x in s: 
        if x in hashMap:
            hashMap[x] += 1
        else:
            hashMap[x] = 1 
    print(hashMap)

    for x in t: 
        if x not in hashMap:
            return False
        else:
            hashMap[x] -= 1
            if hashMap[x] == 0:
                del hashMap[x]

    print(hashMap)
    return len(hashMap) == 0


isAnagram = isAnagram('aamir','rimaa')
print(isAnagram)

