/mnt/d/gitclone/checkpoint/stackoverflow $ time 7z e -so stackoverflow.com-Votes.7z | awk 'BEGIN { FS = "\""; print "id,post_id,vote_type_id,creation_date" } /row/ { printf "%s,%s,%s,%s\n",$2,$4,$6,$8 }' | gzip -9 > Votes.csv.gz

real    26m13.813s
user    35m9.475s
sys     2m3.366s



```awk
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
```

```awk
BEGIN {
  FS = "\""
  print "id,post_id,score,text,creation_date,user_id"
}
/row/ {
  if (index($8, ",")) {
    $8 = "\"" $8 "\""
  }
  printf "%s,%s,%s,%s,%s,%s\n",$2,$4,$6,$8,$10,$12
}
```


| awk 'BEGIN { FS = "\""; print "id,post_id,score,text,creation_date,user_id" } /row/ { printf "%s,%s,%s,%s,%s,%s\n",$2,$4,$6,$8,$10,$12 }'
  <row Id="134691651" PostId="264" Score="0" Text="@PeterCordes Thanks for the correction. I've been fixing typos and grammar in some of the oldest questions here. Mistakes happen (occasionally)." CreationDate="2023-06-01T16:29:01.453" UserId="13407802" />


/mnt/d/gitclone/checkpoint/stackoverflow $ time 7z e -so stackoverflow.com-Posts.7z | awk -f ./post_to_csv.awk | pigz -9 > Posts.csv.gz

real    97m37.508s
user    221m23.812s
sys     15m40.647s

/mnt/d/gitclone/checkpoint/stackoverflow $ duckdb
DuckDB v1.4.0 (Andium) b8a06e4a22
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D set memory_limit = '7GB';
D select * from 'Posts.csv.gz';
 12% ▕████▌                                 ▏ (~6.6 minutes remaining)  Killed
/mnt/d/gitclone/checkpoint/stackoverflow $ duckdb
DuckDB v1.4.0 (Andium) b8a06e4a22
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D select count(1) from 'Posts.csv.gz';
100% ▕██████████████████████████████████████▏ (00:10:25.25 elapsed)
┌─────────────────┐
│    count(1)     │
│      int64      │
├─────────────────┤
│    59819048     │
│ (59.82 million) │
└─────────────────┘
D select * from read_csv('Posts.csv.gz') limit 1;
┌───────┬──────────────┬────────────────────┬──────────────────────┬───────┬────────────┬───┬──────────────┬───────────────┬────────────────┬─────────────┬──────────────────────┬─────────────────┐
│  id   │ post_type_id │ accepted_answer_id │    creation_date     │ score │ view_count │ … │ answer_count │ comment_count │ favorite_count │ closed_date │ community_owned_date │ content_license │
│ int64 │    int64     │       int64        │      timestamp       │ int64 │   int64    │   │    int64     │     int64     │     int64      │  timestamp  │      timestamp       │     varchar     │
├───────┼──────────────┼────────────────────┼──────────────────────┼───────┼────────────┼───┼──────────────┼───────────────┼────────────────┼─────────────┼──────────────────────┼─────────────────┤
│ 38779 │      1       │       40472        │ 2008-09-02 03:41:0…  │   6   │    6282    │ … │      2       │       0       │       0        │ NULL        │ NULL                 │ CC BY-SA 2.5    │
├───────┴──────────────┴────────────────────┴──────────────────────┴───────┴────────────┴───┴──────────────┴───────────────┴────────────────┴─────────────┴──────────────────────┴─────────────────┤
│ 1 rows                                                                                                                                                                     21 columns (12 shown) │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
/mnt/d/gitclone/checkpoint/stackoverflow $ duckdb
DuckDB v1.4.0 (Andium) b8a06e4a22
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D .mode line
D select * from read_csv('Posts.csv.gz') limit 1;
                      id = 38779
            post_type_id = 1
      accepted_answer_id = 40472
           creation_date = 2008-09-02 03:41:06.88
                   score = 6
              view_count = 6282
                    body = &lt;p&gt;I have a wcf application hosted in a windows service running a local windows account. Do I need to set an SPN for this account? If so, what's the protocol the SPN needs to be set under? I know how to do this for services over HTTP, but have never done it for net.tcp.&lt;/p&gt;&#xA;
           owner_user_id = 781
      owner_display_name = Esteban
     last_editor_user_id = 1116
last_editor_display_name = John Nolan
          last_edit_date = 2008-09-02 08:49:19.323
      last_activity_date = 2013-06-24 17:03:55.833
                   title = What SPN do I need to set for a net.tcp service?
                    tags = |wcf|security|spn|
            answer_count = 2
           comment_count = 0
          favorite_count = 0
             closed_date = NULL
    community_owned_date = NULL
         content_license = CC BY-SA 2.5
