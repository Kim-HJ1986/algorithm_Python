input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    sList = list(string)
    print(sList.count("0"))
    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)