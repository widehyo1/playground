$2 > 30 { n++; pay += $2 * $3 }

END     { if (n > 0) {
             print n, "employees, total pay is", pay,
                      "  average pay is", pay/n
          } else {
             print "No employees are paid more than $30/hour"
          }
        }
