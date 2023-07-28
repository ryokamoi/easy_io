from typing import Union
import json

from pathlib import Path


def read_json(file_path: Union[Path, str]) -> dict:
    """Read a json file and return a dictionary."""
    
    with open(file_path, "r") as f:
        return json.load(f)


def dump_json(output_dict: dict, output_path: Union[Path, str]) -> None:
    """Dump a dictionary to a json file."""
    
    with open(output_path, "w") as f:
        json.dump(output_dict, f, indent=4, ensure_ascii=False)


def read_jsonl(file_path: Union[Path, str]) -> list:
    """Read a jsonl file and return a list of dictionaries."""
    
    dataset_json_list = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            dataset_json_list.append(json.loads(line[:-1]))
    
    return dataset_json_list


def dump_jsonl(output_list: list, output_path: Union[Path, str]) -> None:
    """Dump a list of dictionaries to a jsonl file."""
    
    with open(output_path, "w") as f:
        for d in output_list:
            f.write(json.dumps(d) + "\n")


def read_lines_from_txt_file(file_path: Union[Path, str]) -> list:
    """Read a txt file and return a list of lines."""
    
    with open(file_path, "r") as f:
        return f.readlines()
