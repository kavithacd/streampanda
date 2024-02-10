import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
#from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Sales Analysis App",
    page_icon=Image.open('SharkTank_Dashboard/streampanda.png'),
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define styles for the app
styles = """
<style>
img {
    max-width: 50%;
}
.sidebar .sidebar-content {
    background-color: #f5f5f5;
}
</style>
"""


# Render styles
st.markdown(styles, unsafe_allow_html=True)

#image = Image.open(r"C:\Users\kavit\Documents\My_Projects\SharkTank_Dashboard\streampanda.png")

#headers = st.container()
#with headers:
#	col1, col2 = st.columns(2)
#	with col1:
#		st.image(image)
#	with col2:
#		st.header("The Shark Tank Deal Analyzer")
#		st.subheader("Use this Streamlit app to analyze your sales!")
#		st.write('Shark Tank has ')

st.header("The Shark Tank Deal Analyzer")
st.subheader("A Streamlit & PandasAI Analysis")
st.write('Shark Tank is a reality show where startups pitch their products and services to a panel of judges, who are venture capitalists. Based on the pitches and the questions that follow, the judges decide whether or not to invest in those startups. They offer the startups a deal which consists of a monetary investment in exchange for a stake. The startup owners or pitchers can decide to take it, propose a counter offer, or reject the proposal. If the VC and the pitchers agree on a stake and an investment amount, they have a deal.') 
st.write('This show became so popular that it has proliferated across multiple countries. However, I was curious about certain deal trends. I want to know if female founders close more deals, if VCs prefer startups with more than one founder, do these trends change across countries, and more such questions.')























###########################################
