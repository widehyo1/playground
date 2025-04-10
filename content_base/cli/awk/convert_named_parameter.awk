{
    term = substr($1,0,length($1)-1)
    print term "=" term ","
}
