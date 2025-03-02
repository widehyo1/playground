awk "$1"'
function isdevice() { return $1 ~ /^[bc]/ } # devices
function islink()   { return $1 ~ /^L/ }    # symbolic links
function setuid()   { return $1 ~ /^.u/ }   # setuid files
function name()     { return $6 }
function size()     { return $5 }
function owner()    { return $2 }
function older(n)   { return $12 + n*86400 <= now } # older than n days
' now=`date -n` find.data
