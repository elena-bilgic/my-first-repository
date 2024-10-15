def square(side_length):
    p = side_length * 4
    a = side_length ** 2
    return p, a

p, a = square(5)
print(f"Периметер квадрата равен {p}")
print(f"Площадь квадрата равна {a}")
