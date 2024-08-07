from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(["http://localhost:9200"]).options(ignore_status=[400])

# Create an index
es.indices.create(index='test-index')

# Insert data into the index
es.index(index='test-index', id=1, body={"name": "John Doe", "age": 30})
es.index(index='test-index', id=2, body={"name": "Jane Doe", "age": 25})

# Check if the index exists
if es.indices.exists(index='test-index'):
    print("Index exists.")
else:
    print("Index does not exist.")

# Check the number of documents in the index
count = es.count(index='test-index')
print(f"Number of documents in the index: {count['count']}")

# Perform a search query
res = es.search(index='test-index', body={"query": {"match_all": {}}})

# Print the search results
print(res)
