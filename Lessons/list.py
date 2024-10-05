"""9/30 - practicing lists"""

# Creating empty list 2 ways
my_numbers: list[float] = []  # creating empty list named my_numbers using literal
my_numbers: list[float] = list()  # doing the exact same thing but using a constructor

# print(my_numbers)

# String Analogy
# my_name: str = "" #creating string using literal
# my_name: str = str() #using a constructor

# Adding a value to a list
my_numbers.append(1.5) # adding 1.5 to the list
# print(my_numbers)


# Creating an already populated list
game_points: list[int] = [102, 86, 94]
#print(game_points)

# Using subscription notation to access object in list
# print(game_points[2])
last_game: int = game_points[2] #accessing object in list and storing as a variable
# print(last_game)

# Modifying by Index
# (Becuase lists are mutable)
game_points[1] = 72
# print(game_points)

# class_num: str = "110" #change it to "210"
# class_num[0] = "2" #this doesn't work becuase strings are not mutable

# length of a list
# print(len(game_points))

# Remove an item from a list
game_points.pop(1)
# print(game_points)

def display(int_list: list[int]) -> None:
    """prints all elements in list"""
    index: int = 0 
    while index < len(int_list):
        print(int_list[index])
        index += 1

# display(game_points)

game_points.append(72)
game_points.append(72)
print(game_points)