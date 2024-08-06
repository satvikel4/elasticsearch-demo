from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

# Sample product data
products = [
    {"name": "Laptop", "description": "High-performance laptop with SSD"},
    {"name": "Smartphone", "description": "Latest model with advanced camera"},
    {"name": "Headphones", "description": "Noise-cancelling wireless headphones"},
    {"name": "Tablet", "description": "Lightweight tablet with long battery life"},
    {"name": "Smartwatch", "description": "Fitness tracker with heart rate monitor"}
]

# Create the 'products' index if it doesn't exist
if not es.indices.exists(index="products"):
    es.indices.create(index="products")

# Index the sample products
for i, product in enumerate(products):
    es.index(index="products", id=i+1, body=product)

print("Sample data indexed successfully.")