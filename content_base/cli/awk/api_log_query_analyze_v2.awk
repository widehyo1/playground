/Slf4jSpyLogDelegator/ {
    inBlock = 1
    content = ""
}

/\{executed in/ {
    sqlCount++
    sqlInfo[sqlCount] = content
	query = substr(content, 80)
	elapsedLen = split($0, elapsedInfo)
	elapsedMsec = elapsedInfo[elapsedLen - 1]
	if (!queryElapsedArr[query,elapsedMsec]) {
		queryMsecCounter[query]++
		aggIdx = queryMsecCounter[query]
		queryIndexMapper[query,aggIdx] = elapsedMsec
	}
	queryElapsedArr[query,elapsedMsec]++
	queryCounter[query]++
    inBlock = 0
}

inBlock {
    content = content "\n" $0
}


END {
    for (query in queryCounter) {
        print ""
        print query
        print ""
		print "executed " queryCounter[query] " times"

        print "elapsed time distribution:"
        for (aggIdx = 1; aggIdx <= queryMsecCounter[query]; aggIdx++) {
			elapsedMsec = queryIndexMapper[query,aggIdx]
            print elapsedMsec " msec takes " queryElapsedArr[query,elapsedMsec] " times"
        }
    }

    print ""
    print "==="
    print ""
    print "success query count: " sqlCount
    print "distinct query count: " length(queryCounter)

}
