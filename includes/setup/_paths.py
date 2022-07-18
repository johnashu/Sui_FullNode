from tools.file_op import create_data_path, os

paths = dict(
data_path_json_in = os.path.join( "IN", "JSON"),
data_path_csv_in = os.path.join( "IN", "CSV"),
data_path_json_out = os.path.join( "OUT", "JSON"),
data_path_csv_out = os.path.join( "OUT", "CSV"),
)

create_data_path("", data_path="logs")
create_data_path("", data_path="data")

for _, p in paths.items():
    create_data_path(p.split('\\')[0], data_path="data")    
    create_data_path(p, data_path="data")

