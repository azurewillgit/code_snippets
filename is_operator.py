
shopping_list_monday = ['apples', 'milk', 'eggs']
shopping_list_friday = ['apples', 'milk', 'eggs']

# == compares the contents of the list
print(shopping_list_monday == shopping_list_friday)

# Is compares the memory address of both lists
print(shopping_list_monday is shopping_list_friday)

# The id function returns the actual address
print(f"shopping list monday: {id(shopping_list_monday)}")
print(f"shopping list friday: {id(shopping_list_friday)}")

# If we compare them with the == operator, we see the actual difference
print(id(shopping_list_monday) == id(shopping_list_friday))

# Bonus: This shows that assigning an existing list will reference the same address.
# Be careful when reassigning lists!
shopping_list_weekend = shopping_list_friday
print(f"shopping list friday: {id(shopping_list_friday)}")
print(f"shopping list weekend: {id(shopping_list_weekend)}")