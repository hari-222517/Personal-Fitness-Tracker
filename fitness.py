import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# App Configuration
st.set_page_config(page_title="Personal Fitness Tracker", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .navbar {
            background-color: #222;
            padding: 15px;
            text-align: center;
            font-size: 18px;
            color: white;
            display: flex;
            justify-content: space-around;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 10px 15px;
            font-weight: bold;
        }
        .navbar a:hover {
            background-color: #575757;
            border-radius: 5px;
        }
        .logout-button {
            background-color: #d9534f;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            margin-top: 10px;
        }
        .logout-button:hover {
            background-color: #c9302c;
        }
        .login-box {
            background-color: #222;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 450px;
            margin: auto;
            margin-top: 50px;
        }
        .login-box input, .login-box button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
        }
        button{background-color:#4CAF50;}
    </style>
""", unsafe_allow_html=True)

# Navigation Bar at the Top
st.markdown("""
    <div class='navbar'>
        <a href='/?page=Dashboard'>Dashboard</a>
        <a href='/?page=LogWorkout'>Log Workout</a>
        <a href='/?page=LogNutrition'>Log Nutrition</a>
        <a href='/?page=ProgressReport'>Progress Report</a>
        <a href='/?page=Signup'>Sign Up</a>
        <a href='/?page=Login'>Login</a>
        <button class='logout-button' onclick='logout()'>Logout</button>
    </div>
""", unsafe_allow_html=True)

# Logout Functionality
if "logout" not in st.session_state:
    st.session_state.logout = False

def logout():
    st.session_state.logout = True
    st.experimental_rerun()

if st.session_state.logout:
    st.session_state.clear()
    st.experimental_rerun()

# Get Current Page from URL Parameter
page = st.query_params.get("page", "Dashboard")

# Login Page
if page == "Login":
    st.markdown("""
        <div class='login-box'>
            <h2 style='color: white;'>🔐 Login to Your Fitness Tracker</h2>
            <input type='text' placeholder='Username'>
            <input type='password' placeholder='Password'>
            <button>Login</button>
        </div>
    """, unsafe_allow_html=True)

# Signup Page
elif page == "Signup":
    st.markdown("""
        <div class='login-box'>
            <h2 style='color: white;'>📝 Create an Account</h2>
            <input type='text' placeholder='Username'>
            <input type='email' placeholder='Email'>
            <input type='password' placeholder='Password'>
            <input type='password' placeholder='Confirm Password'>
            <button>Sign Up</button>
        </div>
    """, unsafe_allow_html=True)


# Dashboard Page
elif page == "Dashboard":
    st.title("📊 Personal Fitness Tracker")
    st.write("Enter your details to track fitness progress.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age:", 10, 100, 25)
        bmi = st.slider("BMI:", 15, 40, 22)
        duration = st.slider("Workout Duration (min):", 0, 120, 30)

    with col2:
        heart_rate = st.slider("Heart Rate:", 60, 180, 75)
        body_temp = st.slider("Body Temperature (°C):", 36, 42, 37)
        weight=st.slider("Body Weight:", 50,100,70)
    
    gender = st.radio("Gender:", ["Male", "Female"])
    
    st.subheader("Your Fitness Summary:")
    df = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Duration": [duration],
        "Heart Rate": [heart_rate],
        "Body Temp": [body_temp],
        "Gender": [1 if gender == "Male" else 0]
    })
    st.dataframe(df)
    
    st.subheader("Health Insights:")
    st.success("This section will include AI-powered fitness insights in future updates.")

# Log Workout Page
elif page == "LogWorkout":
    st.title("🏋️ Log Your Workout")
    with st.form("workout_form"):
        date = st.date_input("Date", value=datetime.date.today())
        exercise = st.text_input("Exercise Name")
        sets = st.number_input("Sets", min_value=1, value=3)
        reps = st.number_input("Reps per Set", min_value=1, value=10)
        weight_kg = st.number_input("Weight (kg)", min_value=0.0, value=0.0)
        submitted = st.form_submit_button("Log Workout")
        
        if submitted:
            st.success("Workout logged successfully!")

# Log Nutrition Page
elif page == "LogNutrition":
    st.title("🥗 Log Your Nutrition")
    with st.form("nutrition_form"):
        date = st.date_input("Date", value=datetime.date.today())
        meal = st.text_input("Meal Description")
        calories = st.number_input("Calories", min_value=0, value=500)
        submitted = st.form_submit_button("Log Meal")
        
        if submitted:
            st.success("Meal logged successfully!")

# Progress Report Page
elif page == "ProgressReport":
    st.title("📈 Your Progress Report")
    st.write("Visualizing your fitness journey!")
    
    sample_data = pd.DataFrame({
        "Day": ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
        "Calories Burned": [200, 250, 300, 350, 400]
    })
    
    st.line_chart(sample_data.set_index("Day"))
    
    st.success("More detailed analytics coming soon!")
