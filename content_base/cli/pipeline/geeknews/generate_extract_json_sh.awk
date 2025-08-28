BEGIN {
  FS = "="
  print "#!/bin/bash"
}
{
  printf "curl -X GET %s > html/%s.html\n", $0, $2
}
