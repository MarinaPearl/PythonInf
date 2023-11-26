def calculate_and_print_pascal_triangle(n):
    if not isinstance(n, int) or n <= 0:
        print("Введите целое положительное число.")
        return

    pascal_triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
        pascal_triangle.append(row)

    max_len_rows = len(' '.join(map(str, pascal_triangle[-1])))
    for row in pascal_triangle:
        print(f"{' '.join(map(str, row)):^{max_len_rows}}", sep="", end="\n")


while True:
    try:
        n = int(input("Введите число: "))
        calculate_and_print_pascal_triangle(n)
        break
    except ValueError:
        print("Ошибка: неправильный ввод.")