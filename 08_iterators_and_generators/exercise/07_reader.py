def read_next(*args):
    for seq in args:
        # for el in seq:
        #     yield el
        yield from seq


# Test code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print('--------------------------------------------------------------------------------------------------')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

