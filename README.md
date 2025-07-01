# Fake News Detector

This is me trying out my machine learning knowledge and technical skill. My fake news detector app is a machine learning web application that predicts whether a news article is **Real** or **Fake**, using natural language processing (NLP) techniques.

This was built with **Python**, **scikit-learn**, **NLTK**, and **Streamlit**.

---

## The work behind the scene

1.  **Data Cleaning**
    - Checks for missing text and remove them accordingly
    - Checks for duplicate and drop them accordingly

2.  **Text Preprocessing**
    - Add a column that labels fake news article 0 and real news article 1
    - Combines both fake and real news article to have them in a table
    - Combines title and body of article so model can have enough text to learn from
    - Shuffle data by rows to have a spread among text because after combination the text data is stacked on each other
    - Creates a clean_text function that handles lowercasing, punctuation removal, tokenization, stopword removal

3.  **Feature Engineering**
    - Uses TF-IDF vectorizer to convert text to numerical vectors for algorithm understanding

4.  **Model**
    - Trained using Logistic Regression Algorithm

5.  **Prediction**
    - App predicts/classify whether an inputed news article is Real or Fake