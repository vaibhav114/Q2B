import streamlit as st

# Simple Streamlit app to demonstrate basic functionality
def main():
    st.title('Simple Streamlit App')
    
    st.write("Welcome to the Streamlit demo!")

    # Display a simple text input field
    user_input = st.text_input("Enter your name:")

    if user_input:
        st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()
