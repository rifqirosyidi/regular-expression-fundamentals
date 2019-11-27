import re

# ===== Basic Search =====
print("\nBASIC SEARCH")
if re.search("ape", "That apex is in apple"):
    print("There is an Ape")


# ===== Find All That ONLY Matches =====
print("\nFIND MATCHES")
all_apes = re.findall("ape", "There is an ape in apex and in the ape tree ")

for ape in all_apes:
    print(ape, end=", ") # However its only going to match the specific only

print("")


# ===== Find All That Matches =====
print("\nFIND MATCHES")
all_apes = re.findall("ape.", "There is an ape in apex and in the apeace tree ")
# the (.) dot give one more character after the match if it is not then it will gave an empty space

for ape in all_apes:
    print(ape, end=", ") # However its only going to match the specific only

print("")

# ===== Using Finditer to get the index =====
print("\nFIND ITER")
the_str = "There is an ape in apex and in the apeace tree"

for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(the_str[loc_tuple[0]:loc_tuple[1]])


# ===== Match one of any several character =====
print("\nMATCH ANY")
the_animal = "Cat rat bat lat mat"

end_at_and_start_defined = re.findall("[crblqe]at", the_animal) # cat is not included because CASE SENSITIVE
for i in end_at_and_start_defined:
    print(i)


# ===== RANGE =====
print("\nRANGE")
the_animal = "Cat rat bat lat mat pat zat sat"
l_animal = []

animal_to_search = re.findall("[c-rC-R]at", the_animal)
for i in animal_to_search:
    l_animal.append(i)

print(l_animal) # Zat Sat is not included because it only search character between c-r and C-R


# ===== EXCEPT =====
print("\nEXCEPT => [^<anychar>] ")
the_animal = "Cat rat bat lat mat pat zat sat"
l_animal = []

animal_to_search = re.findall("[^c-rC-R]at", the_animal)
for i in animal_to_search:
    l_animal.append(i)

print(l_animal) # Zat Sat is not included because it only search character between c-r and C-R

