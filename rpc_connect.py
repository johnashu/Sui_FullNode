import requests
from includes.config import *
from tools import file_op


rpc_url = "http://154.53.59.19:9000"

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

tx = "6+JDIRduJ8DGp6MTWjkb36lCVLKp7pWeSUsVr0U5rFw="

r = (
    {
        "jsonrpc": "2.0",
        "method": "rpc.discover",
        "id": 1,
    },
    {"jsonrpc": "2.0", "method": "sui_getRecentTransactions", "params": [10], "id": 0},
    {
        "jsonrpc": "2.0",
        "method": "sui_getTotalTransactionNumber",
        "params": [],
        "id": 0,
    },
    {"jsonrpc": "2.0", "method": "sui_getTransaction", "params": [tx], "id": 0},
)

for json_data in r:
    log.info(json_data["method"])
    response = requests.post(rpc_url, headers=headers, json=json_data)

    # print(response.text)
    try:
        data = response.json()
    except Exception as e:
        data = response.text
    # log.info(data)
    file_op.save_json(join(json_out, json_data["method"] + "_rpc"), data)
