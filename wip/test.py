my_array = [60, -60, 180, -60, 380, -60]


first_two_elements = my_array[:2]
positive_elements = [abs(element) for element in first_two_elements]
smallest_value = min(positive_elements)

print (smallest_value)