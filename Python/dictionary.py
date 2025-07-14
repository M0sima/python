
#Dictionaries

person ={
    "name": "Bob",
    "age": 20,
    "city": "Johannesburg"
}

print(person["name"])

#Add a new key-value pair

person["qualification"]="Matric"
print(person)

#Modify the existing key-value
person["age"]=30
print(person)

#Delete a key-value
del person["city"]
print(person)
