# Easy IO

This project includes functions that makes I/O in Python code easier.

## Setup

```sh
git clone https://github.com/ryokamoi/easy_io.git
pip install ./easy_io
```

## Example

```python
from easy_io import read_json, read_jsonl

# json
dict_from_json: dict = read_json("path/to/json_file.json")
dump_json(dict_from_json, "path/to/output_file.json")

# jsonl
list_of_dict: list[dict] = read_jsonl("path/to/jsonl_file.jsonl")
dump_jsonl(list_of_dict, "path/to/output_file.jsonl")
```
