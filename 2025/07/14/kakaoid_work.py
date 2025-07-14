from itertools import groupby

def solution(new_id):
    print("start")
    print(new_id)
    vaild_special = {"-", "_", "."}
    new_id = new_id.lower()
    print("step1:")
    print(new_id)
    new_id = ''.join(char for char in new_id if char.isalnum() or char in vaild_special)
    print("step2:")
    print(new_id)
    new_id = ''.join(gen_group_dot(new_id))
    print("step3:")
    print(new_id)
    if new_id == ".":
        new_id = ""
    if len(new_id):
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    print("step4:")
    print(new_id)
    if not new_id:
        new_id = "a"
    print("step5:")
    print(new_id)

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    print("step6:")
    print(new_id)
    if len(new_id) == 2:
        new_id = new_id + new_id[-1]
    if len(new_id) == 1:
        new_id = new_id * 3
    print("step7:")
    print(new_id)
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
