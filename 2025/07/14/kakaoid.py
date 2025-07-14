from itertools import groupby

def solution(new_id):
    vaild_special = {"-", "_", "."}
    new_id = new_id.lower()
    new_id = ''.join(char for char in new_id if char.isalnum() or char in vaild_special)
    new_id = ''.join(gen_group_dot(new_id))
    if new_id == ".":
        new_id = ""
    if len(new_id):
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if not new_id:
        new_id = "a"

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) == 2:
        new_id = new_id + new_id[-1]
    if len(new_id) == 1:
        new_id = new_id * 3
    return new_id


def gen_group_dot(new_id):
    for groupper, iterator in groupby(new_id):
        if groupper == ".":
            yield "."
            continue
        yield from iterator


# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))
