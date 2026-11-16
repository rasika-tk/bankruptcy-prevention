# bankruptcy-prevention
Bankruptcy Prevention using Machine Learning and Streamlit

# Bankruptcy Prevention | Machine Learning

## Project Overview
This project focuses on predicting company bankruptcy using machine learning classification algorithms based on financial and operational risk factors.

The objective is to identify companies at risk of bankruptcy by analysing relevant features and evaluating multiple classification models.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit

## Project Workflow

1. **Data Collection:** Loaded and examined the company financial and operational dataset.
2. **Data Cleaning:** Handled duplicate records and prepared the dataset for analysis.
3. **Exploratory Data Analysis (EDA):** Analysed feature distributions, patterns and relationships.
4. **Data Preprocessing:** Prepared features and target variables for model development.
5. **Model Building:** Implemented and compared seven machine learning classification algorithms.
6. **Model Evaluation:** Evaluated models using classification metrics and cross-validation.
7. **Model Selection:** Selected Random Forest based on the evaluation results.
8. **Deployment:** Developed an interactive application using Streamlit.

## Machine Learning Models
Seven classification algorithms were implemented and compared.

**Final Selected Model:** Random Forest Classifier

## Key Outcomes
- Identified patterns associated with company bankruptcy.
- Compared the performance of multiple classification algorithms.
- Selected Random Forest based on model evaluation and cross-validation.
- Developed an interactive bankruptcy prediction application using Streamlit.

## Project Structure
```text
bankruptcy-prevention/
├── README.md
├── Project_Bankruptcy_Prevention.ipynb
├── app.py
├── Bankruptcy_prevention_Dataset.csv
├── requirements.txt
├── Bankruptcy_Prevention_Project.pptx
└── images/
    └── dashboard.png
    
```

## How to Run the Project

1. Clone this repository:
```bash
https://github.com/rasika-tk/bankruptcy-prevention.git
```

2. Install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:
```bash
streamlit run app.py
```

## Author
Data Science Project | Machine Learning
