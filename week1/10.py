input_string = input("Please enter an string :")
string_length = len(input_string)
i=0
while i < string_length:
    if (i%2) == 1:
        print(input_string[i])
    i += 1