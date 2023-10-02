# trying out automated testing ideas/routines


def split_amount(amount, n):
    portion, remain = amount // n, amount % n
    portions = []
    for i in range(n):
        portions.append(portion)
        if remain >= 1:
            portions[-1] += 1
            remain -= 1
    return portions


# split = split_amount(5, 3)
# print(split)

split = split_amount(5, 4)
print(split)

split = split_amount(9, 8)
print(split)
