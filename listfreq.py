Animals = ["dog" , "cat" , "lion", "tiger" , "fox", "cat", "tiger"]



for animal in set(Animals):
    frequency = Animals.count(animal)

    print(frequency,animal)

    
#unique_ani = set(Animals)
# unique_animals = set(Animals)  # Get unique animals
# for animal in unique_animals:
    

#     frequency = Animals.count(animal)  # Count occurrences in original list
#     print(f"{animal}: {frequency}")


# Animals = ["dog", "cat", "lion", "tiger", "fox", "cat", "tiger"]

# freq_dict = {}
# for animal in Animals:
#     if animal in freq_dict:
#         freq_dict[animal] += 1
#     else:
#         freq_dict[animal] = 1

# # Print results
# for animal, count in freq_dict.items():
#     print(f"{animal}: {count}")




