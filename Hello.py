# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def generate_explanation(question):
    # Your code goes here
    # Replace this line with your explanation generation logic
    return "Explanation for: " + question

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    
    # App title
    st.title("Family-Friendly Explanation Generator")

    # Collect user information
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)

    # Check if the name and age are provided
    if name and age:
        # Collect the question
        question = st.text_area("What would you like to explain?")

        if question:
            # Call the function to generate an explanation
            explanation = generate_explanation(question)

            # Display the explanation
            st.write("Here's an explanation suitable for someone named", name, "who is", age, "years old:")
            st.write(explanation)
    else:
        st.write("Please enter your name and age to continue.")


if __name__ == "__main__":
    run()
