# HIV_drug_classification

# Project Overview
The HIV Drug Classification project aims to assist in the identification of compounds that have potential as HIV inhibitors or exhibitors. By providing a compound in SMOTE form, the machine learning model will predict whether it contains parts of HIV inhibitors or exhibitors, which is critical for drug discovery in combating HIV.

# Technologies Used
Python
Pandas
Scikit-learn
TensorFlow/Keras (or other deep learning frameworks as needed)
SMOTE (Synthetic Minority Over-sampling Technique)

# Dataset
The input dataset consists of compounds in SMOTE form. Each data point contains features extracted from the compound and is labeled either as an HIV inhibitor or exhibitor. The dataset is processed to balance the classes using SMOTE to handle class imbalance during training.

# Model Description
The machine learning model built for this project utilizes a classification algorithm to predict whether a given compound belongs to the inhibitor or exhibitor class. The project leverages techniques like:

Data preprocessing and feature extraction from SMOTE form compounds.
Classification algorithms (e.g., Random Forest, Support Vector Machines, or Neural Networks).
Evaluation metrics such as accuracy, precision, recall, and F1-score to validate the model's performance.
