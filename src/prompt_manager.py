import ollama
from duckdb_stats import get_all_metadata, get_explain_result
import os  

def get_model_list():

  
    '''
    **Description**

    Returns a list of available models in local ``ollama`` installation. 

    :return: List of model names 

    .. note::
        
        The models are expected to be installed locally and accessible via the `ollama` python library. 
        The function returns a list of model names that can be used for generating SQL queries.

    You can check if ``ollama`` is installed by running the following command in your terminal: 
    
    .. code-block:: bash
        
        ollama list
        
        NAME              	ID          	SIZE  	MODIFIED    
        
        starcoder2:7b     	1550ab21b10d	4.0 GB	5 weeks ago	
        
        codellama:7b      	8fdf8f752f6e	3.8 GB	5 weeks ago	
        
        sqlcoder:7b       	77ac14348387	4.1 GB	5 weeks ago	
        
        duckdb-nsql:latest	3ed734989690	3.8 GB	5 weeks ago

        
    '''

    models = [m.model for m in ollama.list().models]
    return models

def get_system_prompt():

    '''
    **Description**

    Returns a system prompt template for SQL query generation.
    The system prompt provides context to the model about its role and the task it needs to perform.
    The prompt includes a placeholder for metadata, which will be replaced with the actual database schema information.
    The metadata is expected to be a list of tuples, each containing information about a table and its columns.
    The system prompt also includes guidelines for the model to follow when generating the SQL query.

    ''' 


    system_prompt = '''
    You are a SQL developer working on a project that requires you to write a SQL query.
    You have been provided with a database schema and a prompt that you need to convert into a SQL query.
    Following list represents database schema that the SQL query will run on. 
    The list is a tuple of string representing information of
      table_catalog,  table_schema, table_name, column_name,  ordinal_position,  
      column_default, is_nullable,data_type respectevely. 
      <: metadata :>
    '''
    return system_prompt

def get_guideline_prompts():

    '''
    **Description**

    Returns a set of guidelines for the model to follow when generating SQL queries.
    The guidelines specify that the result should be a valid SQL query that can be executed on the provided schema.
    The model is instructed to return only the SQL query as a string.
    The guidelines are designed to ensure that the generated SQL query is syntactically correct and adheres to SQL standards.
    The guidelines are appended to the system prompt to provide additional context to the model.
    '''

    guideline_prompts = ''' Result should be a SQL query that can be run on the provided schema.
        result must be a string that is a valid SQL query.
        Please return only the SQL query.
    '''
    return guideline_prompts

def generate_sql(prompt: str, model: str):

    '''
    **Description**

    Generates a SQL query from a natural language prompt using the specified model.
    The function first retrieves the metadata from the database using the `get_all_metadata` function.
    The metadata is then used to replace the placeholder in the system prompt template.
    The model is then called to generate the SQL query based on the provided prompt and system prompt.
    The generated SQL query is returned along with the metadata used for generation.
    
    :param str prompt: The natural language prompt.
    
    :param str model: The model to use for query generation (default: duckdb-nsql:latest).
    
    :return: A tuple containing the generated SQL query and the metadata used for generation.
    
    :raises Exception: If the model is not found or if there is an error during SQL generation.
    '''


    metadata = list(get_all_metadata())
    system_prompt_template = get_system_prompt()
    system_prompt = system_prompt_template.replace('<: metadata :>', str(metadata))
    guideline_prompts = get_guideline_prompts() 
    system_prompt = system_prompt + guideline_prompts
    
    r = ollama.generate(
    model = model,
    prompt=prompt,
    system=system_prompt    
    )
    sql_stmt = r['response'] #"SELECT * FROM date_dim"
    
    return sql_stmt, metadata