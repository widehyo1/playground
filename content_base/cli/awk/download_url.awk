@include "common"
BEGIN {
  FS = "/"
}
NR > 1 {
  path = substr($0, 25)
  idx = rindex(path, "/")
  printf "mkdir -p %s\n", substr(path, 1, idx)
  print "curl -XGET " $0 " -o " path

}

