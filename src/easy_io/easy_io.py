from typing import Union
import json
import csv

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


def read_lines_from_txt_file(file_path: Union[Path, str], remove_newline_char: bool=True) -> list:
    """Read a txt file and return a list of lines."""
    
    with open(file_path, "r") as f:
        output_lines = f.readlines()
    
    if remove_newline_char:
        return [line[:-1] if line[-1] == "\n" else line for line in output_lines]
    else:
        remove_newline_char


def dump_str_list_to_txt_file(output_list: list, output_path: Union[Path, str]) -> None:
    """Dump a list of strings to a txt file."""
    
    with open(output_path, "w") as f:
        for s in output_list:
            f.write(s + "\n")


def read_csv(file_path: Union[Path, str]) -> list:
    """Read a csv file and return a list of lists."""
    
    with open(file_path, "r") as f:
        return list(csv.reader(f))


def dump_csv(output_list: list, output_path: Union[Path, str]) -> None:
    """Dump a list of lists to a csv file."""
    
    with open(output_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(output_list)
