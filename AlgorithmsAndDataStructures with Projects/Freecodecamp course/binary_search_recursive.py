def binary_search_recursive(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
              return binary_search_recursive(list[midpoint + 1:],target)
            else:
              return binary_search_recursive(list[:midpoint], target)
def verify(result):
            print("Target found: ", result)
numbers = [1,2,3,4,5,6,7,8,9]
result = binary_search_recursive(numbers, 7)
verify(result)