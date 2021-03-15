empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

#more_numbers =list(numbers)
#more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)

print(numbers is more_numbers) # nem ugyan az tehát false
print(numbers == more_numbers)#a tartalom viszont ua tehát True