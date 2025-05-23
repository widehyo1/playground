function strip(str) {
  gsub(/^\s+|\s+$/, "", str)
  return str
}

function snakeToCamel(text, result) {
  result = ""
  upflag = 0
  for (i = 1; i <= length(text); i++) {
    curchar = substr(text, i, 1)
    if (curchar == "_") {
      upflag = 1
      continue
    }
    if (upflag) {
      upflag = 0
      curchar = toupper(curchar)
    }
    result = result curchar
  }
  result = tolower(substr(result, 0, 1)) substr(result, 2)
  return result
}

function toGetMethod(str) {
  return "get" toupper(substr(str, 1, 1)) substr(str, 2)
}

BEGIN {
  FS = "|"
}

NR >= 55 && NR <= 58 {
  var = snakeToCamel(strip($2))
  print "quotaIaasVgpu.put(\"" var "\", this." toGetMethod(var) "());"
}
