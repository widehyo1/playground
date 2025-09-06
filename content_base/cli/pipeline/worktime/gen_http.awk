{
  year = substr($0,1,4)
  month = substr($0,5)
  printf "### %s\n", $0
  printf "GET http://14.35.255.248:8080/monacoPms/api/month/list?year=%s&month=%s\n", year, month
  print "Cookie: session-id=; saved_id="
  print ""
}
