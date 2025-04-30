# 1. Create a tuple with different datatypes
mixed_tuple = (10, "Hello", 3.14, True)
print("Tuple with different datatypes:", mixed_tuple)
# 2. Create another tuple of integers
int_tuple = (1, 2, 3, 4, 5)
print("Integers tuple:", int_tuple)
# 3. Create a new tuple by adding 9 to each element
# Using a generator expression with tuple comprehension
update_tuple = tuple(x + 9 for x in int_tuple)
print("Tuple after adding 9 to each element:", update_tuple)
# 4. Count the occurrences of an element in the tuple
# For example, count how many times '12' appears in the update tuple
element_to_count = 12
count = update_tuple.count(element_to_count)
print(f"Occurrencesof {element_to_count}:", count)
# 5. Perform slicing on the tuple
# For example, take elements from indees 1 to 3
sliced_tuple = update_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)