class Solution():
    def two_sum(list,target):
        seen = {}
        for i in range(len(list)):
            diff = target - list[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[list[i]] = i

myList = [1,2,3,4,5,6,7,8,9]

print(two_sum(myList,12))