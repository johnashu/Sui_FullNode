from includes.setup._envs import Envs
from includes.setup._logging import start_logger
import includes.setup._paths
from tools.file_op import open_json
import sys

sys.dont_write_bytecode = True

verbose = False

envs = Envs()
log = start_logger(verbose=verbose)

version = '1.0.0'
