public_key1 = 17115212
public_key2 = 3667832

loop = 0
subject_number = 7
value = 1
while True:
    loop += 1
    value *= subject_number
    value %= 20201227
    if value == public_key1 or value == public_key2:
        break

if value == public_key1:
    pkey = public_key2
else:
    pkey = public_key1
value = 1
for i in range(loop):
    value *= pkey
    value %= 20201227

print(f"Solution 1: {value}")
