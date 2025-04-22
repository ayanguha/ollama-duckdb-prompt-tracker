from flask import Flask, request, jsonify
from database_manager import get_query_statistics 
from result_manager import store_data, get_all_data
from prompt_manager import generate_sql, get_model_list

app = Flask(__name__)

# Store prompt history
prompt_history = []

@app.route('/run_prompt', methods=['POST'])
def run_prompt():
    '''
     
**Description**: 

Accepts a natural language prompt and a model name, generates a SQL query, and returns the result.

**Request Body**:

  .. code-block:: json

    {
        "prompt": "Your natural language prompt",
        "model": "Model name (default: duckdb-nsql:latest)"
    }

**Response**:

On success:
  .. code-block:: json

        {
            "prompt_result": {
            "source_prompt": "Your natural language prompt",
            "llm_model_used": "Model name",
            "SQL returned": "Generated SQL query",
            "result_status": "Execution status",
            "result_statistics": "Explain plan or statistics",
            "metadata_used": "Metadata used for query generation"
            }
        }

On error:
    .. code-block:: json 

        {
        "error": "No prompt provided"
        }

    
    '''
    data = request.json
    prompt = data.get('prompt')
    model = data.get('model') 
    
    if prompt:
        result = get_prompt_response(prompt = prompt, model = model)
        return jsonify({"prompt_result": result}), 200
    return jsonify({"error": "No prompt provided"}), 400

# Route for get list of models
@app.route("/models", methods = ['GET'])
def get_models(): 
    '''
        
**Description**: 

Returns a list of available models.

**Response**:

On success:
  .. code-block:: json

        {
            "models": ["model1", "model2", "model3"]
        }    
    '''
    
    return jsonify({"models": get_model_list()})

def get_prompt_response(prompt: str, model: str = 'duckdb-nsql:latest'):

    '''
    **Description**
     
       Generates a SQL query from a natural language prompt using the specified model.
    
    :param str prompt: The natural language prompt.
    :param str model: The model to use for query generation (default: duckdb-nsql:latest).
    :return: A dictionary containing the generated SQL query, execution status, explain plan, and metadata used.

    '''
    sql_query, metadata_used = generate_sql(prompt = prompt, model = model)
    statistics = get_query_statistics(sql_query)
    data = {"source_prompt": prompt,
            "llm_model_used": model,
            "SQL returned": sql_query,
            "result_status": statistics.get('status'),
            "result_statistics": statistics.get('explain_result'),
            "metadata_used": metadata_used
            }
    store_data(data)                    
    return data 

@app.route('/prompt_history', methods=['POST'])
def get_prompt_history():
    '''
**Description**: 

Description: (deployment test 1) Retrieves the history of prompts and their corresponding results.
**Request Body**:

  .. code-block:: json

    {
        "filter": "not_yet_implemented"
    }

**Response**

On success:
  .. code-block:: json

        {
            "prompt_history": [
                {
                    "source_prompt": "Prompt 1",
                    "llm_model_used": "Model name",
                    "SQL returned": "Generated SQL query",
                    "result_status": "Execution status",
                    "result_statistics": "Explain plan or statistics",
                    "metadata_used": "Metadata used for query generation"
                },
            ]
        }

    
    '''
    all_results = get_all_data()
    print(jsonify({"prompt_history": all_results}))
    return jsonify({"prompt_history": all_results}), 200

if __name__ == '__main__':
    app.run(debug=True)