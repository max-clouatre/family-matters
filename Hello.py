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

import pandas as pd

# Function to generate explanation (placeholder for your implementation)
def generate_explanation(question, people):
    # Your code goes here
    # Replace this line with your explanation generation logic
    return f"Explanation for: {question}, tailored for {', '.join([person['name'] for person in people])}"

# App title
st.title("Family-Friendly Explanation Generator")

# Initialize session state for the table
if 'people_table' not in st.session_state:
    st.session_state.people_table = pd.DataFrame(columns=['name', 'age'])

# Function to add a new person to the table
def add_person():
    st.session_state.people_table = st.session_state.people_table.append({'name': new_name, 'age': new_age}, ignore_index=True)

# Input fields to add new person
new_name = st.text_input("Enter name:")
new_age = st.number_input("Enter age:", min_value=0, max_value=120, step=1)

# Button to add the person to the table
if st.button("Add Person"):
    if new_name and new_age:
        add_person()

# Display the table and allow selection of people
st.write("People to Explain to:")
selected_indices = st.multiselect("Select people:", st.session_state.people_table.index, format_func=lambda x: st.session_state.people_table.loc[x, 'name'])
selected_people = st.session_state.people_table.loc[selected_indices]

# Collect the question
question = st.text_area("What would you like to explain?")

# Display the explanation
if question and not selected_people.empty:
    explanation = generate_explanation(question, selected_people.to_dict('records'))
    st.write("Explanation:")
    st.write(explanation)
