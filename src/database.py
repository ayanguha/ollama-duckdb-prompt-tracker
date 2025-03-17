import couchdb 



couch = couchdb.Server('http://admin:admin@127.0.0.1:5984//')

try:
    db = couch.create('ollama-duckdb-prompt-tracker')
except:
    db = couch['ollama-duckdb-prompt-tracker']
# create a function to store data in database running on localhost:5984 
def store_data(data):
    _id, _rev = db.save(data)
    return _id  

# create a function to get All data from database running on localhost:5984
def get_all_data():
    results = db.view('_all_docs',include_docs=True)
    return [r.doc for r in results]

# create a function to get data by id from database running on localhost:5984

def get_data(id: int):
    pass