from fastapi import FastAPI
import json
import os


app = FastAPI()

file_name = "data.txt"

@app.post("/add_data")
def add_data_to_file(add_data: dict):
    with open(file_name, "a" , encoding="utf-8") as file:
        line = json.dumps(add_data, ensure_ascii=False)
        file.write(line + "\n")

    return {"status": "saved"}

@app.get("/last_ten")
def get_last_ten_lines():
    if not os.path.exists(file_name):
        return {"last_ten" : []}
    
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    last_lines = [line.strip() for line in lines[-10:] if line.strip()]

    last_items = []
    for line in last_lines:
        try:
            last_items.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return {"last_ten": last_items}






