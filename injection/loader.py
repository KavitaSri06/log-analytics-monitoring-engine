import dask.bag as db
from injection.parser import parse_log_line
from Schema.schema import log_schema

def load_logs(file_path):
    bag = db.read_text(file_path)
    parsed = (
        bag.map(parse_log_line)
        .filter(lambda x: x is not None)  # Filter out lines that failed to parse
    )
    df = parsed.to_dataframe()
    return df.astype(log_schema)