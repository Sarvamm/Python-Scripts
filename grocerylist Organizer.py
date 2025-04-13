import ollama
import os

model="hf.co/mradermacher/DeepSeek-R1-Distill-Qwen-7B-Uncensored-i1-GGUF:Q4_K_M";

inputf = r"C:\Users\Sarvamm\Documents\Codes\Python\My Projects\Ollama\list.txt"
outputf = "edited_list.txt";

if not os.path.exists(inputf):
    print(f"Input file {inputf} does not exist!")
    exit(1)

with open(inputf, "r") as f:
    items = f.read().strip()

prompt = f"""
You are an assistant that categorises and sorts grocery items.

Here is a list of grocery items:

{items}

Please :
1. Categorise these items into categories.
2. Sort the items in each category in alphabetical order.
3. Present in a organized manner
"""

try:
    res = ollama.generate(model = model, prompt=prompt)
    updated_list = res.get("response", "")

    with open(outputf, "w") as f:
        f.write(updated_list)
    print(f"Output saved to {outputf}")
except Exception as e:
    print(f"Error: {e}")
    exit(1)



