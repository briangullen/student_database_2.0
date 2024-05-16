def list_names(student_data: list[dict[str, str]]):
    for i, student in enumerate(student_data):
        print(f"{i + 1}. {student['name']}")


student_data = [
  {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
  {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
  {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]

list_names(student_data)