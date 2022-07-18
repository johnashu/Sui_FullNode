import requests, re
from includes.config import *
from tools import file_op
from template import imports_constants, method_blank


def camel_to_snake(str):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", str).lower()


def create_api_data(fn: str) -> None:
    api_data = requests.get(api_url).json()
    file_op.save_json(fn, api_data)


def open_api_data(fn: str, show: bool = False) -> dict:
    api_data = file_op.open_json(fn)
    if show:
        for x in api_data["methods"]:
            log.info(x["name"])
    return api_data


def build_method(
    method: dict,
    template: str,
    snake_case: bool = True,
    link: str = "https://docs.sui.io/build/json-rpc",
) -> str:
    func = camel_to_snake(method.get("name").split("_")[-1])
    desc = method.get("description")
    params = method.get("params")
    params = [x["name"] for x in params]
    args = params = ", ".join(params)
    method_name = method.get("name")
    completed = template.format(func, args, desc, link, method_name, params)
    return completed


def create_file(
    fn: str, methods: list, imports_constants: str, method_blank: str
) -> None:
    _file_str = ""
    _file_str += imports_constants

    for x in methods:
        _file_str += build_method(x, method_blank)
    file_op.save_file(fn, _file_str)


data_fn = join(json_out, api_data_fn)
py_fn = join("pysui", "rpc_methods.py")

create_api_data(data_fn)
data = open_api_data(data_fn)["methods"]
create_file(py_fn, data, imports_constants, method_blank)
