
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
#splitter(my_array=my_test_bug)

def normalize_duration_timings(duration_array=my_test_bug):
    # Duration array representing Morse code tones (with imperfect timing)

    # Find the position of the first non-pause element
    first_non_pause_index = next((i for i, duration in enumerate(duration_array) if duration > 0), None)

    positive_durations = [duration for duration in duration_array if duration > 0]
    average_duration = float(sum(positive_durations))/float(len(positive_durations)) 

    # Estimate words per minute and calculate dit duration
    average_dit_duration = sum([duration for duration in duration_array[first_non_pause_index:] if duration > 0]) / len([duration for duration in duration_array[first_non_pause_index:] if duration > 0])
    wpm_estimate = int(1200 / average_dit_duration) if average_dit_duration > 0 else 0
    dit_length_estimate = int(1200 / wpm_estimate)
    dah_length_estimate = int(3*dit_length_estimate)

    # Define a threshold to distinguish between Dits and Dahs
    threshold = average_duration # 3 * average_dit_duration 
    #print (threshold)

    # Convert the array to Morse code string
    morse_code = ""
    normalized_durations = []
    for duration in duration_array[first_non_pause_index:]:
        if duration > 0 and duration <= threshold:  # Dit
            morse_code += "."
            normalized_durations.append(dit_length_estimate)
            normalized_durations.append(-dit_length_estimate)
        elif duration >= threshold:  # Dah
            morse_code += "-"
            normalized_durations.append(dah_length_estimate)
            normalized_durations.append(-dit_length_estimate)
        elif duration < 0 and abs(duration) >= threshold: # Pause
            morse_code += " " # FIXME: more types of pauses (word, character, ...)

    result = {"wpm_estimate": wpm_estimate, "morse_code_normalized": morse_code, "normalized_durations": normalized_durations}

    return result


print (normalize_duration_timings(duration_array=my_v))
print (normalize_duration_timings(duration_array=my_test_bug))


