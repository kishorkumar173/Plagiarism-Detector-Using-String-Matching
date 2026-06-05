📄 Plagiarism Detector Using String Matching Algorithms

A professional plagiarism detection system built using **Data Structures & Algorithms (DSA)** concepts and **String Matching Algorithms** like **Naive Matching**, **KMP (Knuth–Morris–Pratt)**, **Rabin–Karp**, and **Jaccard Similarity**.

This project detects **exact plagiarism**, **near-duplicate text**, and **lightly modified content** using layered detection techniques and provides a **professional Streamlit dashboard UI**.

---

🚀 Live Demo

Coming Soon (After Streamlit Deployment)

```text
https://your-project-name.streamlit.app
```

---

📌 Problem Statement

Plagiarism is a major issue in:

* Academic assignments
* Research papers
* Blogs and articles
* Online content platforms
* EdTech systems

Manual plagiarism checking is:

❌ Time-consuming
❌ Inefficient
❌ Error-prone

This project automates plagiarism detection using efficient **string matching algorithms** and **similarity analysis**.

---

🎯 Project Objective

The goal of this project is to:

* Detect copied text between documents
* Identify exact and near-duplicate matches
* Calculate plagiarism percentage
* Extract matched content
* Generate plagiarism reports
* Demonstrate DSA concepts in a real-world system

---

⚙️ Features

✅ Document Upload Support (`.txt`)
✅ Text Preprocessing & Cleaning
✅ Sentence Tokenization
✅ Naive String Matching
✅ KMP Algorithm
✅ Rabin–Karp Algorithm
✅ Jaccard Similarity
✅ Exact Match Detection
✅ Near-Duplicate Detection
✅ Final Plagiarism Percentage
✅ Matched Sentence Detection
✅ Professional Streamlit UI
✅ Downloadable Report

---

🧠 Algorithms Used
 1. Naive String Matching

A brute-force string matching approach used as a baseline comparison.

**Time Complexity**

```text
O(N × M)
```

---

2. KMP (Knuth–Morris–Pratt)

Efficient pattern searching using the **LPS (Longest Prefix Suffix) array** to avoid unnecessary comparisons.

**Time Complexity**

```text
O(N + M)
```

---

3. Rabin–Karp Algorithm

Uses **hashing** and **rolling hash** for efficient string matching.

**Time Complexity**

```text
Average: O(N + M)
Worst: O(N × M)
```

---

4. Jaccard Similarity

Detects **near-duplicate content** by comparing common words between documents.

Formula:

```text
J(A,B) = |A ∩ B| / |A ∪ B|
```

---
🏗️ Project Architecture

```text
Input Documents
        ↓
Text Preprocessing
        ↓
Sentence Tokenization
        ↓
Naive Matching
        ↓
KMP Matching
        ↓
Rabin–Karp Matching
        ↓
Jaccard Similarity
        ↓
Similarity Score
        ↓
Matched Content Extraction
        ↓
Plagiarism Report
```

---

📂 Folder Structure

```text
Plagiarism-Detector-Using-String-Matching/
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── documents/
│   ├── original.txt
│   └── submitted.txt
│
├── src/
│   ├── file_handler.py
│   ├── preprocessing.py
│   ├── naive_match.py
│   ├── kmp_match.py
│   ├── rabin_karp.py
│   ├── similarity.py
│   └── report_generator.py
│
├── reports/
├── outputs/
├── images/
└── docs/
```

---

🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Streamlit
* NLTK

### Concepts Used

* String Matching
* Hashing
* Rolling Hash
* Sliding Window
* Set Operations
* Pattern Matching
* DSA Optimization

---

💻 Installation

Clone Repository

```bash
git clone https://github.com/your-username/Plagiarism-Detector-Using-String-Matching.git
```

### Move Into Project Folder

```bash
cd Plagiarism-Detector-Using-String-Matching
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

▶️ Run Project

### Run Streamlit UI

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

📊 Example Output

### Metrics

```text
Naive Score: 40%
KMP Score: 40%
Rabin–Karp Score: 40%
Jaccard Score: 72%

Final Plagiarism Score: 48%
```

---

 🖼️ Screenshots

### Home Page

(Add Screenshot)

### Upload Section

(Add Screenshot)

### Detection Results

(Add Screenshot)

### Final Plagiarism Score

(Add Screenshot)

---
🌍 Real-World Applications

This system can be used in:

* Colleges & Universities
* EdTech Platforms
* Content Publishing
* Blog Platforms
* Academic Research
* Assignment Verification Systems

---

 📈 Future Enhancements

* PDF & DOCX support
* Semantic similarity detection
* Multi-document comparison
* Database integration
* API support
* Cloud deployment
* AI-powered paraphrase detection

---

👨‍💻 Author

**Kishor Kumar L**

BE CSE (AIML) — 6th Semester

---
 ⭐ If you found this useful

Give this repository a star ⭐
