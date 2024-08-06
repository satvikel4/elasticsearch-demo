from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(["http://localhost:9200"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify([])
    
    result = es.search(index="products", body={
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "description"]
            }
        }
    })
    
    products = [hit['_source'] for hit in result['hits']['hits']]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)