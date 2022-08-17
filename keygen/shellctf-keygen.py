flag = ''
#The flag is stored in the getstring() function from which this was pulled from
bytearray = ['53', '48', '45', '4c', '4c', '43', '54', '46', '7b', '6b', '33', '79', '67', '65', '6e', '5f', '31', '73', '5f', '99','30', '6f', '4c', '7d']
for char in bytearray:
    # print(int(char, 16))
    try:
        flag += bytes.fromhex(char).decode("ASCII")
    except:
        flag += (f"{char}")
print(flag)
#SHELLCTF{k3ygen_1s_990oL}