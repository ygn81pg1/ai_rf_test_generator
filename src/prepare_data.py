import json

# Upload .robot files
uploaded = files.upload()

# --- Helpers ---
def extract_test_case_section(content):
    lines = content.splitlines()
    test_case_lines = []
    inside_test_section = False
    for line in lines:
        if line.strip().startswith("*** Test Cases ***"):
            inside_test_section = True
            continue
        if inside_test_section:
            if line.strip().startswith("***"):
                break
            test_case_lines.append(line.rstrip())
    return test_case_lines

def extract_structured_test_cases(lines):
    test_cases = []
    current_case = None
    for line in lines:
        if not line.strip():
            continue
        if not line.startswith(" ") and not line.startswith("#"):
            if current_case:
                test_cases.append(current_case)
            current_case = {"name": line.strip(), "body": [], "doc": ""}
        elif current_case:
            current_case["body"].append(line.rstrip())
            if "[Documentation]" in line:
                doc_text = line.split("[Documentation]")[-1].strip()
                if doc_text.startswith("..."):
                    doc_text = doc_text[3:].strip()
                current_case["doc"] = doc_text
    if current_case:
        test_cases.append(current_case)
    return test_cases

def to_finetune_format(test_cases):
    dataset = []
    for case in test_cases:
        # Build instruction more intelligently
        instruction = case["doc"].strip() if case["doc"] else f"Create a Robot Framework test case for: {case['name']}"

        # Build output: full test case block
        output_lines = ["*** Test Cases ***", case["name"]] + case["body"]
        output = "\n".join(output_lines)

        dataset.append({
            "text": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{instruction}\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n{output}\n<|eot_id|>"
        })
    return dataset

# --- Main Processing ---
all_test_cases = []

for filename in uploaded:
    content = uploaded[filename].decode("utf-8")
    test_case_lines = extract_test_case_section(content)
    structured = extract_structured_test_cases(test_case_lines)
    all_test_cases.extend(structured)

# Convert to Unsloth-compatible format
finetune_data = to_finetune_format(all_test_cases)

# Save as JSONL for training
output_file = "robot_framework_finetune_dataset.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for item in finetune_data:
        f.write(json.dumps(item) + "\n")

# Download
files.download(output_file)
