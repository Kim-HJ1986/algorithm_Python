def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for alpha in string:
        if alpha.isalpha():
            alphabet_occurrence_array[ord(alpha)-97] += 1
        else:
            continue

    max_idx = alphabet_occurrence_array.index(max(alphabet_occurrence_array))
    return chr((max_idx)+97)


#result = find_max_occurred_alphabet(input)
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))