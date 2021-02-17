shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list)) #ID remains the same, because the lists are mutable4
                        #python didnt need to create a new object!!!
                        #str and tuple_ immutable. list :mutable!!!

print(another_list)

a = b = c = d = e = f = another_list
print(a)
print("adding cream")
b.append("cream")
print(c)
print(d)
print(shopping_list)
print(another_list)
print(a)