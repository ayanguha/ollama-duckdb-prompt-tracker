import couchdb 


def __createOrGetDatabase__():
    """
    create a connection to the couchdb server running on ```localhost:5984```
    create a database called ollama-duckdb-prompt-tracker. If it already exists, get the existing database
    return the database object
    create a connection to the couchdb server running on localhost:5984
    
    .. note::

        This function is used to create a connection to the couchdb server running on locally for MVP. 
        Please overwrite this appropriately for any production workload
    
    
    """
    couch = couchdb.Server('http://admin:admin@127.0.0.1:5984//')

    try:
        db = couch.create('ollama-duckdb-prompt-tracker')
    except:
        db = couch['ollama-duckdb-prompt-tracker']
    return db
# create a function to store data in database running on localhost:5984 
def store_data(data):

    """
    Get the database object from the __createOrGetDatabase__ function and store the data in the database
    
    :param data: data to be stored in the database
    :return: id of the data stored in the database

    """

    db = __createOrGetDatabase__()
    _id, _rev = db.save(data)
    return _id  


def get_all_data():

    """
    Get the database object from the __createOrGetDatabase__ function and get all the data from the database
    
    :return: list of all data in the database
    :rtype: list

    .. note::    
        This function does not take any parameters. It is used to get all the data from the database, so some filtering and pagination will be needed
    
    """

    db = __createOrGetDatabase__()
    results = db.view('_all_docs',include_docs=True)
    return [r.doc for r in results]

# create a function to get data by id from database running on localhost:5984

def get_data(db,id: int):

    """
    .. note::
        This function is not implemented yet
    """

    pass