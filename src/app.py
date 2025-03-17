import streamlit as st
import requests 

st.set_page_config(layout="wide")

# Set the title of the app
st.title("SQL Prompt Validation Application")


with st.expander("Read the explanation"):
        
    # Docstring to document this application

    """
    Streamlit App for sending prompts to a Flask server and displaying the results.

    This application allows users to input a prompt, select a model from available options,
    and submit the prompt to a Flask server endpoint. The server processes the prompt using
    the selected model and returns the response, which is then displayed in the app. Additionally,
    the app fetches and displays the history of all prompts submitted.

    Modules:
        streamlit: Used for creating the web application interface.
        requests: Used for making HTTP requests to the Flask server.

    Functions:
        None

    Endpoints:
        GET /models: Fetches the list of available models from the Flask server.
        POST /run_prompt: Sends the user's prompt and selected model to the Flask server for processing.
        POST /prompt_history: Fetches the history of all prompts submitted to the Flask server.

    User Interface:
        - Title: "Streamlit App"
        - Text Area: For inputting the user's prompt.
        - Pills: For selecting the model to use.
        - Button: For submitting the prompt.
        - Display: Shows the user's prompt and the server's response.
        - Display: Shows the history of all prompts submitted.
    """




tab1, tab2 = st.tabs(['Run A Single Query', "View All Results"])

with tab1:
    # Create a text area with the specified properties
    prompt = st.text_area(
        label="Ask a Question",
        value="A single, specific, short description of your business question.",
        height=100,
        help="A single, specific, short description of your business question."
    )

    # create a request to flask server send the prompt to the server to run_prompt endpoint
    # and print the response
    options = requests.get("http://localhost:5000/models").json().get('models')# ["duckdb-nsql:latest", "llama3.2:latest"]



    selected_model = st.pills(
        "Model",
        options=options,
        selection_mode="single",
    )


    # Create a submit button
    if st.button("Submit"):
        response = requests.post("http://localhost:5000/run_prompt", json={"prompt": prompt, "model": selected_model})
        st.write("Your prompt:", prompt)
        st.json(response.json(), expanded=True)


with tab2:
    all_results = requests.post("http://localhost:5000/prompt_history").json().get('prompt_history')#

    st.json(all_results, expanded=1)