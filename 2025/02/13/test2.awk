{
    "yes 'test this line'" | getline str
    print str
    split(str, str_arr, " ")
    for (item in str_arr) {
        print item
        print str_arr[item]
        print "'test quote is expressed'"
    }
}
