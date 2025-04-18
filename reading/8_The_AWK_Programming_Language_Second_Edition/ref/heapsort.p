# heapsort

    { _LBcnt[3]++;  A[NR] = $0 }

END { _LBcnt[5]++;  hsort(A, NR)
      for (i = 1; i <= NR; i++)
          { _LBcnt[7]++;  print A[i] }
    }

function hsort(A,n,  i) { _LBcnt[10]++; 
    for (i = int(n/2); i >= 1; i--)  # phase 1
         { _LBcnt[12]++;  heapify(A, i, n) }
    for (i = n; i > 1; i--) { _LBcnt[13]++;         # phase 2
         { _LBcnt[14]++;  swap(A, 1, i) }
         { _LBcnt[15]++;  heapify(A, 1, i-1) }
    }
}
function heapify(A,left,right,   p,c) { _LBcnt[18]++; 
    for (p = left; (c = 2*p) <= right; p = c) { _LBcnt[19]++; 
        if (c < right && A[c+1] > A[c])
            { _LBcnt[21]++;  c++ }
        if (A[p] < A[c])
            { _LBcnt[23]++;  swap(A, c, p) }
    }
}
function swap(A,i,j,   t) { _LBcnt[26]++; 
    t = A[i]; A[i] = A[j]; A[j] = t
}
END { for (i = 1; i <= 28; i++)
		 print _LBcnt[i] > "prof.cnts"
}
