# Churn Modeling Using Logistic Regression

This repository contains a machine learning project for predicting customer churn using logistic regression. The code is organized into multiple Python files, each focused on a specific part of the workflow, including data preprocessing, feature selection, model training, and visualization. The goal is to build a model that can predict whether a customer will churn based on various features in the dataset.

## Project Structure

The project is structured into the following key files:

### 1. **`data_preprocessing.py`**
   - Contains functions for:
     - Loading the dataset from a CSV file.
     - Handling missing values and converting the `TotalCharges` column to numeric.
     - Encoding categorical variables into numerical codes.
     - Splitting the dataset into features and target variables.

### 2. **`feature_selection.py`**
   - Contains functions for:
     - Performing Chi-Square tests to identify important categorical features.
     - Applying Recursive Feature Elimination (RFE) to select the most relevant features for modeling.

### 3. **`modeling.py`**
   - Contains functions for:
     - Training a logistic regression model.
     - Evaluating the model using accuracy and confusion matrix.
     - Plotting the ROC curve for model performance evaluation.

### 4. **`visualization.py`**
   - Contains functions for:
     - Plotting count plots for categorical variables.
     - Plotting distribution plots for continuous variables.
     - Plotting a correlation matrix heatmap for continuous variables.

### 5. **`main.py`**
   - This is the entry point of the project where all the modules are imported and used.
   - It loads and preprocesses the data, performs feature selection, trains the model, and generates visualizations.

## Setup Instructions

Follow these steps to set up and run the project locally:

### Prerequisites
Ensure you have Python installed (Python 3.6+ is recommended). You will also need to install the required dependencies.

### Install Dependencies

You can install the required libraries using `pip`. It's recommended to use a virtual environment to manage dependencies.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
