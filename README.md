🚀 Log Classification with Hybrid Framework

This project implements a powerful Hybrid Log Classification System combining multiple advanced techniques to ensure accurate log classification across varying complexity levels. The system effectively handles predictable patterns, complex data, and poorly-labeled logs using a strategic combination of methods.

🧠 Classification Approaches

✅ Regular Expression (Regex)

Efficiently classifies predictable and structured log patterns.

Ideal for handling simple patterns with predefined rules.

🔍 Sentence Transformer + Logistic Regression

Handles complex patterns when sufficient labeled data is available.

Leverages Sentence Transformers for embedding generation and Logistic Regression as the classifier.

🤖 Large Language Model (LLM)

Efficient for complex patterns with limited labeled data.

Utilizes the powerful DeepSeek-R1-Distill-LLaMA-70B model for enhanced performance.

📂 Folder Structure
├── training/
│   ├── processor_bert.py
│   ├── processor_llm.py
│   ├── processor_regex.py
│   └── models/
│       └── (Saved models: Sentence Transformer, Logistic Regression)
│
├── resources/
│   ├── Sample CSV files (for testing)
│   ├── Output files (classified results)
│   └── Screenshots (demonstrating results)
│
├── classify.py
├── server.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Setup Instructions

1. Install Dependencies

Ensure Python is installed, then run:
pip install -r requirements.txt

Step 2: Run the Streamlit App
streamlit run server.py

📊 Usage Instructions

Upload a CSV file containing log data to the FastAPI endpoint for classification.

Ensure the file has the following columns:

source

log_message

The system will generate a CSV file with an additional column:

target_label — The predicted label for each log entry.

🖥️ Demo Screenshot
![Screenshot 2025-03-12 at 8 51 30 PM](https://github.com/user-attachments/assets/d840fbcf-a5dc-4efa-a46e-1b21949d59e3)

🔬 Models Used

BERT for deep contextual understanding of log data.

Clustering Algorithm for identifying log group patterns.

DeepSeek-R1-Distill-LLaMA-70B for improved generalization in low-data scenarios.

📈 Key Achievements

✅ Successfully combines multiple classification techniques for improved accuracy.
✅ Demonstrates strong adaptability across predictable, complex, and noisy log data.
✅ Scalable and efficient implementation to handle large log datasets.
