awk '
function isort(A,left,right,   i,j,t) {
      for (i = left+1; i <= right; i++)
         for (j = i; j > 1 && ++comp && A[j-1] > A[j]; j--) {
            # swap A[j-1] and A[j]
            t = A[j-1]; A[j-1] = A[j]; A[j] = t; ++exch
         }
}

function hsort(A,left,right,  i) {
      for (i = int(right/2); i >= left; i--)
         heapify(A,i,right)
      for (i = right; i > left; i--) {
         swap(A,left,i)
         heapify(A,left,i-1)
      }
}

function heapify(A,left,right,   p,c) {
      for (p = left; (c = 2*p) <= right; p = c) {
         if (c < right && ++comp && A[c+1] > A[c])
            c++
         if (++comp && A[p] < A[c])
            swap(A,c,p)
      }
}

function qsort(A,left,right,   i,last) {
      if (left >= right)  # do nothing if array contains
         return           # at most one element
      swap(A, left, left + int((right-left+1)*rand()))
      last = left
      for (i = left+1; i <= right; i++)
         if (++comp && A[i] < A[left])
            swap(A, ++last, i)
      swap(A, left, last)
      qsort(A, left, last-1)
      qsort(A, last+1, right)
}

function swap(A,i,j,   t) {
      t = A[i]; A[i] = A[j]; A[j] = t; ++exch
}
# check:  is A[m..n] in increasing order

function check(A,m,n,   i) {
   for (i = m; i < n; i++)
      if (A[i] > A[i+1])
         print "error: array is not sorted"
}

function genone(A) { # put one integer in A
   A[1] = 1
}
function genran(A,left,right,   i) { # put n random integers in A
   for (i = left; i <= right; i++)
      A[i] = int(n*rand())
}
function gensor(A,left,right,   i) { # put n reverse sorted integers in A
   for (i = left; i <= right; i++)
      A[i] = right - i + 1
}
function genid(A,left,right,   i) { # put n identical integers in A
   for (i = left; i <= right; i++)
      A[i] = 1
}

BEGIN { # testing begins
   print "testing heap sort on"
   
   n = 1
   print "   " n " element"
   comp = exch = 0
   genone(A); hsort(A,1,n); check(A,1,n)
      print n, "comp", comp, "exch", exch, "sum", comp+exch
   
for (n = 20; n <= 100; n += 20) {
   
   print "   " n " reverse sorted integers"
   comp = exch = 0
   gensor(A,1,n); hsort(A,1,n); check(A,1,n)
      print n, "comp", comp, "exch", exch, "sum", comp+exch

   print "   " n " random integers"
   comp = exch = 0
   genran(A,1,n); hsort(A,1,n); check(A,1,n)
      print n, "comp", comp, "exch", exch, "sum", comp+exch
   
   print "   " n " identical integers"
   comp = exch = 0
   genid(A,1,n); hsort(A,1,n); check(A,1,n)
      print n, "comp", comp, "exch", exch, "sum", comp+exch
}
}
'
