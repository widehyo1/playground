/^{$/ {
  isContent = 1
}
isContent {
  print $0
}
/^}$/ {
  isContent = 0
}
