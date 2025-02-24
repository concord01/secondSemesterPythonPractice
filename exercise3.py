movies = ["The Thing", "Animal House", "Rush Hour", "Rush Hour 2"]


print(movies[0])


num = 0
for movie in movies:
    print(str(num) + "." + movie)
    num = num + 1

# different list methods
movies.sort() # sorts list in order or alphabetically
print(movies)

movies.append("Fantastic 4") # append adds to the end
print(movies)

movies.pop() # pop removes item from end of list
movies.pop()
print(movies)

# remove removes first instance of an item
movies.remove("Animal House") 
print(movies)

# inser inserts itme at specific index
movies.insert(2, "Deadpool")
print(movie)

print(len(movies)) # len gives the length of our list


# print last item in our list
print(movies[2])

# removing numbers from a list
numbers = [1, 2, 2, 9, 2, 2, 12, 9]
for num in numbers:
    if num == 2:
        numbers.remove(2)

print(numbers)

name = "joaquin hoyem"
for letter in name:
    print(letter)
    