def rotate(text, key):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    rot_abc, rot_text = '', ''
    if key == 26:
        key = 0
    while count < 26:
        if abc[key] == 'z':
            rot_abc += abc[key]
            key = 0
        if len(rot_abc) == 26:
            break
        rot_abc += abc[key]
        key += 1
        count += 1
    for i in text:
        if i.isupper():
            rot_text += i.lower().replace(abc[abc.index(i.lower())], rot_abc[abc.index(i.lower())]).upper()
            continue
        if not i.isalpha():
            rot_text += i
            continue
        rot_text += i.replace(abc[abc.index(i)], rot_abc[abc.index(i)])
    return rot_text

text1 = 'The quick brown fox jumps over the lazy dog.'
text2 = 'Testing 1 2 3 testing'
text3 = "Let's eat, Grandma!"

print(rotate(text2, 21))

# ! Otra solucion al problema
# def rotate(text, key):
#     abc = 'abcdefghijklmnopqrstuvwxyz'
#     rot_abc = abc[key % 26:] + abc[:key % 26]
#     rot_text = ''

#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             index_in_abc = abc.index(char.lower())
#             rotated_char = rot_abc[index_in_abc]
#             rot_text += rotated_char.upper() if is_upper else rotated_char
#         else:
#             rot_text += char

#     return rot_text