import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Credit Card Default Prediction")

#Limited balance
LIMIT_BAL = st.text_input('LIMIT_BAL')


#sex
SEX = st.selectbox('SEX',['Male','Female'])

#Education
EDUCATION = st.selectbox('EDUCATION', ['graduate school' , 'university' , 'high school' , 'others' , 'unknown', 'unknown'])

#Marriage
MARRIAGE = st.selectbox('MARRIAGE', ['married', 'single' , 'others']) 

# Age
AGE = st.number_input('Age of person')

#pay

PAY_0 = st.selectbox('PAY_0',[-2,-1,1,2,3,4,5,6,7,8,9,0])
PAY_2 = st.selectbox('PAY_2',[-2,-1,1,2,3,4,5,6,7,8,9,0])
PAY_3 = st.selectbox('PAY_3',[-2,-1,1,2,3,4,5,6,7,8,9,0])
PAY_4 = st.selectbox('PAY_4',[-2,-1,1,2,3,4,5,6,7,8,9,0])
PAY_5 = st.selectbox('PAY_5',[-2,-1,1,2,3,4,5,6,7,8,9,0])
PAY_6 = st.selectbox('PAY_6',[-2,-1,1,2,3,4,5,6,7,8,9,0])

#bill
BILL_AMT1 =st.number_input('bill statement in September')
BILL_AMT2 =st.number_input('bill statement in August')
BILL_AMT3 =st.number_input('bill statement in July')
BILL_AMT4 =st.number_input('bill statement in June')
BILL_AMT5 =st.number_input('bill statement in May')
BILL_AMT6 =st.number_input('bill statement in April')


#Pay
PAY_AMT1 =st.number_input('previous payment in September')
PAY_AMT2 =st.number_input('previous payment in August')
PAY_AMT3 =st.number_input('previous payment in July')
PAY_AMT4 =st.number_input('previous payment in June')
PAY_AMT5 =st.number_input('previous payment in May')
PAY_AMT6 =st.number_input('previous payment in April')




if st.button('PREDICT CREDIT CARD DEFAULTER PAYMENT'):
    # query
    
    if SEX == 'Male':
        SEX = 1
    else:
        SEX = 2



    if EDUCATION == 'graduate school':
        EDUCATION = 1
    elif EDUCATION == 'university':
        EDUCATION = 2
    elif EDUCATION == 'high school':
        EDUCATION = 3
    elif EDUCATION == 'others':
        EDUCATION = 4
    elif EDUCATION == 'unknown':
        EDUCATION = 5
    else:
        EDUCATION =6
        

    if MARRIAGE == 'married':
        MARRIAGE = 1
    elif MARRIAGE == 'single':
        MARRIAGE = 2
    else:
        MARRIAGE = 3

    
    query1 = np.array([LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
       PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
       BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
       PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6])



    query = np.array(query1).astype(float).reshape(1,-1)
    #query = query.reshape(1,23)
    final = pipe.predict(query)

    #st.title("The predicted price of this configuration is " + final)

    print(final)

    if (final == [1]):
        st.header("The credit card holder will be Defaulter in the next month")
    else:
        st.header("The Credit card holder will not be Defaulter in the next month")



