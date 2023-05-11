# Arrays
array = ["Karl", "Carl", "Til", "Philip"]
array.append("Hannah")
array += ["Cora", "Wilhelm"]
array.extend(["Max", "Leni", "Mailin"])
print(array)

# Dictionaries
dict = {
    "alter":17,
    "vorname":"Carl",
    "nachname":"Zimmermann"
}
print(dict)

# Tuple
tuple = (17, "Carl", "Zimmermann")
print(tuple)

# Sets
set = {2, 5, 9, frozenset([5,2])}
print(set.intersection({2,5, 'a'}))
print(set)