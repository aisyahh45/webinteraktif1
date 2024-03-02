import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3

# import pandas as pd
#import matplotlib.pyplot as plt

# st.write("aisyah")
# df = pd.DataFrame({
#         'no' : ['1','2','3','4'],
#         'nama' : ['daren','nara','angkasa','asya'],
#         'nilai' : ['84','88','94','98']
# })

# df


        
PAGES = {
                "page 1" : page_1,
                "page 2" : page_2,
                "page 3" : page_3
}

st.sidebar.image("bear_1.jpg", width=200)
page = st.sidebar.radio("halaman", list(PAGES.keys()))
PAGES[page]()