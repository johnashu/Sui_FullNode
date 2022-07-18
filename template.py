imports_constants = """
from .rpc.request import (
    rpc_request
)
from .exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError
)
import time
import random

_default_endpoint = 'http://localhost:9000'
_default_timeout = 30

"""

method_blank = '''
def {}({}, endpoint=_default_endpoint, timeout=_default_timeout) -> list:
    """
    {}

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of transactions in the pool, see get_transaction_by_hash for a description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    {}
    """
    method = '{}'
    params = [{}]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)['result']
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e

'''
