import re

def regex_extract(text):
    pattern = r"```(?:\w+)?\n([\s\S]*?)```"

    match = re.search(pattern, text)

    output = match.group(1) if match else None

    return output