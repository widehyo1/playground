BEGIN {
  FS = "\""
  arr["  <row Id="] = 1
  arr[" PostTypeId="] = 2
  arr[" AcceptedAnswerId="] = 3
  arr[" CreationDate="] = 4
  arr[" Score="] = 5
  arr[" ViewCount="] = 6
  arr[" Body="] = 7
  arr[" OwnerUserId="] = 8
  arr[" OwnerDisplayName="] = 9
  arr[" LastEditorUserId="] = 10
  arr[" LastEditorDisplayName="] = 11
  arr[" LastEditDate="] = 12
  arr[" LastActivityDate="] = 13
  arr[" Title="] = 14
  arr[" Tags="] = 15
  arr[" AnswerCount="] = 16
  arr[" CommentCount="] = 17
  arr[" FavoriteCount="] = 18
  arr[" ClosedDate="] = 19
  arr[" CommunityOwnedDate="] = 20
  arr[" ContentLicense="] = 21
  print "id,post_type_id,accepted_answer_id,creation_date,score,view_count,body,owner_user_id,owner_display_name,last_editor_user_id,last_editor_display_name,last_edit_date,last_activity_date,title,tags,answer_count,comment_count,favorite_count,closed_date,community_owned_date,content_license"
}
/row/{
  for ( i = 2; i <= NF; i = i + 2) {
    if (index($i, ",")) {
      $i = "\"" $i "\""
    }
    arr2[arr[$(i-1)]]=$i
  }
  printf "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n", arr2[1],  arr2[2],  arr2[3],  arr2[4],  arr2[5], arr2[6],  arr2[7],  arr2[8],  arr2[9],  arr2[10], arr2[11], arr2[12], arr2[13], arr2[14], arr2[15], arr2[16], arr2[17], arr2[18], arr2[19], arr2[20], arr2[21]
}
