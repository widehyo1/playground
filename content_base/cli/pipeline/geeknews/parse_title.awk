BEGIN {
  FS = "[<>]"
}
{
  print $5
}

