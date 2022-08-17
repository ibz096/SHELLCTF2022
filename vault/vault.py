from pickletools import string1


flag = ''
string_array = ['4654434c4c454853', '343534383433357b', '3434353334633463', '3535333133623736', '3336373333323566', '3631333533323733', '3333336635373665', '3766333937333734', '7d64']

for word in string_array:
    quote_a = bytes.fromhex(word).decode("ASCII")
    quote   = quote_a.replace(';', '\n- ')
    flag += (quote[::-1])

print(flag)
#SHELLCTF{5348454c4c4354467b31355f523376337235316e675f333473793f7d}

flag2 = ''
string_array2 = ['5348454c4c4354467b31355f523376337235316e675f333473793f7d']
for word in string_array2:
    quote_a = bytes.fromhex(word).decode("ASCII")
    quote   = quote_a.replace(';', '\n- ')
    flag2 += (quote)

print(flag2)
#SHELLCTF{15_R3v3r51ng_34sy?}