# 🚀 DAY 6: FILE HANDLING + PERSISTENT STORAGE

Today is a HUGE milestone.

Right now your data disappears when program closes.

Today you’ll learn how to:

* save data permanently,
* read files,
* write files,
* work with JSON,
* build persistent systems.

This is foundational for:

* AI datasets,
* ML pipelines,
* databases,
* APIs.

---

# 🧠 1. Reading Files

```python id="z8u91d"
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# 🧠 2. Writing Files

```python id="bgb8n7"
file = open("data.txt", "w")

file.write("Hello Divya")

file.close()
```

⚠️ `"w"` overwrites file.

---

# 🧠 3. Append Mode

```python id="4pv9k7"
file = open("data.txt", "a")

file.write("\nNew line")

file.close()
```

---

# ✅ Better Method (`with open`) — IMPORTANT

```python id="1qxmu6"
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

Automatically closes file.

Professional way.

---

# 🧠 4. JSON (VERY IMPORTANT FOR AI)

AI systems heavily use JSON.

Example:

```python id="uvlypm"
{
    "name": "Divya",
    "age": 25
}
```

---

# 🧠 Save JSON

```python id="x4v0d7"
import json

data = {
    "name": "Divya",
    "age": 25
}

with open("user.json", "w") as file:
    json.dump(data, file)
```

---

# 🧠 Read JSON

```python id="1qx8ol"
import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data)
```

---

# 🧪 DAY 6 PROJECTS

---

# 🟢 1. Persistent Contact Book

Store contacts in:

```id="5dg6x4"
contacts.json
```

Features:

* add contact
* view contacts
* search contact
* delete contact

---

# 🟢 2. Expense Tracker with JSON

Save all records permanently.

---

# 🟢 3. Student Database System

Store students in JSON file.

---

# 🧪 PRACTICE TASKS

---

## 🔹 1. Count words in text file

---

## 🔹 2. Find longest word in file

---

## 🔹 3. Read CSV-like data

Example file:

```id="7prkxv"
name,marks
Divya,90
John,80
```

Parse manually.

---

# 🔥 CHALLENGE PROJECT

Build:

# 🟣 JSON-Based Mini Database

Features:

* persistent storage
* CRUD operations
* search
* update
* delete

---

# ❓ QUICK TEST

1. Difference between `"w"` and `"a"`?
2. Why use `with open()`?
3. What is JSON?
4. Why JSON is important in AI?

---

# 🎯 YOUR MISSION

Convert one of your existing systems into:
✅ persistent JSON-based storage.

This is a BIG step toward real backend engineering.

Then reply:
**"Day 6 submission"**

After that:
🔥 Error Handling + OOP + Real Engineering Patterns.
