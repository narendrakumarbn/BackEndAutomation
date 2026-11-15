
import json

# 1. json.loads() - JSON String to Dictionary

details = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''

dict_details = json.loads(details)

print("----- json.loads() -----")
print(dict_details["name"])
print(dict_details["age"])


# 2. json.load() - JSON File to Dictionary

with open("employee.json", "r") as file:
    employee_data = json.load(file)

print("\n----- json.load() -----")

# Normal dictionary access
print(employee_data["company"])

# List index + dictionary key access
print(employee_data["employees"][0]["name"])
print(employee_data["employees"][1]["name"])

# Index-based access
print(employee_data["employees"][0]["designation"])
print(employee_data["employees"][1]["designation"])

# Access nested dictionaries
print(employee_data["employees"][0]["department"]["technology"])
print(employee_data["employees"][1]["department"]["technology"])

# Loop through employees
for employee in employee_data["employees"]:
    print(employee["name"], employee["designation"])


# Loop through employees and check designation

print("\n----- For Loop + If Condition -----")

for employee in employee_data["employees"]:

    if employee["designation"] == "QA Engineer":
        print("Employee Found!")
        print("Name:", employee["name"])
        print("Designation:", employee["designation"])
        print("Department:", employee["department"]["name"])

    elif employee["designation"] == "Software Engineer":
        print("Software Engineer Found!")
        print("Name:", employee["name"])

    else:
        print("Employee not found")