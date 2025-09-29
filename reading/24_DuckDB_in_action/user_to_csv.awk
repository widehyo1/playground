BEGIN {
  FS = "\""
  arr["  <row Id="]       = 1
  arr[" Reputation="]     = 2
  arr[" CreationDate="]   = 3
  arr[" DisplayName="]    = 4
  arr[" LastAccessDate="] = 5
  arr[" WebsiteUrl="]     = 6
  arr[" Location="]       = 7
  arr[" AboutMe="]        = 8
  arr[" Views="]          = 9
  arr[" UpVotes="]        = 10
  arr[" DownVotes="]      = 11
  arr[" AccountId="]      = 12
  print "id,reputation,creation_date,display_name,last_access_date,website_url,location,about_me,views,up_votes,down_votes,account_id"
}
/row/ {
  for ( i = 2; i <= NF; i = i + 2) {
    # print $(i-1)
    # print arr[$(i-1)]
    if (index($i, ",")) {
      $i = "\"" $i "\""
    }
    arr2[arr[$(i-1)]]=$i
    # print $i
    # printf "%s,",
  }
  printf "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n", arr2[1], arr2[2], arr2[3], arr2[4], arr2[5], arr2[6], arr2[7], arr2[8], arr2[9], arr2[10], arr2[11], arr2[12]
}
