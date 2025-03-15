import re
import sys
from pathlib import Path

PROTO_TYPE_MAPPING = {
    "string": "str",
    "int32": "int",
    "int64": "int",
    "uint32": "int",
    "uint64": "int",
    "float": "float",
    "double": "float",
    "bool": "bool",
    "bytes": "bytes",
}

def parse_proto_file(proto_file):
    """Parses a .proto file and extracts message definitions."""
    with open(proto_file, "r") as f:
        lines = f.readlines()

    messages = {}
    current_message = None
    for line in lines:
        line = line.strip()

        # Start of a new message
        match = re.match(r"message (\w+) {", line)
        if match:
            current_message = match.group(1)
            messages[current_message] = []
            continue

        # End of message
        if line == "}":
            current_message = None
            continue

        # Parse fields inside a message
        if current_message:
            field_match = re.match(r"(\w+) (\w+) = \d+;", line)
            if field_match:
                field_type, field_name = field_match.groups()
                python_type = PROTO_TYPE_MAPPING.get(field_type, field_type)  # Handle custom types
                messages[current_message].append((field_name, python_type))

    return messages

def generate_dataclasses(messages):
    """Generates Python dataclasses from parsed messages."""
    dataclasses_code = ["from dataclasses import dataclass\n"]
    
    for message, fields in messages.items():
        dataclasses_code.append(f"@dataclass\nclass {message}:")
        if not fields:
            dataclasses_code.append("    pass  # Empty message")
        else:
            for field_name, field_type in fields:
                dataclasses_code.append(f"    {field_name}: {field_type}")
        dataclasses_code.append("")  # Add newline

    return "\n".join(dataclasses_code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python proto_to_dataclass.py <file.proto>")
        sys.exit(1)

    proto_file = sys.argv[1]
    if not Path(proto_file).exists():
        print(f"Error: File {proto_file} not found.")
        sys.exit(1)

    messages = parse_proto_file(proto_file)
    dataclasses_code = generate_dataclasses(messages)

    output_file = Path(proto_file).with_suffix(".py")
    with open(output_file, "w") as f:
        f.write(dataclasses_code)

    print(f"Generated dataclasses saved in {output_file}")

