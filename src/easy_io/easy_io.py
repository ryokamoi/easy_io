from typing import Union, List, Literal
import json

from pathlib import Path


def read_jsonl(dataset_path: Union[Path, str]) -> List[dir]:
    dataset_json_list = []
    with open(dataset_path, "r") as f:
        for line in f.readlines():
            dataset_json_list.append(json.loads(line[:-1]))
    
    return dataset_json_list


def read_list_from_text_file(file_path: Union[Path, str], element_type: Literal["int", "float", "str"]) -> List[int]:
    output = []
    with open(file_path, "r") as f:
        for line_ in f.readlines():
            assert line_[-1] == "\n"
            
            line = line_[:-1]
            if element_type == "str":
                output.append(line)
            elif element_type == "int":
                output.append(int(line))
            elif element_type == "float":
                output.append(float(line))
            else:
                raise ValueError("Not implemented")
    
    return output


def dump_list_to_text_file(dump_list: List[Union[float, int, str]], file_path: Union[Path, str]):
    with open(file_path, "w") as f:
        for num in dump_list:
            f.write(str(num) + "\n")
