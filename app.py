import os
import pytesseract
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# path configuration
TEXT_FOLDER = "documents"
IMAGE_FOLDER = "images"

# OCR setup (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ---------- READ TEXT FILES ----------

def read_text_files():

    student_files = []
    student_notes = []

    for file in os.listdir(TEXT_FOLDER):

        if file.endswith(".txt"):

            path = os.path.join(TEXT_FOLDER, file)

            with open(path, encoding="utf-8") as f:
                text = f.read()

            student_files.append(file)
            student_notes.append(text)

    return student_files, student_notes


# ---------- READ IMAGE FILES ----------

def read_image_files():

    image_files = []
    image_texts = []

    for file in os.listdir(IMAGE_FOLDER):

        if file.endswith((".png", ".jpg", ".jpeg")):

            path = os.path.join(IMAGE_FOLDER, file)

            img = Image.open(path)
            text = pytesseract.image_to_string(img)

            image_files.append(file)
            image_texts.append(text)

    return image_files, image_texts


# ---------- VECTORIZE ----------

def vectorize(text):

    return TfidfVectorizer().fit_transform(text).toarray()


# ---------- SIMILARITY ----------

def similarity(doc1, doc2):

    return cosine_similarity([doc1, doc2])[0][1]


# ---------- PLAGIARISM CHECK ----------

def check_plagiarism(files, vectors):

    s_vectors = list(zip(files, vectors))

    plagiarism_results = set()

    for student_a, text_vector_a in s_vectors:

        new_vectors = s_vectors.copy()

        current_index = new_vectors.index((student_a, text_vector_a))

        del new_vectors[current_index]

        for student_b, text_vector_b in new_vectors:

            sim_score = similarity(text_vector_a, text_vector_b)

            student_pair = sorted((student_a, student_b))

            score = (student_pair[0], student_pair[1], sim_score)

            plagiarism_results.add(score)

    return plagiarism_results


# ---------- MAIN ----------

def main():

    print("\nPLAGIARISM CHECKER SYSTEM\n")

    text_files, text_data = read_text_files()

    image_files, image_data = read_image_files()

    all_files = text_files + image_files
    all_text = text_data + image_data

    vectors = vectorize(all_text)

    results = check_plagiarism(all_files, vectors)

    print("-" * 60)

    for file1, file2, score in results:

        percent = score * 100

        if score >= 0.7:
            status = "🚨 PLAGIARISM"
        elif score >= 0.5:
            status = "⚠ SUSPICIOUS"
        else:
            status = "✅ SAFE"

        print(f"{file1}  vs  {file2}")
        print(f"Similarity: {percent:.2f}%")
        print(f"Status: {status}")
        print("-" * 60)


if __name__ == "__main__":
    main()
