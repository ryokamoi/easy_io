from typing import Union, List
import json

from pathlib import Path


def read_jsonl(dataset_path: Union[Path, str]) -> List[dir]:
    dataset_json_list = []
    with open(dataset_path, "r") as f:
        for line in f.readlines():
            dataset_json_list.append(json.loads(line[:-1]))
    
    return dataset_json_list


def read_numbers_list_from_text_file(file_path: Union[Path, str], num_type="int") -> List[int]:
    output = []
    with open(file_path, "r") as f:
        for line_ in f.readlines():
            line = line_[:-1]
            if num_type == "int":
                output.append(int(line))
            elif num_type == "float":
                output.append(float(line))
            else:
                raise ValueError("Not implemented")
    
    return output


def read_str_list_from_text_file(file_path: Union[Path, str]) -> List[str]:
    output: List[str] = []
    
    with open(file_path, "r") as f:
        for line_ in f.readlines():
            assert line_[-1] == "\n"
            
            output.append(line_[:-1])
    
    return output


def dump_numbers_list_to_text_file(num_list: List[Union[float, int]], file_path: Union[Path, str]):
    with open(file_path, "w") as f:
        for num in num_list:
            f.write(str(num) + "\n")
