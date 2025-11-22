from ast import Node
from dataclasses import asdict, is_dataclass


def ast_to_json(node):
    if is_dataclass(node):
        data = asdict(node)

        # 再帰処理
        for key, value in data.items():
            if isinstance(value, Node):
                data[key] = ast_to_json(value)
            elif isinstance(value, list):
                data[key] = [ast_to_json(v) if isinstance(v, Node) else v for v in value]

        return {
            "type": node.__class__.__name__,
            "value": data
        }

    return node
