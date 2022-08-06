word = str(input())

upper_char_list = list(word.upper())
alphabet_list = list(0 for i in range(26))

ascii_A = ord('A')
for char in upper_char_list:
    index = ord(char) - ascii_A
    alphabet_list[index] += 1

max_value = max(alphabet_list)
max_index = alphabet_list.index(max_value)
alphabet_list.remove(max_value)
if alphabet_list.__contains__(max_value):
    print('?')
else:
    print(chr(max_index + ascii_A))
