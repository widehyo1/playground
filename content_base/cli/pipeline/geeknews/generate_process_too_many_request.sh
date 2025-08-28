#!/bin/bash
echo "#!/bin/bash" > process_too_many_request.sh
wc -l html/* \
| awk '$1 < 100 { print $0 }' \
| cut -d "/" -f2 \
| cut -d "." -f1 \
| awk '{ printf "curl -X GET https://news.hada.io/topic?id=%s > html/%s.html\n", $0, $0 }' >> process_too_many_request.sh

