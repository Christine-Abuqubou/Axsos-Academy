x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

for i in range(len(students)):
    students[1]["last_name"] = "pryan"
print(students)

for i in range(len(sports_directory)):

    sports_directory["soccer"][0] = "andres"
print(sports_directory)

# for i in range(len(z)):
z[0]["y"] = 30
print(z)

for i in range(len(x)):
    x[1][0] = 15
print(x)
