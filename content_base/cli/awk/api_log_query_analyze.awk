function strip(str) {
    gsub(/^\s+|\s+$/, "", str)
    return str
}

function getLastIndex(idx) {
    # 2) Build a greedy pattern that eats everything up to the *last* sep
    regex = ".*" SUBSEP

    # 3) Remove that prefix in one go—what’s left is your last field
    sub(regex, "", idx)

    return idx
}

function lastSplit(str, sep,    safe_sep, regex) {
    # 1) Escape any regex-meta chars in sep
    safe = sep
    gsub(/[][().*+?^${}|\\]/, "\\\\&", safe)

    # 2) Build a regex that captures:
    #    (.*) <last-sep> ([^sep]* ) from start to end
    regex = "^(.*)" safe "([^" safe "]*)$"

    # 3) Use match() with an array to pull out the groups
    if (match(str, regex, tmp)) {
        out["head"] = tmp[1]
        out["tail"] = tmp[2]
    } else {
        out["head"] = ""
        out["tail"] = str
    }
}

/Slf4jSpyLogDelegator/ {
    startNR = NR
    inBlock = 1
    content = ""
}

inBlock {
    content = content "\n" $0
}

/\{executed in/ {
    endNR = NR
    sqlCount++
    sqlInfo[sqlCount] = content
    inBlock = 0
}

END {
    for (sqlIdx in sqlInfo) {
        # logHead = substr(sqlInfo[sqlIdx], 1, 79)
        # executionTimeStamp = substr(sqlInfo[sqlIdx], 1, 24)
        logContent = substr(sqlInfo[sqlIdx], 80)
        lastSplit(logContent, "\n")

        query = out["head"]
        elapsed = out["tail"]

        split(elapsed, elapsedArr)
        elapsedArrLength = length(elapsedArr)
        elapsedMsec = elapsedArr[elapsedArrLength - 1]

        if (!queryCountInfo["count",query]++) {
            queryCounter++
            queries[queryCounter] = query
        }
        # queryExecutionTimestampInfo["executionTimeStamp",query] = queryExecutionTimestampInfo["executionTimeStamp",query] "|" strip(executionTimeStamp)
        # queryElapsedTimeInfo["elapsed",query] = queryElapsedTimeInfo["elapsed",query] "|" strip(elapsed)
        queryElapsedTimeCounterInfo["elapsedCounter", query, elapsedMsec]++

    }

    for (queryIdx in queries) {
        print ""
        query = queries[queryIdx]
        print queryIdx "th query executed " queryCountInfo["count",query] " times"

        print ""
        print queries[queryIdx]
        print ""
        # print "execution times:"
        # print queryExecutionTimestampInfo["executionTimeStamp",query]
        # print "elapsed times:"
        # print queryElapsedTimeInfo["elapsed",query]
        print "elapsed time distribution:"
        for (queryElapsedTimeCounterIdx in queryElapsedTimeCounterInfo) {
            split(queryElapsedTimeCounterIdx, qetciArr, SUBSEP)
            curQuery = qetciArr[2]
            if (curQuery != query) {
                continue
            }
            elapsedMsec = qetciArr[3]
            print elapsedMsec " msec takes " queryElapsedTimeCounterInfo[queryElapsedTimeCounterIdx] " times"
        }
    }


    print ""
    print "==="
    print ""
    print "success query count: " sqlCount
    print "distinct query count: " length(queryCountInfo)

}

