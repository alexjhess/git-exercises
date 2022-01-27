import json

# Open file
with open("data.json", "r") as f:
    # Load json
    data = json.load(f)
    answer = data["answer"]
    question = data["question"]
    print(f"{question}: \n{answer}")
