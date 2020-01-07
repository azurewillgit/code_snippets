shopping_list = ['apples', 'oranges', 'eggs']
shopping_list_2 = list()

nested_list = [
    32.0,
    'dog',
    ['dog_treats', 'cat_treats']
]

print(shopping_list[0])  # Output: apples
print(shopping_list[-1])  # Negative indexing starts at the end of the list
print(nested_list[2][0])  # Nested lists can be accessed like this

# Methods

# append() - add item to the end of a list
shopping_list.append('cheese')
print(shopping_list)

# insert() - add item at any position in the list, use first argument as index
shopping_list.insert(0, 'garlic')
print(shopping_list)

# pop() - removes last item in the list and returns it
popped = shopping_list.pop()
print(popped)
print(shopping_list)

# sort() - This will sort any list (either alphabetically or numerically) in-place, meaning it changes the list
nums = [2, 1, 4, 3, 5]
nums.sort()
print(nums)



