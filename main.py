
import streamlit as st # streamlit is a library for building web apps
from units import UNIT_CATEGORIES # units is a module that contains the unit categories and their units
from converter import convert # converter is a module that contains the convert function

st.set_page_config(page_title="Unit Converter", layout="centered") # set the page title and layout

st.title("🔄 Unit Converter") # set the title of the app

category = st.selectbox("Select Category", list(UNIT_CATEGORIES.keys())) # select the category of the units
units = UNIT_CATEGORIES[category] # get the units for the selected category

col1, col2 = st.columns(2) # create two columns
with col1:
    from_unit = st.selectbox("From", list(units.keys()), key="from_unit") # select the from unit
with col2:
    to_unit = st.selectbox("To", list(units.keys()), key="to_unit") # select the to unit

value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0) # input the value to convert

if st.button("Convert"): # convert the value
    result = convert(category, from_unit, to_unit, value)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}") # display the result    
    else:
        st.error("Conversion failed. Please check your input.") # display an error if the conversion fails  


# Add a footer with a link to the GitHub repository

st.markdown("------------")

st.markdown("Made with ❤️ by [Muhammad Awais](https://github.com/awais995)")




