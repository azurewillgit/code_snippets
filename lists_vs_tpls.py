import timeit

# To test the performance, we call the timeit function from the timeit module.
# What this does is run a certain statement a given amount of time.
# We will create a tuple and a list a million times and output the time it took to do that.
# Note that the statement has to be a string.
# I used f-strings to round the output and make it look cleaner.

tuple_performance = timeit.timeit(stmt='(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)', number=100000)
list_performance = timeit.timeit(stmt='[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', number=100000)
print(f"Creating a tuple took {round(tuple_performance, 4)} seconds")
print(f"Creating a list took {round(list_performance, 4)} seconds")

