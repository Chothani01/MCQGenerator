# MCQGenerator

A Python-based tool to generate multiple-choice quizzes (MCQs) from input text using language models.

---

## ✨ Features

- Generates quizzes by processing input text and desired quiz parameters.  
- Supports adjustable number of questions, subject focus, and tone (difficulty level).  
- Designed for use in educational contexts such as classroom assistance or automated quiz creation.  
- Streamlit-powered web app for interactive quiz generation.  

---

## 🚀 Getting Started

### ✅ Prerequisites

You’ll need:

- Python 3.8+  
- Dependencies listed in `requirements.txt`

Install them with:

```bash
pip install -r requirements.txt
```

## ⚙️ Environment Setup

- You must create a .env file in the project root to store your model API keys.

## 📂 Project Structure
```
MCQGenerator/
│
├── src/                      # Core code for quiz generation
│   ├── main.py               # Main script for running quiz generation
│   └── utils/                # Helper/utility functions
│
├── streamlitApp.py           # Interactive Streamlit app
├── data.txt                  # Sample input data for quizzes
├── response.json             # Example output from the quiz generator
├── requirements.txt          # Python dependencies
├── setup.py                  # For packaging/installing the tool
├── .env                      # Stores API keys (ignored by git)
└── README.md                 # Project documentation
```
