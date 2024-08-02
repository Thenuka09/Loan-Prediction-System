import streamlit as st
from PIL import Image
import pandas as pd
import pickle

model = pickle.load(open('LDA_Model.pkl','rb'))

app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])

if app_mode == 'Home':
    st.title('LOAN PREDICTION :')
    st.image('loan_image.jpg')
    st.markdown('Dataset :')
    data = pd.read_csv('loan.csv')
    st.write(data.head())
    st.markdown('Applicant Income VS Loan Amount ')
    st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))

elif app_mode == 'Prediction':
    def run():
        img = Image.open('slider-short-3.jpg')
        st.title("Predict Your Status of Bank Loan")

        fullName = st.text_input("Your Full Name")

        gender_display = ('Male','Female')
        gender_options = list(range(len(gender_display)))
        Gender = st.selectbox("Gender", gender_options, format_func=lambda x: gender_display[x])

        marriage_display = ('Yes','No')
        marriage_options = list(range(len(marriage_display)))
        Married = st.selectbox("Marriage", marriage_options, format_func=lambda x: marriage_display[x])

        dependency_display = ('No','One', 'Two', 'More than Two')
        dependency_options = list(range(len(dependency_display)))
        Dependents = st.selectbox("Dependencies", dependency_options, format_func=lambda x: dependency_display[x])

        education_display = ('Graduate','Not Graduate')
        education_options = list(range(len(education_display)))
        Education = st.selectbox("Education", education_options, format_func=lambda x: education_display[x])

        selfEmployee_display = ('Yes','No')
        selfEmployee_options = list(range(len(selfEmployee_display)))
        Self_Employed = st.selectbox("Self-Employed", selfEmployee_options, format_func=lambda x: selfEmployee_display[x])

        property_display = ('Rural','Semi-Urban','Urban')
        property_options = list(range(len(property_display)))
        Property_Area = st.selectbox("Property Area", property_options, format_func=lambda x: property_display[x])

        credit_display = ('Yes','No')
        credit_options = list(range(len(credit_display)))
        Credit_History = st.selectbox("Credit History", credit_options, format_func=lambda x: credit_display[x])

        ApplicantIncome = st.number_input("Applicant's Monthly Income($)", value=0)

        CoapplicantIncome = st.number_input("Co-Applicant's Monthly Income($)", value=0)

        LoanAmount = st.number_input("Loan Amount", value=0)

        duration_display = ['2 months', '6 months', '8 months', '1 year', '16 months']
        duration_options = list(range(len(duration_display)))
        Loan_Amount_Terms = st.selectbox("Loan Duration", duration_options, format_func=lambda x: duration_display[x])

        if st.button("Predict"):
            Loan_Amount_Term = 0
            if Loan_Amount_Terms == 0:
                Loan_Amount_Term = 60
            elif Loan_Amount_Terms == 1:
                Loan_Amount_Term = 180
            elif Loan_Amount_Terms == 2:
                Loan_Amount_Term = 240
            elif Loan_Amount_Terms == 3:
                Loan_Amount_Term = 360
            elif Loan_Amount_Terms == 4:
                Loan_Amount_Term = 480

            features = pd.DataFrame([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome , LoanAmount,Loan_Amount_Term, Credit_History,Property_Area]],
                                    columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome' , 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'])
            print(features)

            prediction = model.predict(features)
            lc = [str(i) for i in prediction]
            ans = int("".join(lc))

            if ans == 0:
                st.error("Hello! " + fullName + " You cannot get a loan, sorry.")
            else:
                st.success("Hello! " + fullName + " Congratulations! You can get a loan.")
    run()
