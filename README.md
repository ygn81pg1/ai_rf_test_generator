# AI-Powered Robot Framework Test Case Generator

This project provides an **offline AI-powered assistant** to generate Bosch-formatted Robot Framework test cases from natural language prompts. It fine-tunes an open-source LLM (e.g., LLaMA 3) with example Bosch test cases and then produces `.robot` files that follow strict naming, tagging, and documentation conventions.

---

## 📂 Repository Structure
```
ai-rf-test-generator/
│
├── src/
│   ├── prepare_data.py       # Convert .robot files → JSONL dataset for training
│   ├── train.py              # Fine-tune LLM with LoRA (unsloth/transformers)
│   ├── infer_with_model.py   # Generate test cases from natural language prompts
│   ├── export_gguf.py        # Export trained models to GGUF format
│
├── data/                     # Place your .robot files and generated datasets here
├── outputs/                  # Generated test cases (.robot)
├── requirements_from_notebook.txt
├── README.md                 # This file
└── RUN_GUIDE_extracted_scripts.txt
```

---

## ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/ai-rf-test-generator.git
   cd ai-rf-test-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements_from_notebook.txt
   ```

3. (Optional) Install GPU-enabled libraries (CUDA/ROCm) for faster training.

---

## 🧩 Workflow

### 1. Prepare Training Data
Place your existing `.robot` test cases under `data/robot_files/`.

Run preprocessing:
```bash
python src/prepare_data.py \
    --input_dir data/robot_files \
    --output_file data/robot_framework_finetune_dataset.jsonl \
    --use_tokens
```
This creates a JSONL dataset compatible with fine-tuning.

---

### 2. Train Model
Fine-tune an open-source LLM (e.g., `unsloth/llama-3-8b-instruct`):
```bash
python src/train.py \
    --dataset data/robot_framework_finetune_dataset.jsonl \
    --model_name unsloth/llama-3-8b-instruct \
    --output_dir model_out \
    --load_in_4bit
```

Training outputs will be saved in `model_out/`.

---

### 3. Export to GGUF (Optional)
To run inference in lightweight environments (e.g., llama.cpp):
```bash
python src/export_gguf.py \
    --model_dir model_out \
    --out_dir model_gguf
```

---

### 4. Generate Test Cases (Inference)
Run the trained model to generate `.robot` tests:
```bash
python src/infer_with_model.py \
    --prompt "Check on general voltage reading" \
    --model_path model_gguf \
    --out_dir outputs \
    --load_in_4bit
```

This produces a file like:
```
outputs/DEMO_Generated_Voltage.robot
```

---

## ✅ Benefits
- Runs **completely offline** (no cloud)
- Ensures **Bosch-specific formatting** ([Tags], [Documentation], naming rules)
- **Reduces tester workload**: write intent in English → get ready-to-run `.robot`
- Extensible to **more modules** beyond Power/Diagnostics

---

## 🚀 Next Steps
- Add a simple GUI for non-technical testers
- Train on larger and more diverse Bosch test suites
- Auto-correct or suggest improvements for invalid prompts

---

## 🙏 Acknowledgments
- Bosch test engineers (domain expertise)
- Open-source LLM community (LLaMA, HuggingFace, unsloth, llama.cpp)
