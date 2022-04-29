
def perfectSquare(x: int) -> bool:
	return (int(x ** 0.5)) ** 2 == x


# метод Ферма
def ferma(number: int) -> tuple[int, int]:
	x = int(number ** 0.5) + 1
	while not perfectSquare(x * x - number):
		x += 1
	y = int((x * x - number) ** 0.5)
	a = x - y
	b = x + y
	return a, b


if __name__ == '__main__':
	number = 75  # відоме непарне ціле число, яке є добутком двох невідомих чисел
	print(ferma(number))
