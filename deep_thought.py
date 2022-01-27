import json

with open("data.json", "r") as f:
    data = json.load(f)
    answer = data["answer"]
    question = data["question"]
    print(f"{question}: \n{answer}")
