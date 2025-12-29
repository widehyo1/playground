# Fundamentals_of_Data_Visulization

## ch6

okabeito_colors()
#>     orange light blue      green      amber       blue        red     purple 
#>  "#E69F00"  "#56B4E9"  "#009E73"  "#F5C710"  "#0072B2"  "#D55E00"  "#CC79A7" 
#>       grey      black 
#>  "#999999"  "#000000" 

okabeito_colors(c("red", "light blue", "orange"))
#>        red light blue     orange 
#>  "#D55E00"  "#56B4E9"  "#E69F00" 

okabeito_colors(original_names = TRUE)
#>         orange       sky blue   bluish green          amber           blue 
#>      "#E69F00"      "#56B4E9"      "#009E73"      "#F5C710"      "#0072B2" 
#>     vermillion reddish purple           grey          black 
#>      "#D55E00"      "#CC79A7"      "#999999"      "#000000" 

okabeito_colors(black_first = TRUE)
#>      black     orange light blue      green      amber       blue        red 
#>  "#000000"  "#E69F00"  "#56B4E9"  "#009E73"  "#F5C710"  "#0072B2"  "#D55E00" 
#>     purple       grey 
#>  "#CC79A7"  "#999999" 

```dat
rank,title,weekly amount(million USD)
1,Star Wars: The Last Jedi,71565498
2,Jumanji: Welcome to the Jungle,36169328
3,Pitch Perfect 3,19928525
4,The Greatest Showman,8805843
5,Ferdinand,7316746
```



set datafile missing "null"
set datafile separator ","
set key autotitle columnhead

set style data histogram
set style fill solid border -1
set ylabel "weekly amount(million USD)"
set yrange [0:72]
set xtics rotate by -45
set boxwidth 2
unset key

set palette defined ( \
    0  "#E69F00", \
    1  "#56B4E9", \
    2  "#009E73", \
    3  "#F5C710", \
    4  "#0072B2", \
    5  "#D55E00", \
    6  "#CC79A7", \
    7  "#999999", \
    8  "#000000" )

plot '~/temp.dat' using 3:xtic(2):1 ti col

pause -1 "Hit return to continue"


"/home/widehyo/script.dem" line 24: Too many columns in using specification
