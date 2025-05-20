function join(arr, sep) {
	acc = arr[1]
	for (i = 2; i <= length(arr); i++) {
		acc = acc sep arr[i]
	}
	return acc
}
function extractInfo(target, numOfAttrs, sep) {
	for (i = 1; i <= numOfAttrs; i++) {
		attr = lshift(1, i-1)
		reprArr[i] = and(target, attr) ? 1 : 0
	}
	return join(reprArr, sep)
}
BEGIN {
	FS = ""
}
{
	attr = lshift(1, NR-1)
	for (i = 1; i <= NF; i++) {
		result[$i] = or(result[$i], attr)
	}
}
END {
	for (idx in result) {
		print "result[" idx "]: " result[idx]
		print "information of " idx
		print(extractInfo(result[idx], NR, ","))
	}
}
