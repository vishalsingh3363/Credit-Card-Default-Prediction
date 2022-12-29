import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


def predict_default(features):

    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return prediction, probability


def main():

    html_temp = """
        <div style = "background-color: #4f8bf9; padding: 10px;">
            <center><h1>CREDIT CARD DEFAULT PREDICTION</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    LIMIT_BAL = st.text_input("Limited Balance (in New Taiwanese (NT) dollar)")

    sex_status= ["Male","Female"]
    education_status = ["graduate school", "university", "high school", "others"]
    marital_status = ["Married","single", "others"]

     
    SEX = sex_status.index(st.selectbox(
        "Sex",
        tuple(sex_status)
    )) + 1


    EDUCATION = education_status.index(st.selectbox(
        "Select Education",
        tuple(education_status)
    )) + 1

    
    MARRIAGE = marital_status.index(st.selectbox(
        "Marital Status",
        tuple(marital_status)
    )) + 1
    
    AGE = st.text_input("Age (in Years)")


    PAY_0 = st.selectbox('PAY_0',[-2,-1,1,2,3,4,5,6,7,8,9,0])
    PAY_2 = st.selectbox('PAY_2',[-2,-1,1,2,3,4,5,6,7,8,9,0])
    PAY_3 = st.selectbox('PAY_3',[-2,-1,1,2,3,4,5,6,7,8,9,0])
    PAY_4 = st.selectbox('PAY_4',[-2,-1,1,2,3,4,5,6,7,8,9,0])
    PAY_5 = st.selectbox('PAY_5',[-2,-1,1,2,3,4,5,6,7,8,9,0])
    PAY_6 = st.selectbox('PAY_6',[-2,-1,1,2,3,4,5,6,7,8,9,0])




    BILL_AMT1 = st.text_input("Last month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT2 = st.text_input("Last 2nd month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT3 = st.text_input("Last 3rd month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT4 = st.text_input("Last 4th month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT5 = st.text_input("Last 5th month Bill Amount (in New Taiwanese (NT) dollar)")
    BILL_AMT6 = st.text_input("Last 6th month Bill Amount (in New Taiwanese (NT) dollar)")

    PAY_AMT1 = st.text_input("Amount paid in Last Month (in New Taiwanese (NT) dollar)")
    PAY_AMT2 = st.text_input("Amount paid in Last 2nd month (in New Taiwanese (NT) dollar)")
    PAY_AMT3 = st.text_input("Amount paid in Last 3rd month (in New Taiwanese (NT) dollar)")
    PAY_AMT4 = st.text_input("Amount paid in Last 4th month (in New Taiwanese (NT) dollar)")
    PAY_AMT5 = st.text_input("Amount paid in Last 5th month (in New Taiwanese (NT) dollar)")
    PAY_AMT6 = st.text_input("Amount paid in Last 6th month (in New Taiwanese (NT) dollar)")

    if st.button("Predict"):
        
        features = [LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
       PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
       BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
       PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]

        prediction, probability = predict_default(features)
        # print(prediction)
        # print(probability[:,1][0])
        if prediction[0] == 1:
            # counselling_html = """
            #     <div style = "background-color: #f8d7da; font-weight:bold;padding:10px;border-radius:7px;">
            #         <p style = 'color: #721c24;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
            #     </div>
            # """
            # st.markdown(counselling_html, unsafe_allow_html=True)

            st.success("This account will be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))

        else:
            st.success("This account will not be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))

    html_temp = """
           <div style = "padding: 10px;">
               <center><h2>Made by-</h2>
               <b><i>VISHAL SINGH</i><b></center>
           </div><br>
       """
    st.markdown(html_temp, unsafe_allow_html=True)



if __name__ == '__main__':
    main()