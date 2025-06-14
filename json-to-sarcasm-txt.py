import json

input_path = "data/Sarcasm_Headlines_Dataset_v2.json"
output_path = "data/sarcasm.txt"

with open(input_path, "r") as f, open(output_path, "w") as out:
    for line in f:
        try:
            obj = json.loads(line)
            if obj.get("is_sarcastic") == 1:
                out.write(obj["headline"].strip() + "\n")
        except json.JSONDecodeError:
            continue  # Skip malformed lines

