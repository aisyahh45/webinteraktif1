import streamlit as st
# import pandas as pd
#import matplotlib.pyplot as plt

# st.write("aisyah")
# df = pd.DataFrame({
#         'no' : ['1','2','3','4'],
#         'nama' : ['daren','nara','angkasa','asya'],
#         'nilai' : ['84','88','94','98']
# })

# df

def page_1():
        st.title("Halaman 1")
        st.write('Halaman ini digunakan untuk Intro')
def page_2():
        st.title("Halaman 2")
        st.write('Halaman ini digunakan untuk Menampilkan youtube')
def page_3():
        st.title("Halaman 3")
        st.write('Halaman ini digunakan untuk Menam[pilkan Rumus Matematika')
        
PAGES = {
                "page 1" : page_1,
                "page 2" : page_2,
                "page 3" : page_3
}

page = st.sidebar.radio("halaman", list(PAGES.keys()))
PAGES[page]()