# AI Chat Log Summarizer

'AI Chat Log Summarizer' is a Python-based tool that parses chat logs between a user and an AI, counts messages, extracts the top 5 keywords using TF-IDF, and generates a summary of the conversation. It supports single chat log files and multiple logs in a folder.

The code uses an object-oriented structure for modularity and extensibility, and saves summaries to text files in an output folder.

---

## Features

### ✅ Chat Log Parsing
- Separates messages by speaker (User vs. AI).
- Handles multi-line messages using the `ChatLogParser` class.
- Validates that conversations start with a `User:` message.
- If not valid then doesn't produce any summary for that file.

### ✅ Message Statistics
- Counts total messages and messages per speaker.
- Calculates exchanges as paired interactions.

### ✅ Keyword Analysis
- Extracts the top 5 keywords using **TF-IDF** via `scikit-learn`.
- Also used frequency-based extraction using NLTK as a backup.
- Excludes conversational greetings like "hi", "hello", "hey", and "greetings".
- Each file uses its **own corpus** to reflect the specific conversation.

### ✅ Summary Generation
- Produces a summary including:
  - Number of exchanges.
  - Total messages per speaker.
  - Top keywords.
  - Nature of conversation.

---

## 📂 File Handling Logic

- Checks the `chat_logs/` folder first for `.txt` files.
- If none found, checks for a single `chat.txt` file in the root directory.
- If both exist:
  - Summarizes all files with respective headlines:
    - `Summaries for Chat Logs in Folder`
    - `Summary for Single Chat Log`
- If neither exists:
  - Prints:  
    `"No .txt files were found either within the 'chat_logs' directory or in the current working directory."`
- Invalid files are excluded from the summarization process, and no summaries are generated for them. A list of all invalid files is displayed at the end of the terminal output.

---

## 📁 Output Files

- Folder summaries: `output/folder_summaries.txt`
- Single file summary: `output/single_summary.txt`
- Output folder is created automatically if it doesn’t exist.

## ⚠️ Invalid File Handling

Rejects chat logs that:
- Don’t start with a `User:` message.
- Contain no valid messages.
---

## ✅ Requirements

- Python 3.6+
- NLTK  
  `pip install nltk`
- scikit-learn  
  `pip install scikit-learn`

---

## ⚙️Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ashik1104/AI-Chat-Log-Summarizer.git
   cd ai-chat-log-summarizer

2. Create and activate a virtual environment with python=3.9 (recommended):
   ```bash
   conda create --name <venv name> python=3.9
   conda activate <venv name>

3. Install Dependencies
   ```bash
   pip install nltk scikit-learn

## 🚀 Usage

Run the script (make sure you are in the project directory and the virtual environment is activated):

```bash
python main.py
```

## 📑 Sample Chat Log(chat.txt)
```text
User: What is blockchain?
AI: Blockchain is a digital ledger that records transactions across many computers in a secure and transparent way.
User: Why is it considered secure?
AI: Because once a block is added to the chain, it’s nearly impossible to change. Each block is linked to the previous one using cryptography.
User: Is blockchain only used for cryptocurrency?
AI: No, it’s also used in supply chain management, healthcare, voting systems, and many other fields for secure data tracking.
```

## 🧾 Sample Output
```text
Summary for Single Chat Log:

        Summary for chat.txt:
        - The conversation had 3 exchanges.
        - Total messages: 6 (User: 3, AI: 3).
        - Conversation about blockchain, secure, block.
        - Most common keywords: blockchain, secure, block, chain, many.

```

## 📸 Screenshot
Displays output summaries in the terminal when multiple chat log files are present in the 'chat_logs' directory, as well as when a single chat.txt file exists in the project root directory. Invalid files, if any, are listed at the end of the output.

![Chat Log Summary Example](https://github.com/ashik1104/AI-Chat-Log-Summarizer/blob/9410afc72721a711eb308be3866e3de86165799b/Screenshot.png)


## 📁Project Structure
```text
ai-chat-log-summarizer/
│
├── main.py                        # Main script
├── the_parser.py                  # Handles parsing and validation of chat logs
├── the_extractor.py              # Extracts keywords using TF-IDF or fallback
├── the_summarizer.py             # Generates summaries using parsed data and keywords
├── chat.txt                       # Single chat log
├── chat_logs/                     # Folder for multiple logs
│   ├── chat1.txt
│   └── chat2.txt
├── output/                        # Output summaries folder
│   ├── folder_summaries.txt
│   └── single_summary.txt
└── README.md                      # Project documentation

```
