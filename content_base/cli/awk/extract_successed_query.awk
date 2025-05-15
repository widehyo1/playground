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
    sqlInfo[sqlCount,1] = startNR
    sqlInfo[sqlCount,2] = endNR
    sqlInfo[sqlCount,3] = content

    loggerHead = substr(content, 1, 79)
    executionTimeStamp = substr(loggerHead, 1, 23)
    content = substr(content, 80)

    lastSplit(content, "\n")
    query = out["head"]
    elapsed = out["tail"]

    sqlInfo[sqlCount,4] = query
    sqlInfo[sqlCount,5] = elapsed
    sqlInfo[sqlCount,6] = loggerHead
    sqlInfo[sqlCount,7] = executionTimeStamp
    inBlock = 0
}

END {
    for (sqlIdx in sqlInfo) {
        split(sqlIdx, nrInfo, SUBSEP)
		if (!uniq[nrInfo[1]]++) {
			print ""
			print "success query count: " nrInfo[1]
			print "line info [from: " sqlInfo[nrInfo[1],1] ", to: " sqlInfo[nrInfo[1],2] "]"
			print sqlInfo[nrInfo[1],3]
            print "query is:"
			print sqlInfo[nrInfo[1],4]
            print "elapsed is:"
			print sqlInfo[nrInfo[1],5]
            print "loggerHead is:"
			print sqlInfo[nrInfo[1],6]
            print "executionTimeStamp is:"
			print sqlInfo[nrInfo[1],7]
		}
    }
}

