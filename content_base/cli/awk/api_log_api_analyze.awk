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

	# print ""
	# print "API start"
	# print apiType
	# print worker " " timestampstr
}
/\[curityContextPersistenceFilter] : Cleared SecurityContextHolder to complete request/ {

	worker = substr($0, 33, 10)
	if (workerStatusInfo[worker] == 1) {
		apiType = workerApiInfo["apiType",worker]
		apiCounter[apiType]++
		timestampstr = substr($0, 1, 23)
		endTimestamp = convertTime(timestampstr)
		apiElapsedArr[apiType,apiCounter[apiType]] = endTimestamp - workerTimeInfo["stime",worker]

		workerStatusInfo[worker] = 0
	}

	# print worker " " timestampstr
	# print "API ends"
	# print ""
}

END {
	print ""
	print "execution detail"
	print ""
	for (apiCounterIdx in apiCounter) {
		print ""
		print "api type: " apiCounterIdx "(" apiCounter[apiCounterIdx] ")"
		for (i = 1; i <= apiCounter[apiCounterIdx]; ++i) {
			print i "th execution takes " apiElapsedArr[apiCounterIdx,i] " sec"
		}
	}

	print ""
	print "summary"
	for (apiCounterIdx in apiCounter) {
		print apiCounterIdx " api executed " apiCounter[apiCounterIdx] " times"
	}

}
