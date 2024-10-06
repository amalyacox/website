
# Main Page of Website 

import streamlit as st 
import streamlit.components.v1 as components 
from details import * 

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide") 

# sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    st.success("Select a page above.")

# main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.header("Amalya Johnson", divider='rainbow')

col1, col2, col3 = st.columns([1.3, 0.2, 1])

with col1: 
    st.markdown(info['brief'])

with col3: 
    st.image("static/AmalyaJohnsonHeadshot2024.png")

col4, col5 = st.columns([0.1,3])

with col4: 
    st.markdown(linkedin_logo, unsafe_allow_html=True)
    st.markdown(github_logo, unsafe_allow_html=True)
    st.markdown(research_logo, unsafe_allow_html=True)
    # st.markdown(research_logo, unsafe_allow_html=True)

with col5: 
    st.markdown(f"###### [Linkedin]({linkedin_link})")
    st.markdown(f"###### [Github]({github_link})")
    st.markdown(f"###### [Google Scholar]({googlescholar_link})")


