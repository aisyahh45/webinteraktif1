import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from image1 import main

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
    "page 3" : page_3,
    "Hitung Luas" : page_4,
    "Image processing" : main
}

st.sidebar.image("bear.png", width=200)
page = st.sidebar.radio("halaman", list(PAGES.keys()))
PAGES[page]()