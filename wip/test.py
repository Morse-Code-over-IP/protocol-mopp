my_array = [60, -60, 180, -60, 380, -60]
my_v = [-2000, +50, -50, +50, -50, +50, -50, +150]
my_test_bug = [ -347, +145, -183, +51, -160, +51, -47, +47, -51, +47, -211, +144 ] 

def splitter(my_array):
    print (my_array)

    first_two_elements = my_array[:2]
    positive_elements = [abs(element) for element in first_two_elements]
    smallest_value = min(positive_elements)

    print (smallest_value)

    fractional_multiples = []
    non_fractional_multiples = []

    i = 0
    for element in my_array:
        if element % smallest_value == 0:
            fractional_multiples.append(element)
            i += 1
        else:
            break

    non_fractional_multiples = my_array[i:]
    print (fractional_multiples)
    print (non_fractional_multiples)



#splitter(my_array=my_array)

#splitter(my_array=my_v)
splitter(my_array=my_test_bug)
