# 1. Remove duplicates from list
def remove_duplicate(data):
    unique_val = set(())
    for d in data:
        unique_val.add(d)
    return list(unique_val)


data = [1, 1, 2, 2, 3, 4]
# print(remove_duplicate(data))


# 2. Count frequency of characters
def frequency_of_character(charters):
    frequency = {}
    for c in range(len(charters)):
        if charters[c] in frequency:
            frequency[charters[c]] = frequency[charters[c]] + 1
        else:
            frequency[charters[c]] = 1
    return frequency


character = "banana"
# print(frequency_of_character(character))


# 3. Find largest number in list
def largest_number(num_list=[]):
    larget_num = num_list[0]
    for num in num_list:
        if num > larget_num:
            larget_num = num
    return larget_num


numbers = [30, 10, 60, 3, 45, 2, 506, 234]
# print(largest_number(numbers))

# Find first non-repeat characters
# input "aabbced"
# output "c"

def find_first_non_repeat(characters):
    seprator = {}
    result = False
    for i in range(len(characters)):
        if characters[i] in seprator:
            seprator[characters[i]] = seprator[characters[i]] + 1
        else:
            seprator[characters[i]] = 1
    for x in seprator:
        if seprator[x] == 1:
            result = x
            break
    return result

print(find_first_non_repeat("aabbcedc"))
