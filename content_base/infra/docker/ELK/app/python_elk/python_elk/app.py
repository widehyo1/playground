from pprint import pprint, pformat
from elasticsearch import Elasticsearch

# Define the Elasticsearch connection
es = Elasticsearch(
    "https://localhost:9200",  # Elasticsearch URL
    ca_certs="/tmp/ca.crt",    # Path to the certificate
    basic_auth=("elastic", "changeme"),  # Username and password
)

# Define the query
query = {
    "query": {
        "match_all": {}
    }
}

# Send a search request
response = es.search(index="knowinfo", body=query)

pprint(f'{response=}')

# Print the response
print("Total hits:", response['hits']['total']['value'])
