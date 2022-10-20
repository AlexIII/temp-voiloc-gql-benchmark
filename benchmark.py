from main_query import MainQuery
import requests
from timeit import default_timer as timer

VOILOC_GQL_URL = "http://192.168.8.28:8080/graphql"

def run_query(url: str, query: str, variables = None) -> str:
    request = requests.post(url, json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Unexpected status code returned: {request.status_code}")

vars = {
    'noGasData': True,
    'ts': '2022-10-14T05:00:00.000Z'    # Archive date
}

startTs = timer()
res = run_query(VOILOC_GQL_URL, MainQuery, vars)
endTs = timer()

# print(res)
print(f'Time elapsed: {endTs - startTs} sec')
