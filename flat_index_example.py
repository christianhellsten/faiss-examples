"""
Faiss Flat Index (Brute-Force Search) Example
"""
import pickle
import faiss
import numpy as np
import os.path

data_file = 'flat_faiss.data'
index_file = 'flat_faiss.index'
rows = 1000
dimensions = 2 # columns = dimensions

def index():
    """
    Index the data
    """
    ix = faiss.IndexFlatL2(dimensions)
    ix.add(data)
    faiss.write_index(ix, index_file)
    return ix


def search(row, limit=10):
    """
    Search the data
    """
    return ix.search(row, limit)

def load_data():
    """
    Load data
    """
    if not os.path.isfile(data_file):
        data = np.random.random((rows, dimensions)).astype('float32')
        with open(data_file, 'wb') as fh:
            pickle.dump(data, fh)
        return data
    else:
        return pickle.load(open(data_file, "rb"))

def load_index():
    """
    Load index
    """
    if not os.path.isfile(index_file):
        print("Writing index to disk")
        return index()
    else:
        print("Reading index from disk")
        return faiss.read_index(index_file)

data = load_data()
ix = load_index()

# Generate a random query
# query = np.random.random((5, dimensions)).astype('float32')
# Search for first 5 rows
query = data[:5]
distances, indices = search(query)

print("=========QUERY=========")
print(f"Searching for rows most similar to:\n {query}")

print("=========INDICES=========")
print(indices)

print("=========DISTANCES=========")
print(distances)
