import streamlit as st
import pandas as pd
from joblib import load  # For loading the saved model and encoders

# Load the saved model and label encoders
# Function to load files with error handling
def load_file(file_path):
    try:
        return load(file_path)
    except FileNotFoundError:
        st.error(f"The file '{file_path}' was not found. Please ensure it is uploaded.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading '{file_path}': {e}")
        st.stop()

# Load the saved model and label encoders
rf_model = load_file('rf_model.joblib')
label_encoders = load_file('label_encoders.joblib')

# Define categorical features (replace with actual feature names)
categorical_features = ['Academic_Level', 'Status', 'Gender', 'Payment_Method']

st.image('logo.png', width=300)
# Load CSS for custom styles
with open("styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Using markdown for the title with some decorations
st.markdown(
    """
    <h1>Customer Cluster Prediction App</h1>
    """, 
    unsafe_allow_html=True
)

st.write("Enter your information to predict your customer cluster:")

# Collect user input through Streamlit elements and perform basic validation
age = st.number_input("Enter your age:", min_value=0)  # Enforce non-negative age
educationlvl = st.selectbox("Education level:", options=["Basic", "Graduation", "Master", "PhD"])
marriedstatus = st.selectbox("Marital status:", options=["Single", "Together", "Married", "Widow", "Divorced"])
gender = st.selectbox("Gender:", options=["Male", "Female", "Other"])
payment_method = st.selectbox("Payment method:", options=["Cash", "Card", "Mobile", "Online"])
children = st.number_input("Enter the number of children:", min_value=0)
totalspent = st.number_input("Enter your total spent amount:", min_value=0)

# Create a dictionary with user-provided data
user_data = {
    'Age': age,
    'Academic_Level': educationlvl,
    'Status': marriedstatus,
    'Gender': gender,
    'Payment_Method': payment_method,
    'Children': children,
    'TotalSpent': totalspent
}

# Convert the dictionary to a DataFrame
user_df = pd.DataFrame([user_data])

# Encode the categorical features using the loaded label encoders
for feature in categorical_features:
    le = label_encoders[feature]
    user_df[feature] = le.transform(user_df[feature])

# Display prediction button
if st.button("Predict Cluster"):
    # Predict the cluster
    try:
        cluster_pred = rf_model.predict(user_df)
        predicted_cluster = cluster_pred[0]  # Get the predicted cluster
        st.success(f"The user belongs to Cluster {predicted_cluster}")
    except ValueError as e:
        st.error(f"Error in prediction: {e}")