def search_imperative(array, target):
    for el in array:
        if el == target:
            return True
    return False


print(search_imperative([1,2,3,4,5],6))