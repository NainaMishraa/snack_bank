fruits = ["apple", "banana", "mango", "orange", "kiwi", "pineapple", "grape", "watermelon"]
fruit_categories = {"tropical":["mango", "banana", "kiwi", "pineapple"],
                    "non-tropical":["apple", "orange", "grape", "watermelon"]}
tropical_fruits, non_tropical_fruits =[], []
for fruit in fruits:
    if fruit in fruit_categories["tropical"]:
        tropical_fruits.append(fruit)
    else:
        non_tropical_fruits.append(fruit)
print("Tropical fruits:", tropical_fruits)
print("Non-tropical fruits:", non_tropical_fruits)