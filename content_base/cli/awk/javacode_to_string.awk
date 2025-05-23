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
  className = "QuotaIaasVgpu"
  firstColumnFlag = 1
  print "StringBuilder builder = new StringBuilder();"
  print "builder.append = new StringBuilder();"
}

NR >= 55 {
  inBlock = 1
}
inBlock {
  var = snakeToCamel(strip($2))
  if (firstColumnFlag) {
    print "builder.append(\"" className " [" var "=\");"
    print "builder.append(" var ");"
    firstColumnFlag = 0
    next
  }
  # print "quotaIaasVgpu.put(\"" var "\", this." toGetMethod(var) "());"
  print "builder.append(\", " var "=\");"
  print "builder.append(" var ");"
}
NR >= 59 {
  exit
}

END {
  print "builder.append(\"]\");"
}
