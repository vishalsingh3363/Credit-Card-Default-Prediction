import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


query1 = np.array([120000,2,2,2,26,-1,2,0,0,0,2,2682,1725,2682,3272,3455,3261,0,1000,1000,1000,0,2000])




query = np.array(query1).astype(str).reshape(1,-1)
    #query = query.reshape(1,23)
final = pipe.predict(query)

print(final)
    
    
    
if (final == [1]):
    print("The credit card holder will be Defaulter in the next month")
else:
    print("The Credit card holder will not be Defaulter in the next month")


#st.title("The predicted price of this configuration is " + final)
