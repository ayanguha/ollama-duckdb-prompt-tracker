from duckdb_stats import get_explain_result

def get_query_statistics(qry: str):
    
    '''
    **Description**
    
    Get the query statistics for a given SQL query.
    The function uses the `get_explain_result` function from the `duckdb_stats` module to analyze the query.
    
    :param str qry: The SQL query to analyze.

    :return: A dictionary containing the query statistics.

    :rtype: dict
    '''
    
    explain_res = get_explain_result(qry)
    return explain_res

