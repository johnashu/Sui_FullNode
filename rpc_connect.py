import json
from urllib import response
from brownie import rpc
import requests
from includes.config import *
from tools import file_op
import pysui.rpc.request


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
    # response = requests.post(rpc_url, headers=headers, json=json_data)
    response = pysui.rpc.request.rpc_request(
        json_data["method"], json_data.get("params"), endpoint=rpc_url
    )
    # print(response.text)
    try:
        data = response
    except Exception as e:
        data = response
    # log.info(data)
    file_op.save_json(join(json_out, json_data["method"] + "_rpc"), data)
