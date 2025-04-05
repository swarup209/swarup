import streamlit as st
name=st.text_input("Enter your name: ")
fname=st.text_input("enter your father name: ")
adr=st.text_area("enter your address: ")
classdata=st.selectbox("enter your class: ",("graduation","under graduation"))
button=st.button("submit")
if button :
    st.markdown(f"""
                Name={name}
                Father name={fname}
                address={adr}
                education detail={classdata}""")