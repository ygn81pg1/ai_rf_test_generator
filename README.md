# AI-Powered Robot Framework Test Case Generator

This project provides an **offline AI-powered assistant** to generate Bosch-formatted Robot Framework test cases from natural language prompts. It fine-tunes an open-source LLM (e.g., LLaMA 3) with example Bosch test cases and then produces `.robot` files that follow strict naming, tagging, and documentation conventions.

## Fine-Tuning LLaMA 3 (8B) with LoRA on Custom Dataset

This repository contains a step-by-step tutorial and implementation for fine-tuning the LLaMA 3 (8B) model using LoRA (Low-Rank Adaptation). The tutorial is written in a teaching style, with clear explanations for each phase of the pipeline—from setup to exporting models for deployment.

### 📚 Overview

The notebook in this repo guides you through:

1) Environment Setup – Installing required libraries (Hugging Face Transformers, PEFT, BitsAndBytes, etc.).

2) Model & LoRA Configuration – Loading LLaMA 3.2 1B with quantization and applying LoRA adapters.

3) Dataset Preparation – Building a dataset from Robot Framework test cases or any text dataset.

4) Training with LoRA – Using Hugging Face Trainer with efficient LoRA fine-tuning.

5) Saving & Exporting – Saving the fine-tuned model and pushing it to Hugging Face Hub.

6) Optional Deployment Formats – Exporting to GGUF format for llama.cpp or other lightweight inference frameworks.

### 🛠️ Prerequisites

Python 3.10+

GPU with CUDA support (NVIDIA GPU recommended)

Hugging Face account (for pushing to hub)
