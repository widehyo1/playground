NF != 3   { print $0, "number of fields is not equal to 3" }
$2 < 15   { print $0, "rate is too low" }
$2 > 25   { print $0, "rate exceeds $25 per hour" }
$3 < 0    { print $0, "negative hours worked" }
$3 > 60   { print $0, "too many hours worked" }
