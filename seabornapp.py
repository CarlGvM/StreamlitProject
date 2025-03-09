import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import random
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

conn = st.connection("gsheets", type = GSheetsConnection)

df = conn.read(spreadsheet = "https://docs.google.com/spreadsheets/d/1ThK1QNFalgtDpkvoee_3d8Lx3o8eEiG6ZF1f1gJQiyQ/edit?usp=sharing")


st.title("Which year had the most natural disasters, based ont the data?")
st.markdown("Press the button to see the graph")
st.write("###Data from google Sheets")
st.dataframe(df)



#session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "chart_shown" not in st.session_state:
    st.session_state.chart_shown = False
    
button1 = st.button("Show Graph")   

if button1:
    st.session_state.chart_shown = True
    st.session_state.start_time = time.time()
    
    selected_chart = random.choice(["bar", "line"])
    plt.figure(figsize=(10, 5))
    if selected_chart == "bar":
        sns.barplot(data=df, x="Year", y="Deaths", color="blue")
        plt.title("Total Deaths from Natural Disasters Per Year (Bar Chart)")
    else:
        sns.lineplot(data=df, x="Year", y="Deaths", marker="o", color="red")
        plt.title("Total Deaths from Natural Disasters Per Year (Line Chart)")

    plt.xlabel("Year")
    plt.ylabel("Deaths")
    st.pyplot(plt)

 # Show second button after graph is displayed
if st.session_state.chart_shown:
     button2 = st.button("I answered your question")

     if button2:
        elapsed_time = time.time() - st.session_state.start_time
        st.write(f"⏳ You took {elapsed_time:.2f} seconds to answer!")

