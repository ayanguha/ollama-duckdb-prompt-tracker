Server Module
=============

This module provides a Flask server that exposes APIs for generating SQL queries from natural language prompts, retrieving model lists, and storing/retrieving prompt history.

API Endpoints
-------------

`run_prompt` (POST)
----------------------
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

- On error:
    .. code-block:: json 

        {
        "error": "No prompt provided"
        }
