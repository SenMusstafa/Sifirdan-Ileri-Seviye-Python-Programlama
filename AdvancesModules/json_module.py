import json

# JSON string representing a person
person_string = '{"name": "Sema", "languages": ["Python","JavaScript"]}'
# result = person["name"]
# result = person["languages"]
# print(result)

# Converting JSON string to a dictionary

# result = json.loads(person_string)
# print(result)

# Loading data from a JSON file
# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])



# Converting a dictionary to a JSON string 
person_dict = {"name": "Sema", "languages": ["Python", "C#"]}

# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# Saving a dictionary as a JSON file
with open("person.json", "w") as file:
    json.dump(person_dict, file)
