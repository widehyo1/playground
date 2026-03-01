BEGIN {
  FS = ","
  CONVFMT = "%2.2f"
  OFS = ","
}
{
  if ($6 ~ /KRW/) {
    $6 = "USD"
    $5 /= 1440
    $7 /= 1440
  }
  print $0
}

