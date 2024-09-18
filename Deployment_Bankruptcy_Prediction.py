import streamlit as st
import numpy as np
import pickle

# Load the trained model

with open(r"C:\Users\Amirtha\Desktop\Final\Bankruptcy_prediction.sav", 'rb') as f:
    loaded_model = pickle.load(f)

def predict_bankruptcy(input_data):
    # Reshape input data
    input_data_reshaped = np.asarray(input_data).reshape(1, -1)
    # Predict
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    st.title("Bankruptcy Prediction")

    # Input fields
    st.header("Enter Financial Data")
    col1, col2, col3, col4 = st.columns(4)
    input_data = {}
    with col1:
        input_data['Net Value Growth Rate'] = st.number_input('Net Value Growth Rate', step=0.1)
        input_data['Long-term fund suitability ratio (A)'] = st.number_input('Long-term fund suitability ratio (A)', step=0.1)
        input_data['Fixed Assets Turnover Frequency'] = st.number_input('Fixed Assets Turnover Frequency', step=0.1)
        input_data['Cash/Current Liability'] = st.number_input('Cash/Current Liability', step=0.1)
        input_data['Long-term Liability to Current Assets'] = st.number_input('Long-term Liability to Current Assets', step=0.1)
        input_data['Cash Flow to Sales'] = st.number_input('Cash Flow to Sales', step=0.1)
        input_data['Current Liability to Current Assets'] = st.number_input('Current Liability to Current Assets', step=0.1)
        input_data['Degree of Financial Leverage (DFL)'] = st.number_input('Degree of Financial Leverage (DFL)', step=0.1)
        


    with col2:
        input_data['Quick Ratio'] = st.number_input('Quick Ratio', step=0.1)
        input_data['Borrowing dependency'] = st.number_input('Borrowing dependency', step=0.1)
        input_data['Net Worth Turnover Rate (times)'] = st.number_input('Net Worth Turnover Rate (times)', step=0.1)
        input_data['Current Liability to Assets'] = st.number_input('Current Liability to Assets', step=0.1)
        input_data['Total expense/Assets'] = st.number_input('Total expense/Assets', step=0.1)
        input_data['Fixed Assets to Assets'] = st.number_input('Fixed Assets to Assets', step=0.1)
        input_data['Liability-Assets Flag'] = st.number_input('Liability-Assets Flag', step=0.1)
        
        
        

    with col3:
        input_data['Total debt/Total net worth'] = st.number_input('Total debt/Total net worth', step=0.1)
        input_data['Contingent liabilities/Net worth'] = st.number_input('Contingent liabilities/Net worth', step=0.1)
        input_data['Revenue per person'] = st.number_input('Revenue per person', step=0.1)
        input_data['Inventory/Current Liability'] = st.number_input('Inventory/Current Liability', step=0.1)
        input_data['Current Asset Turnover Rate'] = st.number_input('Current Asset Turnover Rate', step=0.1)
        input_data['Current Liability to Equity'] = st.number_input('Current Liability to Equity', step=0.1)
        input_data['Total assets to GNP price'] = st.number_input('Total assets to GNP price', step=0.1)

    with col4:
        input_data['Debt ratio %'] = st.number_input('Debt ratio %', step=0.1)
        input_data['Inventory and accounts receivable/Net value'] = st.number_input('Inventory and accounts receivable/Net value', step=0.1)
        input_data['Allocation rate per person'] = st.number_input('Allocation rate per person', step=0.1)
        input_data['Current Liabilities/Equity'] = st.number_input('Current Liabilities/Equity', step=0.1)
        input_data['Quick Asset Turnover Rate'] = st.number_input('Quick Asset Turnover Rate', step=0.1)
        input_data['Equity to Long-term Liability'] = st.number_input('Equity to Long-term Liability', step=0.1)
        input_data['Liability to Equity'] = st.number_input('Liability to Equity', step=0.1)



    # Prediction
    if st.button("Predict"):
        prediction = predict_bankruptcy(list(input_data.values()))
        if prediction[0] == 0:
            st.write('As per the financial data provided there is no Bankruptcy !!')
        else:
            st.write('As per the financial data provided there is Bankruptcy !!')

if __name__ == "__main__":
    main()
