import re
from typing import List, Dict


def parse_java_code(source_code: str) -> List[Dict]:
    classes = []

    class_pattern = r'\bclass\s+(\w+)'
    class_matches = list(re.finditer(class_pattern, source_code))

    for class_match in class_matches:
        class_name = class_match.group(1)

        attributes = extract_attributes(source_code)
        methods = extract_methods(source_code)

        classes.append({
            "name": class_name,
            "attributes": attributes,
            "methods": methods
        })

    return classes


def extract_attributes(source_code: str) -> List[str]:
    attribute_pattern = r'\b(private|public|protected)\s+[\w<>\[\]]+\s+(\w+)\s*(=.+)?;'
    matches = re.findall(attribute_pattern, source_code)

    attributes = []
    for match in matches:
        attribute_name = match[1]
        attributes.append(attribute_name)

    return attributes


def extract_methods(source_code: str) -> List[str]:
    method_pattern = r'\b(private|public|protected)\s+[\w<>\[\]]+\s+(\w+)\s*\([^)]*\)\s*\{'
    matches = re.findall(method_pattern, source_code)

    methods = []
    for match in matches:
        method_name = match[1]

        if method_name not in ["if", "for", "while", "switch"]:
            methods.append(method_name)

    return methods