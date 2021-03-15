pangram ="The quick borwn fox jumps over the lazy dog"

letters =sorted(pangram)
print(letters)

numbers = [2.3,4.5,8.7,3.1,9.2,1.6]

sorted_numbers =sorted(numbers) # másik listát készít és azt rendezi
print(numbers)
print(sorted_numbers)

numbers.sort() #az eredeti listát rendezi sorba!!! ha másik változónak adjuk át
#none lesz
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the crazy dog",
                        key=str.casefold) #fontos, hogy a casefold zárójeleit
                        #ne vegyük bele str.casefold nem str.casefold()!
print(missing_letter)

names =[
    "Graham",
    "John",
    "terry",
    "eric",
    "Terry",
    "michael"
]
names.sort(key=str.casefold)
print(names)


