function snake_to_camel(text, result) {
  result = ""
  split(text, arr, "_")
  for (idx in arr) {
    result = result toupper(substr(arr[idx], 0, 1)) substr(arr[idx], 2)
  }
  result = tolower(substr(result, 0, 1)) substr(result, 2)
  return result
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
function camel_to_snake(text, result) {
  result = text
  while (match(result, /[A-Z]/) > 1) {
    result = substr(result, 0, RSTART - 1) "_" tolower(substr(result, RSTART, 1)) substr(result, RSTART + 1)
  }
  return result
}
{
  split("|",arr,$0)
  gsub(/^_+/, "", arr[0])
  if (match(arr[0], "_")) {
    print snake_to_camel(arr[0])
  } else if (match(arr[0], /[A-Z]/) > 1) {
    print camel_to_snake(arr[0])
  } else {
    print arr[0]
  }
}
