User Interface
====================

Usage  
------------------------

Streamlit App for sending prompts to a Flask server and displaying the results.

This application allows users to input a prompt, select a model from available options, 
and submit the prompt to a Flask server endpoint. The server processes the prompt using 
the selected model and returns the response, which is then displayed in the app. Additionally, 
the app fetches and displays the history of all prompts submitted.

Modules
-------------------------
`streamlit` used for creating the web application interface.

`requests` used for making HTTP requests to the Flask server.

Functions:
--------------------------
None

API Endpoints Consumed 
---------------------------

GET /models: Fetches the list of available models from the Flask server.

POST /run_prompt: Sends the user's prompt and selected model to the Flask server for processing.

POST /prompt_history: Fetches the history of all prompts submitted to the Flask server.

See :doc:`server` for more details on the API endpoints.

User Interface
--------------------------
**Title**: "Streamlit App"

**Text Area**: For inputting the user's prompt.

**Pills**: For selecting the model to use.

**Button**: For submitting the prompt.

**Display**: Shows the user's prompt and the server's response.

**Display**: Shows the history of all prompts submitted.

How to Run  
------------------------

.. code-block:: bash

   streamlit run src/ui.py 

