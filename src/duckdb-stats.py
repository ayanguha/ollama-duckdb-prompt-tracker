import duckdb

def prepare_data(generate = False):
    if generate:
      if os.path.exists("sample.duckdb"):
          os.remove("sample.duckdb")
      con = duckdb.connect(database='sample.duckdb')
      qry = "CALL dsdgen(sf = 1);"
      con.execute(qry)
    else:
      con = duckdb.connect(database='sample.duckdb')
    return con



def get_all_metadata():
    con = duckdb.connect(database='sample.duckdb', read_only=True)
    qry = '''select table_catalog, 
                 table_schema, 
                 table_name, 
                 column_name, 
                 ordinal_position, 
                 column_default, 
                 is_nullable,
                  data_type,
           from information_schema.columns;'''
    res = con.execute(qry).fetchall()
    return res 

def compare_data(qry: str = None):
    con = duckdb.connect(database='sample.duckdb', read_only=True)
    con.sql("PRAGMA enable_profiling;")

    res = con.sql(qry)
    explain_res = res.explain("ANALYZE")
    return explain_res

prepare_data()
columns = get_all_metadata()
print(compare_data())