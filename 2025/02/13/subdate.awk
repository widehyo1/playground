/@date/ {
"date +'%a., %h %d, %Y'" | getline today
gsub(/@date/, today)
}
{ print }
