import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import matplotlib

matplotlib.use('tkAgg')



# Read Data
india=pd.read_csv(r"C:\Users\kavit\Documents\My_Projects\SharkTank_Dashboard\sharktank_india.csv", sep=',')
usa=pd.read_csv(r"C:\Users\kavit\Documents\My_Projects\SharkTank_Dashboard\sharktank_usa.csv", sep=',')

# create an LLM by instantiating OpenAI object, and passing API token
llm = OpenAI(api_token="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")

# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

# Define main content
content = st.container()
with content:
	option = st.selectbox('Please select a country for analysis',('India', 'U.S.A'))
	st.write('You selected:', option)
	if option == 'India':
		option = india
		st.dataframe(option.head())
	else:
		option=usa
		st.dataframe(option.head())


# new code below...
prompt = st.text_area("Please enter your query: ")

# query answering
if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                #if 'show' or 'plot' or 'graph' in prompt:
                 #   plot = pandas_ai.run(option, prompt) #option.chat(prompt)
                  #  st.pyplot(plot.fig)
                #else:
                st.write(pandas_ai.run(option, prompt))
        else:
            st.warning("Please enter a prompt.")