import couchdb 


def __createOrGetDatabase__():
    # create a connection to the couchdb server running on localhost:5984
    # create a database called ollama-duckdb-prompt-tracker
    # if it already exists, get the existing database
    # return the database object
    # create a connection to the couchdb server running on localhost:5984
    couch = couchdb.Server('http://admin:admin@127.0.0.1:5984//')

    try:
        db = couch.create('ollama-duckdb-prompt-tracker')
    except:
        db = couch['ollama-duckdb-prompt-tracker']
# create a function to store data in database running on localhost:5984 
def store_data(data):
    db = __createOrGetDatabase__()
    _id, _rev = db.save(data)
    return _id  

# create a function to get All data from database running on localhost:5984
def get_all_data():
    db = __createOrGetDatabase__()
    results = db.view('_all_docs',include_docs=True)
    return [r.doc for r in results]

# create a function to get data by id from database running on localhost:5984

def get_data(db,id: int):
    pass