import json

file = "database.json"

# ---------- CREATE ----------
def create_students():
    students = [
        {
            "name": "Chevy",
            "age": 14,
            "favorite_subject": "Math 3",
            "favorite_color": "Red",
            "favorite_song": "Vroom Vroom by Charli XCX"
        },
        {
            "name": "Sophia",
            "age": 13,
            "favorite_subject": "Music",
            "favorite_color": "Green, Blue, Pink",
            "favorite_song": "123-78 by BoyNextDoor"
        },
        {
            "name": "Kim",
            "age": 14,
            "favorite_subject": "Math 3",
            "favorite_color": "Blue",
            "favorite_song": "Meow"
        },
        {
            "name": "Meowl",
            "age": 13,
            "favorite_subject": "Statistics",
            "favorite_color": "Orange and Blue",
            "favorite_song": "Cats Song"
        },
        {
            "name": "Geoff",
            "age": 67,
            "favorite_subject": "Lunch",
            "favorite_color": "Beige",
            "favorite_song": "Let Me Check Spotify"
        }
    ]

    with open(file, "w") as f:
        json.dump(students, f, indent=4)

    print("Students created in database.\n")


# ---------- READ ----------
def read_students():
    with open(file, "r") as f:
        students = json.load(f)

    print("Current Students:\n")

    for s in students:
        print(s)

    print()


# ---------- UPDATE ----------
def update_students():
    with open(file, "r") as f:
        students = json.load(f)

    for s in students:
        s["school"] = "PSHS Diliman"

    with open(file, "w") as f:
        json.dump(students, f, indent=4)

    print("Students updated with school field.\n")


# ---------- DELETE ----------
def delete_students():
    with open(file, "r") as f:
        students = json.load(f)

    filtered_students = []

    for s in students:
        color = s["favorite_color"].lower()

        if "red" not in color and "blue" not in color and "yellow" not in color:
            filtered_students.append(s)

    with open(file, "w") as f:
        json.dump(filtered_students, f, indent=4)

    print("Students with red, blue, or yellow favorite colors deleted.\n")


# ---------- RUN PROGRAM ----------