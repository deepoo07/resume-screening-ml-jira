# Resume Screening using Machine Learning

## Project Demo

A short walkthrough of the project is available here:

## Overview
This project focuses on building a machine learning model to automatically classify resumes into different job categories. The goal is to simulate a real-world resume screening system using natural language processing (NLP) techniques.

The project includes end-to-end steps such as data preprocessing, feature extraction, model training, evaluation, and deployment using a reusable prediction script.

---

## Problem Statement
Manual resume screening is time-consuming and inefficient. This project aims to automate the classification of resumes into predefined categories using machine learning techniques.

---

## Dataset
The dataset contains resumes categorized into multiple job domains such as:
- Information Technology
- HR
- Finance
- Engineering
- Sales
- Healthcare
- And others

Each resume is provided as raw text and labeled with a category.

---

## Approach

### 1. Data Preprocessing
- Removed HTML tags and special characters
- Converted text to lowercase
- Removed unnecessary whitespace
- Cleaned resume text for modeling

### 2. Feature Engineering
- Applied TF-IDF vectorization
- Used n-grams (unigrams + bigrams)
- Limited vocabulary size using max_features
- Removed rare and overly frequent terms

### 3. Model Building
- Used Logistic Regression for classification
- Applied class balancing to handle imbalanced dataset

### 4. Evaluation
- Evaluated using:
  - Accuracy
  - Precision, Recall, F1-score
  - Confusion Matrix

### 5. Prediction System
- Saved trained model using pickle
- Built a reusable prediction script to classify new resume text
- Added confidence score to assess prediction reliability

---

## Exploratory Data Analysis (EDA)

- Category distribution shows moderate class imbalance
- Certain categories (e.g., BPO, Automobile, Agriculture) have fewer samples
- Resume lengths follow a right-skewed distribution with some long-text outliers

---

## Results

- Accuracy: ~66%
- Weighted F1 Score: ~0.66
- Macro F1 Score: ~0.61

The model performs well on categories with sufficient data and distinct keywords, while performance drops for underrepresented or overlapping categories.

---

## Key Insights

- Class imbalance significantly affects model performance
- Overlapping vocabulary across domains leads to misclassification
- TF-IDF captures word frequency but not semantic meaning
- Model performs better on keyword-rich resumes than short or generic inputs
- Low confidence scores indicate uncertain predictions for unseen or ambiguous inputs

---

## Limitations

- Lack of dedicated categories for roles like Data Analyst/Data Scientist
- Imbalanced dataset across categories
- TF-IDF does not capture contextual meaning
- Model may misclassify similar job roles due to overlapping terms

---

## Recommendations

- Collect more data for underrepresented categories
- Use advanced NLP models such as Word2Vec or BERT
- Merge overlapping categories to improve classification clarity
- Enhance preprocessing with lemmatization and domain-specific features
- Introduce confidence thresholding for reliable predictions
- Deploy the model as a web application for real-world use

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- NLTK

---

## Project Structure
Resume-Screening-ML/
│
├── Resume_Screening_ML.ipynb
├── predict.py
├── resume_model.pkl
├── tfidf_vectorizer.pkl
├── data/
└── README.md

---

## How to Run

1. Train the model using the notebook
2. Run prediction script:

3. Enter resume text to get predicted category

---

## Future Scope

- Deploy using Streamlit or Flask
- Integrate with real resume parsing systems
- Improve accuracy using deep learning models

---

## Author
Deepanti Poonekar
