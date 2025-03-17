import ollama
from duckdb_stats import get_all_metadata, get_explain_result
import os 

def generate_sql(prompt: str, model: str):
    metadata = list(get_all_metadata())
    
    r = ollama.generate(
    model = model,
    prompt=prompt,
    system='''
    You are a SQL developer working on a project that requires you to write a SQL query.
    You have been provided with a database schema and a prompt that you need to convert into a SQL query.
    Following list represents database schema that the SQL query will run on. 
    The list is a tuple of string representing information of
      table_catalog,  table_schema, table_name, column_name,  ordinal_position,  
      column_default, is_nullable,data_type respectevely.
    ''' + str(metadata) + 
    ''' Result should be a SQL query that can be run on the provided schema.
        result must be a string that is a valid SQL query.
        Please return only the SQL query.
    '''
    )
    sql_stmt = r['response'] #"SELECT * FROM date_dim"
    
    return sql_stmt, metadata


def get_query_statistics(qry: str):
    explain_res = get_explain_result(qry)
    return explain_res

def get_model_list():
  models = [m.model for m in ollama.list().models]
  return models