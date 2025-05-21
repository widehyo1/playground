function convertTime(timestampstr) {
	gsub(/[\- :\.]/, " ", timestampstr)
	return mktime(substr(timestampstr, 1, 19)) + substr(timestampstr, 21) / 1000
}
/\[              FilterChainProxy] : Securing/ {
	apiType = substr($0, 88)
	worker = substr($0, 33, 10)
	timestampstr = substr($0, 1, 23)
	timestamp = convertTime(timestampstr)

	workerTimeInfo["stime",worker] = timestamp
	workerStatusInfo[worker] = 1
	workerApiInfo["apiType",worker] = apiType

}
/\[curityContextPersistenceFilter] : Cleared SecurityContextHolder to complete request/ {

	worker = substr($0, 33, 10)
	if (workerStatusInfo[worker] == 1) {
		apiType = workerApiInfo["apiType",worker]
		apiCounter[apiType]++
		timestampstr = substr($0, 1, 23)
		endTimestamp = convertTime(timestampstr)
		elapsedTimeMsec = sprintf("%.0f", endTimestamp - workerTimeInfo["stime",worker] + 0.01)
		
		if (!apiElapsedArr[apiType,elapsedTimeMsec]) {
			apiTypeElapsedTimeCounter[apiType]++
			aggIdx = apiTypeElapsedTimeCounter[apiType]
			apiTypeElapsedTimeMapper[apiType,aggIdx] = elapsedTimeMsec
		}
		apiElapsedArr[apiType,elapsedTimeMsec]++

		workerStatusInfo[worker] = 0
	}

}

END {
	print ""
	print "execution detail"
	print ""
	for (apiType in apiCounter) {
		print ""
		print "api type: " apiType "(" apiCounter[apiType] ")"
		for (aggIdx = 1; aggIdx <= apiTypeElapsedTimeCounter[apiType]; aggIdx++) {
			elapsedTimeMsec = apiTypeElapsedTimeMapper[apiType, aggIdx]
			print "execution time: " elapsedTimeMsec "msec, count: " apiElapsedArr[apiType,elapsedTimeMsec]
		}
	}

	print ""
	print "summary"
	for (apiType in apiCounter) {
		print apiType " api executed " apiCounter[apiType] " times"
	}

}
