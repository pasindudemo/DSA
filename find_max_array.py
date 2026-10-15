arr = [12, 305, 110, 10, 34, 35]


def find_max_array (arr):
    max_value = 0
    for i in range(len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

print(find_max_array(arr))