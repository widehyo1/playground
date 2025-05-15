{
	if (substr($0,77,1) == ":") {
		logLevel = substr($0,25,7)
		location = substr($0,44,32)
		if (location == "[          Slf4jSpyLogDelegator]") {
			logMessage = substr($0,79)
			gsub(/[0-9]*\. /, "", logMessage)
		} else if (substr($0,79,33) == "JupyterHub API ERROR - 상태코드 : 404") {
			logMessage = substr($0,1,235) substr($0,265) # aggragating following format: date:"Wed, 03 Apr 2024 13:30:01 GMT"
			logMessage = substr(logMessage,79)
		} else {
			logMessage = substr($0,79)
		}
		gsub(/@[0-9A-Fa-f]{6,}/, "", logMessage)
		aggKey = logLevel " " location " " logMessage
		arr[aggKey]++
	} else {
		gsub(/@[0-9A-Fa-f]{6,}/, "", $0)
		arr[$0]++
	}
}
END {
	for (idx in arr) {
		print arr[idx] "|" idx
	}
}
