from flask import Flask, request, jsonify
from generate import generate_sql, get_query_statistics, get_model_list 
from database import store_data, get_all_data,get_data

app = Flask(__name__)

# Store prompt history
prompt_history = []

@app.route('/run_prompt', methods=['POST'])
def run_prompt():
    data = request.json
    prompt = data.get('prompt')
    model = data.get('model') 
    
    if prompt:
        result = get_prompt_response(prompt = prompt, model = model)
        #prompt_history.append(result)

        #return jsonify({"prompt_history": prompt_history}), 200
        return jsonify({"prompt_result": result}), 200
    return jsonify({"error": "No prompt provided"}), 400

# Route for get list of models
@app.route("/models", methods = ['GET'])
def get_models(): 
    # return a list 
    
    return jsonify({"models": get_model_list()})

def get_prompt_response(prompt: str, model: str = 'duckdb-nsql:latest'):
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
    all_results = get_all_data()
    print(all_results)
    print(jsonify({"prompt_history": all_results}))
    return jsonify({"prompt_history": all_results}), 200

if __name__ == '__main__':
    app.run(debug=True)