def neutralise(s1, s2):

    result_list = []
    
    for stringa1, stringa2 in zip(s1, s2):

        if stringa1 == stringa2:

            result_list.append(stringa1)

        else:

            result_list.append("0")

    return ''.join(result_list)

stringa_1 = "--++--"
stringa_2 = "++--++"

print("Test case 1:\n")
print(neutralise(stringa_1, stringa_2))

stringa_3 = "-+-+-+"
stringa_4 = "-+-+-+"

print("\nTest case 2:\n")
print(neutralise(stringa_3, stringa_4))
