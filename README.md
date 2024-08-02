
# Loan Prediction System 

This project involves developing a loan prediction system using machine learning techniques. The system predicts whether a loan applicant will be approved or not based on various features such as gender, marital status, income, lone amount, education, property and more.

The project consists of a Streamlit web application that allows users to input their details and receive a loan approval prediction based on a trained **Linear Discriminant Analysis (LDA) model.**


## Features

- **Home Page:** Displays the dataset and visualizations of applicant income vs. loan amount.
- **Prediction Page:** Provides an interactive form for users to input their details and get loan approval predictions.


## Used Technologies

**Python:** Programming language for data processing and machine learning.

**Streamlit:** Framework of building the web application.

**Scikit-learn:** Library for machine learning, used for model training and prediction.

**Pandas:** Library for data manipulation and analysis.

**Pickle:** Serialization library for saving and loading the trained model.

**Matplotlib/Seaborn** Libraries for data visualization.

## File Structure


- `Lone_Prediction.py` Streamlit application script that includes both home and prediction pages.

- `loan.csv` Dataset used for training and testing the model.

- `LDA_Model.pkl` Pickled Linear Discriminant Analysis model for loan prediction.

- `Lone_Prediction_ML_Model.ipynb` Python code for train the Machine Learning Model
- `requirements.txt`  List of required Python packages.
- `documentation.pdf` Development steps and streamlit link
## Data Processing

1. **Loading Data:** The dataset is loaded from `loan.csv.`

2. **Preprocessing**
- Conversion of categorical variables to numerical values.
- Handling missing values by imputation.
- Dropping irrelevant columns.

3. **Model Training**

- Various models are trained, including Linear Discriminant Analysis, Decision Trees, SVM, Logistic Regression, K- Neirest Neighbors, Naive Bayes, Random Forest Classifier.
- The best-performing model was Linear Discriminant Analysis and accurace was 0.84 and saved using Pickle.
## Model Usage

- **Training:** The Linear Discriminant Analysis (LDA) model is trained on the preprocessed data.
- **Prediction:** Users can input their details on the Streamlit app, and the LDA model predicts loan approval.
## Acknowledgements

 - [Streamlit Documentaion](https://docs.streamlit.io/)
 - [Scikit-learn Documentation](https://scikit-learn.org/stable/)
 - [Pandas Documentation](https://pandas.pydata.org/docs/)

## Streamlit URL
Visit to the [Lone Prediction System](https://lone-prediction-system.streamlit.app/)

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License

