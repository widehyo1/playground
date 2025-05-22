/Slf4jSpyLogDelegator/ && /Connection.prepareStatement/{
    inBlock = 1
	content = substr($0, index($0, "(") + 1)
	next
}

/) returned net.sf.log4jdbc.sql.jdbcapi.PreparedStatementSpy/ {
	content = content "\n"  substr($0, 1, index($0, ") returned net.sf.log4jdbc.sql.jdbcapi.PreparedStatementSpy") - 1)
    sqlCount++
    sqlInfo[sqlCount] = content
	queryCounter[content]++
    inBlock = 0
}

inBlock {
    content = content "\n" $0
}



END {
	for (query in queryCounter) {
		counter++
		print ""
		print counter " th query execution count: " queryCounter[query]
		print query
	}

    print "distinct query count: " length(queryCounter)
}
