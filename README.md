# 🧠 Random Quiz Generator using Python

A terminal-based quiz application that randomly selects 10 questions from multiple CSV files and evaluates user responses. This lightweight quiz engine is ideal for practicing general knowledge, educational quizzes, or interview prep.

---

## 📌 Features

- 🔀 **Random Question Selection** from multiple CSV files
- 📊 **Score Calculation** based on accuracy
- 📁 **Multiple CSV Support** for diverse question pools
- 💬 **User Interaction via CLI**

---

## 🚀 Technologies Used

| Category        | Tools & Libraries |
|-----------------|------------------|
| Programming     | Python            |
| Data Handling   | pandas            |
| Randomization   | random            |
| File Handling   | csv, os           |

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ommishra03/Random_Quiz.git
   cd Random_Quiz```

2. **Install required packages**

   ```bash
   pip install pandas
   ```

---

## 📥 Input

* CSV files must contain two columns:

  * `question`
  * `answer`

**Example format:**

```csv
question,answer
What is the capital of France?,Paris
Who wrote "1984"?,George Orwell
```

---

## 🧪 Usage

1. **Update CSV paths in your script**

   ```python
   filenames = [r"path/to/file1.csv", r"path/to/file2.csv"]
   ```

2. **Run the script**

   ```bash
   python quiz_application.py
   ```

3. **Answer the quiz**

   * The app asks 10 random questions
   * You input answers one-by-one
   * Your final score is shown at the end

---

## 🧾 Example Output

```bash
Question 1: What is the capital of France?
Your answer: Paris
Question 2: Who wrote "1984"?
Your answer: George Orwell
...
Your score: 9/10
```

---

## 📚 About the Author

👨‍🎓 **Om Mishra**
📍 Third-year Student, Chandigarh University
🏆 Reliance Foundation Scholar
🧠 Mentor at Reliance Foundation (C, C++, DSA, Python)
🌐 Blockchain & AI Enthusiast (Solidity, Ethereum, React, ML)
🎮 Hackathon Finalist (NASA Space App Challenge, NITs, BITS)
📢 Rebuilt math curriculum at an ed-tech startup
🧑‍🏫 Taught merchant navy aspirants

🔗 [Connect on LinkedIn](https://www.linkedin.com/in/om-mishra-a62991289)

---

## ✨ Acknowledgements

* 🧠 `pandas` for data processing
* 🐍 Python's `random` module for question shuffling

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 📧 Contact

For suggestions, collaboration, or queries: **[ommishra1729@gmail.com](mailto:ommishra1729@gmail.com)**

```

---

Let me know if you'd like this turned into a GUI (Tkinter or Streamlit) or deployed as a web app next!
```
