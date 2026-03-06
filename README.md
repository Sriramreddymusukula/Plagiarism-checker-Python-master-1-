📄 Plagiarism Checker System (Text + Image OCR)

A Python-based plagiarism detection system that compares documents and images by extracting text and measuring similarity using machine learning techniques.

The system reads text files and images, extracts textual content using OCR, converts them into numerical vectors, and calculates similarity to detect possible plagiarism.

This project combines:

Tesseract OCR for extracting text from images

scikit-learn for text vectorization and similarity analysis

📌 Project Overview

Plagiarism detection is widely used in:

Academic submissions

Document verification

Content originality checking

Assignment evaluation systems

This system works by:

1️⃣ Reading text documents
2️⃣ Extracting text from images using OCR
3️⃣ Converting text into numerical vectors
4️⃣ Comparing vectors using cosine similarity
5️⃣ Reporting plagiarism percentage

⚙️ Features

✔ Detects plagiarism between text files
✔ Detects plagiarism between images and text
✔ Uses OCR to extract text from images
✔ Uses TF-IDF vectorization for feature extraction
✔ Calculates similarity using Cosine Similarity
✔ Supports multiple files simultaneously
✔ Displays plagiarism percentage and status

🧠 System Workflow
Documents / Images
        │
        ▼
Text Extraction
(TXT + OCR)
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Cosine Similarity
        │
        ▼
Plagiarism Detection
📂 Project Structure
Plagiarism-Checker
│
├── app.py
│
├── documents
│   ├── file1.txt
│   ├── file2.txt
│
├── images
│   ├── image1.png
│   ├── image2.jpg
│
└── README.md
🔧 Requirements

Install the required libraries:

pip install pytesseract pillow scikit-learn

You must also install:

Tesseract OCR

Download from:

https://github.com/UB-Mannheim/tesseract/wiki

After installing, update the path inside the script:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶️ Running the Project

Run the program using:

python app.py

The system will:

1️⃣ Load all .txt files from the documents folder
2️⃣ Extract text from images in the images folder
3️⃣ Convert all content into vectors
4️⃣ Compare documents for similarity

📊 Example Output
PLAGIARISM CHECKER SYSTEM

------------------------------------------------------------

file1.txt vs file2.txt
Similarity: 82.34%
Status: 🚨 PLAGIARISM

file1.txt vs image1.png
Similarity: 54.12%
Status: ⚠ SUSPICIOUS

file2.txt vs image2.jpg
Similarity: 21.45%
Status: ✅ SAFE
📈 Similarity Threshold
Similarity Score	Status
≥ 70%	🚨 Plagiarism
50% – 69%	⚠ Suspicious
< 50%	✅ Safe
🛠 Technologies Used

Python

Tesseract OCR

scikit-learn

Pillow

NumPy

TF-IDF Vectorization

Cosine Similarity

🚀 Future Improvements

Possible enhancements for this project:

Sentence-level plagiarism detection

PDF and DOCX file support

Web-based interface

Real-time plagiarism API

Visualization of similarity scores

Machine learning models for semantic similarity
