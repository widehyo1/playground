function trim(str) { sub(/^[[:space:]]+/, "", str); sub(/[[:space:]]+$/, "", str); return str }
function indent_level(line, w) { match(line, /^[[:space:]]*/); return RLENGTH / w }

function parse(line,   lvl, key, val, sepPos) {
    lvl = indent_level(line, INDENT)
    sepPos = index(line, ":")
    if (sepPos) {
        key = trim(substr(line, 1, sepPos - 1))
        val = trim(substr(line, sepPos + 1))
    } else {
        key = trim(line); val = ""
    }
    return lvl SUBSEP key SUBSEP val   # 복합 반환(key,value,lvl)
}

function set_path(lvl, key,   i) {
    stackLen = lvl                          # 깊이 초과분 미리 drop
    stack[++stackLen] = key                 # push/replace
}

function join_path(   i, s){
    s = stack[1]
    for (i = 2; i <= stackLen; i++) s = s "." stack[i]
    return s
}

function print_prop(val,   path) {
    path = join_path()
    printf "-D%s=%s", path, val
    if (!LAST) print " \\"      # 마지막 줄이면 줄바꿈만
    else       print ""
}

BEGIN { INDENT = 2 }

/^[[:space:]]*#/ || /^[[:space:]]*$/ { next } # skip

{
    line = $0
    gsub(/#[^"']*$/, "", line)               # 따옴표 안의 # 유지
    info = parse(line)                       # "lvl<ss>key<ss>val"
    split(info, f, SUBSEP)
    lvl = f[1]; key = f[2]; val = f[3]

    set_path(lvl, key)
    if (val != "") {
        props++
        prop_val[props] = val
        print_prop(val)
    }
}

END {
    # 마지막 역슬래시 제거 이미 처리됨
}
