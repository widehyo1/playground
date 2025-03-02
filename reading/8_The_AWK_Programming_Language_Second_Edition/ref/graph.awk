# graph - generate Python program to draw a graph

awk '
BEGIN {
  print "import matplotlib.pyplot as plt"
  print "import pandas as pd"
  print "df = pd.read_csv(\"temp\", sep=\" \")"
  print "plt.scatter(df[\"col1\"],df[\"col2\"])"  
  print "col1 col2" >"temp"
}
/xlabel|ylabel|title/ {
  label = $1; $1 = ""
  printf("plt.%s(\"%s\")\n", label, $0)
  next
}
NF == 1 { print ++n, $1 >"temp" }
NF == 2 { print $1, $2 >"temp" }
END { print "plt.show()" }
' $*
