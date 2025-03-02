/Asia/   { pop["Asia"] += $3 }
/Africa/ { pop["Africa"] += $3 }
END      { print "Asian population", pop["Asia"], "million"
           print "African population", pop["Africa"], "million"
         }
