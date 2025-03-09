import re
from functools import reduce

def gen_camel_to_snake(text):
    matches = re.finditer('[A-Z]', text)
    target_positions = {mat.start() for mat in matches}
    for idx, ch in enumerate(text):
        if idx in target_positions:
            yield from f"_{ch.lower()}"
        else:
            yield ch

def camel_to_snake(text):
    res = "".join(gen_camel_to_snake(text))
    return res

def snake_to_camel(text):
    head, *tails = text.split("_")
    return reduce(lambda acc, cur: f"{acc}{cur[0].upper()}{cur[1:]}", tails, head)

def swap_camel_snake(text: str) -> str:
    leading_underscore_pattern = re.compile(r"^_+")
    # discards leading underscores
    text = re.sub(leading_underscore_pattern, "", text)
    if re.search("_", text):
        return snake_to_camel(text)
    elif re.search('[A-Z]', text):
        return camel_to_snake(text)
    return text

if __name__ == '__main__':
    test_cases = ["groupName" ,"group_name" ,"__createdDate" ,"createdDate"
            ,"__created_date" ,"created_date" ,"modifiedDate" ,"modified_date"
            ,"joinSepDelemeter" ,"join_sep_delemeter", ]
    for text in test_cases:
        print(swap_camel_snake(text))
