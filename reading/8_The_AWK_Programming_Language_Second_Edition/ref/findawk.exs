find.awk 'isdevice() && name() !~ "^/dev/"'

find.awk 'setuid() && owner() == 0'

find.awk 'name() ~ /[.]o$/ && older(7) { n++; sum += size() }
          END { print n, sum }'
