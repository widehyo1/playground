## install DuckDB

[DuckDB Installation – DuckDB](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=linux&download_method=direct&architecture=x86_64)
`curl https://install.duckdb.org | sh`


```txt
vim.keymap.set('n', '<space>`', 'yiwcw``"0P')
vim.keymap.set('v', '<space>`', 'ygvc``"0P')
vim.keymap.set('n', '<space>"', 'yiwcw"""0P')
vim.keymap.set('v', '<space>"', 'ygvc"""0P')
vim.keymap.set('n', '<space>\'', 'yiwcw\'\'"0P')
vim.keymap.set('v', '<space>\'', 'ygvc\'\'"0P')
vim.keymap.set('n', '<space>(', 'yiwcw()"0P')
vim.keymap.set('v', '<space>(', 'ygvc()"0P')
vim.keymap.set('n', '<space>[', 'yiwcw[]"0P')
vim.keymap.set('v', '<space>[', 'ygvc[]"0P')
vim.keymap.set('n', '<space><', 'yiwcw<>"0P')
vim.keymap.set('v', '<space><', 'ygvc<>"0P')
vim.keymap.set('n', '<space>{', 'yiwcw{}"0P')
vim.keymap.set('v', '<space>{', 'ygvc{}"0P')
```

```awk
function strip(str) {
  gsub(/^\s+|\s+$/, "", str)
  return str
}
BEGIN {
  FS = "'"
}
{
  gsub(/vim.keymap.set\(/, "", $0)
  gsub(/^'n',/, "nnoremap", $0)
  gsub(/^'v',/, "vnoremap", $0)
  if (NF == 5) {
    printf "%s %s %s\n", strip($1), $2, $4
  } else {
    gsub(/\\'/, "'", $0)
    printf "%s %s' %s''%s\n", strip($1), $2, $5, $7
  }
}
```

```vim
nnoremap <space>` yiwcw``"0P
vnoremap <space>` ygvc``"0P
nnoremap <space>" yiwcw"""0P
vnoremap <space>" ygvc"""0P
nnoremap <space>' yiwcw''"0P
vnoremap <space>' ygvc''"0P
nnoremap <space>( yiwcw()"0P
vnoremap <space>( ygvc()"0P
nnoremap <space>[ yiwcw[]"0P
vnoremap <space>[ ygvc[]"0P
nnoremap <space>< yiwcw<>"0P
vnoremap <space>< ygvc<>"0P
nnoremap <space>{ yiwcw{}"0P
vnoremap <space>{ ygvc{}"0P
```

```sql
D describe select * from 'https://oedi-data-lake.s3.amazonaws.com/pvdaq/csv/systems.csv';
┌────────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│    column_name     │ column_type │  null   │   key   │ default │  extra  │
│      varchar       │   varchar   │ varchar │ varchar │ varchar │ varchar │
├────────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ system_id          │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ system_public_name │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ site_id            │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ site_public_name   │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ site_location      │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ site_latitude      │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ site_longitude     │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ site_elevation     │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
└────────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┘
```

```vim
iabbrev <buffer> \ctable; CREATE TABLE table_name ();
iabbrev <buffer> \ctas; CREATE TABLE table_name AS SELECT * FROM ref_table;
iabbrev <buffer> \atable; ALTER TABLE table_name ;
iabbrev <buffer> \cseq; CREATE SEQUENCE sequence_name INCREMENT BY 1;
iabbrev <buffer> \cview; CREATE VIEW v_name AS SELECT * FROM ref_table;

iabbrev <buffer> \ine; IF NOT EXISTS
iabbrev <buffer> \orr; OR REPLACE
iabbrev <buffer> \alt; ALTER
iabbrev <buffer> \tab; TABLE
iabbrev <buffer> \col; COLUMN

iabbrev <buffer> \def; DEFAULT
iabbrev <buffer> \nn; NOT NULL
iabbrev <buffer> \pk; PRIMARY KEY
iabbrev <buffer> \fk; FOREIGN KEY
iabbrev <buffer> \uniq; CONSTRAINT name_uk UNIQUE (column)
iabbrev <buffer> \ref; REFERENCES ref_table (column)

iabbrev <buffer> \int; INTEGER
iabbrev <buffer> \time; TIMESTAMP

iabbrev <buffer> \with; WITH cte_name AS ( SELECT * FROM table_name )

iabbrev <buffer> \select; SELECT * FROM table_name
iabbrev <buffer> \count; SELECT count(1) FROM table_name
iabbrev <buffer> \case; CASE WHEN condition THEN value ELSE evalue END
iabbrev <buffer> \csv; read_csv_auto()

iabbrev <buffer> \join; JOIN target t ON t.id = source.id
iabbrev <buffer> \ljoin; LEFT OUTER JOIN target t ON t.id = source.id
iabbrev <buffer> \rjoin; RIGHT OUTER JOIN target t ON t.id = source.id
iabbrev <buffer> \fjoin; FULL OUTER JOIN target t ON t.id = source.id

iabbrev <buffer> \grp; GROUP BY
iabbrev <buffer> \grpa; GROUP BY ALL
iabbrev <buffer> \ord; ORDER BY
iabbrev <buffer> \orda; ORDER BY ALL

iabbrev <buffer> \insert; INSERT INTO table_name VALUES ();
iabbrev <buffer> \byname; BY NAME
iabbrev <buffer> \oconf; ON CONFLICT
iabbrev <buffer> \nop; DO NOTHING

```

```sql
D SELECT year(read_on) AS YEAR
       , system_id
       , count(*)
       , round(sum(power) / 4 / 1000, 2) AS kwh
  FROM readings
  GROUP BY GROUPING
  SETS ((YEAR
       , system_id), YEAR, ())
  ORDER BY YEAR NULLS FIRST, system_id NULLS FIRST;
┌───────┬───────────┬──────────────┬───────────┐
│ YEAR  │ system_id │ count_star() │    kwh    │
│ int64 │   int32   │    int64     │  double   │
├───────┼───────────┼──────────────┼───────────┤
│  NULL │      NULL │       151879 │ 401723.22 │
│  2019 │      NULL │       103621 │ 269303.39 │
│  2019 │        10 │        33544 │   1549.34 │
│  2019 │        34 │        35040 │  205741.9 │
│  2019 │      1200 │        35037 │  62012.15 │
│  2020 │      NULL │        48258 │ 132419.83 │
│  2020 │        10 │        14206 │    677.14 │
│  2020 │        34 │        17017 │ 101033.35 │
│  2020 │      1200 │        17035 │  30709.34 │
└───────┴───────────┴──────────────┴───────────┘
```
```sql
D WITH ranked_reading AS
    (SELECT *
          , dense_rank() OVER (
                               ORDER BY power DESC) AS rnk
     FROM readings)
  SELECT *
  FROM ranked_reading
  WHERE rnk <= 3
  ;
┌───────────┬─────────────────────┬───────────────┬───────┐
│ system_id │       read_on       │     power     │  rnk  │
│   int32   │      timestamp      │ decimal(10,3) │ int64 │
├───────────┼─────────────────────┼───────────────┼───────┤
│        34 │ 2019-05-28 11:45:00 │    133900.000 │     1 │
│        34 │ 2020-04-02 11:30:00 │    133900.000 │     1 │
│        34 │ 2019-05-08 12:15:00 │    133900.000 │     1 │
│        34 │ 2019-05-23 11:30:00 │    133900.000 │     1 │
│        34 │ 2019-05-23 10:00:00 │    133900.000 │     1 │
│        34 │ 2019-05-10 12:15:00 │    133700.000 │     2 │
│        34 │ 2019-05-09 10:30:00 │    133700.000 │     2 │
│        34 │ 2019-03-21 13:00:00 │    133600.000 │     3 │
│        34 │ 2019-04-02 10:30:00 │    133600.000 │     3 │
└───────────┴─────────────────────┴───────────────┴───────┘

D WITH ranked_reading AS
    (SELECT *
          , dense_rank() OVER (PARTITION BY system_id
                               ORDER BY power DESC) AS rnk
     FROM readings)
  SELECT *
  FROM ranked_reading
  WHERE rnk <= 2
  ORDER BY system_id
         , rnk ASC ;
┌───────────┬─────────────────────┬───────────────┬───────┐
│ system_id │       read_on       │     power     │  rnk  │
│   int32   │      timestamp      │ decimal(10,3) │ int64 │
├───────────┼─────────────────────┼───────────────┼───────┤
│        10 │ 2019-02-23 12:45:00 │      1109.293 │     1 │
│        10 │ 2019-03-01 12:15:00 │      1087.900 │     2 │
│        34 │ 2019-05-23 11:30:00 │    133900.000 │     1 │
│        34 │ 2019-05-28 11:45:00 │    133900.000 │     1 │
│        34 │ 2019-05-23 10:00:00 │    133900.000 │     1 │
│        34 │ 2019-05-08 12:15:00 │    133900.000 │     1 │
│        34 │ 2020-04-02 11:30:00 │    133900.000 │     1 │
│        34 │ 2019-05-09 10:30:00 │    133700.000 │     2 │
│        34 │ 2019-05-10 12:15:00 │    133700.000 │     2 │
│      1200 │ 2020-04-16 12:15:00 │     47873.333 │     1 │
│      1200 │ 2020-04-02 12:30:00 │     47866.667 │     2 │
│      1200 │ 2020-04-16 13:15:00 │     47866.667 │     2 │
├───────────┴─────────────────────┴───────────────┴───────┤
│ 12 rows                                       4 columns │
└─────────────────────────────────────────────────────────┘

D SELECT system_id
       , DAY
       , min(kwh) OVER seven_days AS "7-days min"
       , quantile(kwh, [0.25, 0.5, 0.75]) OVER seven_days AS "7-days quantile"
       , max(kwh) OVER seven_days AS "7-days max"
  FROM v_power_per_day
  WINDOW seven_days AS (PARTITION BY system_id
                                   , month(DAY)
                        ORDER BY DAY ASC RANGE BETWEEN INTERVAL 3 days PRECEDING AND INTERVAL 3 days FOLLOWING)
  ORDER BY system_id
         , DAY;
┌───────────┬────────────┬────────────┬──────────────────────────┬────────────┐
│ system_id │    DAY     │ 7-days min │     7-days quantile      │ 7-days max │
│   int32   │    date    │   double   │         double[]         │   double   │
├───────────┼────────────┼────────────┼──────────────────────────┼────────────┤
│        10 │ 2019-01-01 │       2.19 │ [2.19, 5.37, 5.55]       │       5.72 │
│        10 │ 2019-01-02 │       2.19 │ [4.62, 5.37, 5.55]       │       5.72 │
│        10 │ 2019-01-03 │       2.19 │ [3.69, 4.62, 5.55]       │       5.72 │
│        10 │ 2019-01-04 │       2.19 │ [3.69, 5.37, 5.72]       │       5.81 │
│        10 │ 2019-01-05 │       3.69 │ [4.62, 5.37, 5.72]       │       5.81 │
│        10 │ 2019-01-06 │       3.52 │ [3.69, 5.32, 5.72]       │       5.81 │
│        10 │ 2019-01-07 │       3.46 │ [3.52, 4.62, 5.37]       │       5.81 │
│        10 │ 2019-01-08 │       0.28 │ [3.46, 3.69, 5.32]       │       5.81 │
│        10 │ 2019-01-09 │       0.28 │ [1.58, 3.52, 5.32]       │       5.81 │
│        10 │ 2019-01-10 │       0.28 │ [1.58, 3.52, 5.81]       │        5.9 │
│        10 │ 2019-01-11 │       0.28 │ [1.58, 3.52, 5.9]        │       6.22 │
│        10 │ 2019-01-12 │       0.28 │ [1.58, 3.52, 5.9]        │       6.22 │
│        10 │ 2019-01-13 │       0.28 │ [1.58, 3.94, 5.9]        │       6.22 │
│        10 │ 2019-01-14 │       0.28 │ [1.58, 5.09, 5.9]        │       6.22 │
│        10 │ 2019-01-15 │       0.13 │ [1.58, 5.09, 5.9]        │       6.22 │
│        10 │ 2019-01-16 │       0.13 │ [3.94, 5.09, 5.9]        │       6.22 │
│        10 │ 2019-01-17 │       0.13 │ [3.94, 4.96, 5.44]       │       6.22 │
│        10 │ 2019-01-18 │       0.13 │ [3.94, 4.96, 5.44]       │       5.46 │
│        10 │ 2019-01-19 │       0.13 │ [1.47, 4.95, 5.44]       │       5.46 │
│        10 │ 2019-01-20 │       0.13 │ [1.47, 4.95, 5.44]       │       5.46 │
│         · │     ·      │         ·  │         ·                │         ·  │
│         · │     ·      │         ·  │         ·                │         ·  │
│         · │     ·      │         ·  │         ·                │         ·  │
│      1200 │ 2020-06-07 │     196.45 │ [225.62, 259.85, 287.1]  │     297.57 │
│      1200 │ 2020-06-08 │     163.37 │ [196.45, 249.4, 287.1]   │     297.57 │
│      1200 │ 2020-06-09 │     163.37 │ [225.62, 267.44, 287.1]  │     297.57 │
│      1200 │ 2020-06-10 │     163.37 │ [225.62, 274.83, 288.13] │     297.57 │
│      1200 │ 2020-06-11 │     163.37 │ [225.62, 274.83, 288.31] │     297.57 │
│      1200 │ 2020-06-12 │     163.37 │ [225.62, 274.83, 288.31] │      294.7 │
│      1200 │ 2020-06-13 │     163.37 │ [225.47, 267.44, 288.31] │      294.7 │
│      1200 │ 2020-06-14 │      88.39 │ [163.37, 267.44, 288.31] │      294.7 │
│      1200 │ 2020-06-15 │      88.39 │ [219.68, 267.44, 288.31] │      294.7 │
│      1200 │ 2020-06-16 │      88.39 │ [149.11, 225.47, 288.31] │      294.7 │
│      1200 │ 2020-06-17 │      88.39 │ [107.68, 219.68, 288.31] │      294.7 │
│      1200 │ 2020-06-18 │      88.39 │ [107.68, 190.91, 225.47] │      294.7 │
│      1200 │ 2020-06-19 │      88.39 │ [107.68, 190.91, 219.68] │     225.47 │
│      1200 │ 2020-06-20 │      88.39 │ [107.68, 190.91, 214.68] │     219.68 │
│      1200 │ 2020-06-21 │     107.68 │ [149.11, 191.61, 219.68] │      279.8 │
│      1200 │ 2020-06-22 │     107.68 │ [149.11, 191.61, 214.68] │      279.8 │
│      1200 │ 2020-06-23 │        0.0 │ [107.68, 191.61, 214.68] │      279.8 │
│      1200 │ 2020-06-24 │        0.0 │ [190.91, 191.61, 214.68] │      279.8 │
│      1200 │ 2020-06-25 │        0.0 │ [191.61, 203.06, 214.68] │      279.8 │
│      1200 │ 2020-06-26 │        0.0 │ [0.0, 203.06, 214.68]    │      279.8 │
├───────────┴────────────┴────────────┴──────────────────────────┴────────────┤
│ 1587 rows (40 shown)                                              5 columns │
└─────────────────────────────────────────────────────────────────────────────┘


D WITH changes AS
    (SELECT value - lag(value, 1, value) OVER (
                                               ORDER BY valid_from) AS v
     FROM prices
     WHERE date_part('year', valid_from) = 2019
     ORDER BY valid_from)
  SELECT sum(changes.v)
  FROM changes;
┌────────────────┐
│ sum(changes.v) │
│ decimal(38,2)  │
├────────────────┤
│     -1.50      │
└────────────────┘

D SELECT dense_rank() OVER (
                            ORDER BY power DESC) AS rnk
       , *
  FROM readings
  QUALIFY rnk <= 3 ;
┌───────┬───────────┬─────────────────────┬───────────────┐
│  rnk  │ system_id │       read_on       │     power     │
│ int64 │   int32   │      timestamp      │ decimal(10,3) │
├───────┼───────────┼─────────────────────┼───────────────┤
│     1 │        34 │ 2019-05-28 11:45:00 │    133900.000 │
│     1 │        34 │ 2020-04-02 11:30:00 │    133900.000 │
│     1 │        34 │ 2019-05-08 12:15:00 │    133900.000 │
│     1 │        34 │ 2019-05-23 11:30:00 │    133900.000 │
│     1 │        34 │ 2019-05-23 10:00:00 │    133900.000 │
│     2 │        34 │ 2019-05-10 12:15:00 │    133700.000 │
│     2 │        34 │ 2019-05-09 10:30:00 │    133700.000 │
│     3 │        34 │ 2019-03-21 13:00:00 │    133600.000 │
│     3 │        34 │ 2019-04-02 10:30:00 │    133600.000 │
└───────┴───────────┴─────────────────────┴───────────────┘

D SELECT system_id
       , DAY
       , kwh
       , avg(kwh) OVER (PARTITION BY system_id
                        ORDER BY DAY ASC RANGE BETWEEN INTERVAL 3 days PRECEDING AND INTERVAL 3 days FOLLOWING) AS "kWh 
7-day moving average"
  FROM v_power_per_day
  QUALIFY "kWh 7-day moving average" > 875
  ORDER BY system_id
         , DAY;
┌───────────┬────────────┬────────┬──────────────────────────┐
│ system_id │    DAY     │  kwh   │ kWh 7-day moving average │
│   int32   │    date    │ double │          double          │
├───────────┼────────────┼────────┼──────────────────────────┤
│        34 │ 2020-05-21 │  873.5 │        887.4628571428572 │
│        34 │ 2020-05-22 │ 814.05 │        884.7342857142858 │
│        34 │ 2020-06-09 │ 880.75 │        882.4628571428572 │
└───────────┴────────────┴────────┴──────────────────────────┘


D pivot ( from v_power_per_day where day between '2020-05-30' and '2020-06-02') on day using first(kWh);
┌───────────┬────────────┬────────────┬────────────┬────────────┐
│ system_id │ 2020-05-30 │ 2020-05-31 │ 2020-06-01 │ 2020-06-02 │
│   int32   │   double   │   double   │   double   │   double   │
├───────────┼────────────┼────────────┼────────────┼────────────┤
│        10 │       4.24 │       3.78 │       4.47 │       5.09 │
│        34 │      732.5 │     790.33 │     796.55 │     629.17 │
│      1200 │      280.4 │     282.25 │     288.29 │     152.83 │
└───────────┴────────────┴────────────┴────────────┴────────────┘
D pivot ( from v_power_per_day where day between '2020-05-30' and '2020-06-02') on day;
┌───────────┬────────┬────────────┬────────────┬────────────┬────────────┐
│ system_id │  kwh   │ 2020-05-30 │ 2020-05-31 │ 2020-06-01 │ 2020-06-02 │
│   int32   │ double │   int64    │   int64    │   int64    │   int64    │
├───────────┼────────┼────────────┼────────────┼────────────┼────────────┤
│        10 │   4.47 │          0 │          0 │          1 │          0 │
│        10 │   4.24 │          1 │          0 │          0 │          0 │
│        10 │   5.09 │          0 │          0 │          0 │          1 │
│        34 │ 796.55 │          0 │          0 │          1 │          0 │
│        10 │   3.78 │          0 │          1 │          0 │          0 │
│      1200 │ 282.25 │          0 │          1 │          0 │          0 │
│        34 │  732.5 │          1 │          0 │          0 │          0 │
│        34 │ 790.33 │          0 │          1 │          0 │          0 │
│      1200 │ 152.83 │          0 │          0 │          0 │          1 │
│      1200 │ 288.29 │          0 │          0 │          1 │          0 │
│        34 │ 629.17 │          0 │          0 │          0 │          1 │
│      1200 │  280.4 │          1 │          0 │          0 │          0 │
├───────────┴────────┴────────────┴────────────┴────────────┴────────────┤
│ 12 rows                                                      6 columns │
└────────────────────────────────────────────────────────────────────────┘

D PIVOT v_power_per_day
  ON year(DAY)
  USING round(sum(kwh)) AS total
      , max(kwh) AS best_day;
┌───────────┬────────────┬───────────────┬────────────┬───────────────┐
│ system_id │ 2019_total │ 2019_best_day │ 2020_total │ 2020_best_day │
│   int32   │   double   │    double     │   double   │    double     │
├───────────┼────────────┼───────────────┼────────────┼───────────────┤
│        10 │     1549.0 │          7.47 │      677.0 │          6.97 │
│        34 │   205743.0 │         915.4 │   101034.0 │        960.03 │
│      1200 │    62012.0 │        337.29 │    30709.0 │        343.43 │
└───────────┴────────────┴───────────────┴────────────┴───────────────┘

D SELECT power.day
       , power.kWh
       , p.value AS 'ct/kWh'
       , round(sum(p.value * power.kWh) OVER (
                                          ORDER BY power.day ASC) / 100, 2) AS 'Accumulated earnings in EUR'
  FROM v_power_per_day power
  asof JOIN prices p ON p.valid_from <= power.day
  WHERE system_id = 34
  ORDER BY DAY ;
┌────────────┬────────┬──────────────┬─────────────────────────────┐
│    DAY     │  kwh   │    ct/kWh    │ Accumulated earnings in EUR │
│    date    │ double │ decimal(5,2) │           double            │
├────────────┼────────┼──────────────┼─────────────────────────────┤
│ 2019-01-01 │  471.4 │        11.47 │                       54.07 │
│ 2019-01-02 │ 458.58 │        11.47 │                      106.67 │
│ 2019-01-03 │ 443.65 │        11.47 │                      157.56 │
│ 2019-01-04 │ 445.03 │        11.47 │                       208.6 │
│     ·      │    ·   │           ·  │                         ·   │
│     ·      │    ·   │           ·  │                         ·   │
│     ·      │    ·   │           ·  │                         ·   │
│ 2020-06-23 │ 798.85 │         9.17 │                    31371.86 │
│ 2020-06-24 │ 741.15 │         9.17 │                    31439.83 │
│ 2020-06-25 │  762.6 │         9.17 │                    31509.76 │
│ 2020-06-26 │  11.98 │         9.17 │                    31510.86 │
├────────────┴────────┴──────────────┴─────────────────────────────┤
│ 543 rows ( 8 shown)                                    4 columns │
└──────────────────────────────────────────────────────────────────┘

D SELECT distinct on(function_name) function_name
  FROM duckdb_functions()
  where function_type = 'table'
  ORDER BY function_name
  ;
┌──────────────────────────────┐
│        function_name         │
│           varchar            │
├──────────────────────────────┤
│ arrow_scan                   │
│ arrow_scan_dumb              │
│ check_peg_parser             │
│ checkpoint                   │
│ disable_logging              │
│ duckdb_approx_database_count │
│ duckdb_columns               │
│ duckdb_constraints           │
│ duckdb_databases             │
│ duckdb_dependencies          │
│ duckdb_extensions            │
│ duckdb_external_file_cache   │
│ duckdb_functions             │
│ duckdb_indexes               │
│ duckdb_keywords              │
│ duckdb_log_contexts          │
│ duckdb_logs                  │
│ duckdb_memory                │
│ duckdb_optimizers            │
│ duckdb_prepared_statements   │
│     ·                        │
│     ·                        │
│     ·                        │
│ read_json                    │
│ read_json_auto               │
│ read_json_objects            │
│ read_json_objects_auto       │
│ read_ndjson                  │
│ read_ndjson_auto             │
│ read_ndjson_objects          │
│ read_parquet                 │
│ read_text                    │
│ repeat                       │
│ repeat_row                   │
│ seq_scan                     │
│ sniff_csv                    │
│ sql_auto_complete            │
│ summary                      │
│ test_all_types               │
│ test_vector_types            │
│ truncate_duckdb_logs         │
│ unnest                       │
│ which_secret                 │
├──────────────────────────────┤
│      81 rows (40 shown)      │
└──────────────────────────────┘
```

```sql
SELECT *
     , avg(kwh) OVER (PARTITION BY system_id) AS average_per_system
FROM v_power_per_day;


pivot v_power_per_day on year(day) using sum(kWh);
pivot (from v_power_per_day) on year(day) using sum(kWh);
pivot (select * from v_power_per_day) on year(day) using sum(kWh);


SELECT distinct on(function_name) function_name
FROM duckdb_functions()
where function_type = 'table'
ORDER BY function_name
;

SELECT *
FROM duckdb_functions()
ORDER BY function_name
limit 1
;


D .mode line
D SELECT *
  FROM duckdb_functions()
  ORDER BY function_name
  limit 1
  ;
   database_name = system
    database_oid = 0
     schema_name = main
   function_name = !__postfix
        alias_of = NULL
   function_type = scalar
     description = Factorial of x. Computes the product of the current integer and all integers below it
         comment = NULL
            tags = {}
     return_type = HUGEINT
      parameters = [x]
 parameter_types = [INTEGER]
         varargs = NULL
macro_definition = NULL
has_side_effects = false
        internal = true
    function_oid = 1357
        examples = [4!]
       stability = CONSISTENT
      categories = []

D SELECT count(1)
  FROM duckdb_functions()
  ;
count(1) = 2708


D select count(*) as cnt, function_type from duckdb_functions() group by function_type;
┌───────┬───────────────┐
│  cnt  │ function_type │
│ int64 │    varchar    │
├───────┼───────────────┤
│   119 │ table         │
│  1433 │ scalar        │
│     3 │ table_macro   │
│   978 │ aggregate     │
│    45 │ pragma        │
│   130 │ macro         │
└───────┴───────────────┘
select count(*) as cnt, function_type from duckdb_functions() group by function_type;

select function_name, function_type, dense_rank() over (partition by function_type order by function_name) as rnk
from duckdb_functions()
QUALIFY rnk <= 3 ;
;


D SELECT distinct function_name
  FROM duckdb_functions()
  where function_type = 'table'
  ORDER BY function_name
  ;
┌──────────────────────────────┐
│        function_name         │
│           varchar            │
├──────────────────────────────┤
│ arrow_scan                   │
│ arrow_scan_dumb              │
│ check_peg_parser             │
│ checkpoint                   │
│ disable_logging              │
│ duckdb_approx_database_count │
│ duckdb_columns               │
│ duckdb_constraints           │
│ duckdb_databases             │
│ duckdb_dependencies          │
│ duckdb_extensions            │
│ duckdb_external_file_cache   │
│ duckdb_functions             │
│ duckdb_indexes               │
│ duckdb_keywords              │
│ duckdb_log_contexts          │
│ duckdb_logs                  │
│ duckdb_memory                │
│ duckdb_optimizers            │
│ duckdb_prepared_statements   │
│ duckdb_schemas               │
│ duckdb_secret_types          │
│ duckdb_secrets               │
│ duckdb_sequences             │
│ duckdb_settings              │
│ duckdb_table_sample          │
│ duckdb_tables                │
│ duckdb_temporary_files       │
│ duckdb_types                 │
│ duckdb_variables             │
│ duckdb_views                 │
│ enable_logging               │
│ force_checkpoint             │
│ generate_series              │
│ glob                         │
│ icu_calendar_names           │
│ json_each                    │
│ json_execute_serialized_sql  │
│ json_tree                    │
│ parquet_bloom_probe          │
│ parquet_file_metadata        │
│ parquet_kv_metadata          │
│ parquet_metadata             │
│ parquet_scan                 │
│ parquet_schema               │
│ pg_timezone_names            │
│ pragma_collations            │
│ pragma_database_size         │
│ pragma_metadata_info         │
│ pragma_platform              │
│ pragma_show                  │
│ pragma_storage_info          │
│ pragma_table_info            │
│ pragma_user_agent            │
│ pragma_version               │
│ query                        │
│ query_table                  │
│ range                        │
│ read_blob                    │
│ read_csv                     │
│ read_csv_auto                │
│ read_json                    │
│ read_json_auto               │
│ read_json_objects            │
│ read_json_objects_auto       │
│ read_ndjson                  │
│ read_ndjson_auto             │
│ read_ndjson_objects          │
│ read_parquet                 │
│ read_text                    │
│ repeat                       │
│ repeat_row                   │
│ seq_scan                     │
│ sniff_csv                    │
│ sql_auto_complete            │
│ summary                      │
│ test_all_types               │
│ test_vector_types            │
│ truncate_duckdb_logs         │
│ unnest                       │
│ which_secret                 │
├──────────────────────────────┤
│           81 rows            │
└──────────────────────────────┘
```

---

uv add ipython
uv run ipython

uv add ipdb

import ipdb
bk = ipdb.set_trace()
ipdb > where
ipdb > help

```py
In [12]: con.sql('SELECT count(*) FROM over_10m WHERE "GDP ($ per capita)" > 10000')
Out[12]: 
┌──────────────┐
│ count_star() │
│    int64     │
├──────────────┤
│           20 │
└──────────────┘
```

```py
In [15]: %lsmagic
Out[15]: 
Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %autoindent  %automagic  %bookmark  %cat  %cd  %clear  %code_wrap  %colors 
 %conda  %config  %cp  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgsc
ripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %ls
magic  %lx  %macro  %magic  %mamba  %man  %matplotlib  %micromamba  %mkdir  %more  %mv  %notebook  %page  %paste  %paste
bin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %
pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %ru
n  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %uv  %who  %who_ls  %whos  %x
del  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%code_wrap  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%
perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %
%writefile

Automagic is ON, % prefix IS NOT needed for line magics.
```



```py
In [16]: def remove_spaces(field:str) -> str:
    ...:     if field:
    ...:         return field.lstrip().rstrip()
    ...:     else:
    ...:         return field
    ...: 

In [17]: con.sql("""
    ...: SELECT function_name, function_type, parameters, parameter_types, return_type
    ...: from duckdb_functions()
    ...: where function_name = 'remove_spaces'
    ...: """)
Out[17]: 
┌───────────────┬───────────────┬────────────┬─────────────────┬─────────────┐
│ function_name │ function_type │ parameters │ parameter_types │ return_type │
│    varchar    │    varchar    │ varchar[]  │    varchar[]    │   varchar   │
├───────────────┴───────────────┴────────────┴─────────────────┴─────────────┤
│                                   0 rows                                   │
└────────────────────────────────────────────────────────────────────────────┘

In [18]: con.create_function('remove_spaces', remove_spaces)
Out[18]: <_duckdb.DuckDBPyConnection at 0x7739d0add4b0>

In [19]: con.sql("""
    ...: SELECT function_name, function_type, parameters, parameter_types, return_type
    ...: from duckdb_functions()
    ...: where function_name = 'remove_spaces'
    ...: """)
Out[19]: 
┌───────────────┬───────────────┬────────────┬─────────────────┬─────────────┐
│ function_name │ function_type │ parameters │ parameter_types │ return_type │
│    varchar    │    varchar    │ varchar[]  │    varchar[]    │   varchar   │
├───────────────┼───────────────┼────────────┼─────────────────┼─────────────┤
│ remove_spaces │ scalar        │ [col0]     │ [VARCHAR]       │ VARCHAR     │
└───────────────┴───────────────┴────────────┴─────────────────┴─────────────┘

In [20]: con.sql("select length(remove_spaces(' foo '))")
Out[20]: 
┌────────────────────────────────┐
│ length(remove_spaces(' foo ')) │
│             int64              │
├────────────────────────────────┤
│                              3 │
└────────────────────────────────┘

In [21]: con.remove_function('remove_spaces')
Out[21]: <_duckdb.DuckDBPyConnection at 0x7739d0add4b0>

In [22]: from duckdb.typing import *

In [23]: con.create_function(
    ...: 'remove_spaces',
    ...: remove_spaces,
    ...: [(VARCHAR)],
    ...: VARCHAR
    ...: )
Out[23]: <_duckdb.DuckDBPyConnection at 0x7739d0add4b0>

In [24]: con.sql("""
    ...: SELECT DISTINCT Region, length(Region) AS len1,
    ...:        remove_spaces(Region) AS cleanRegion,
    ...:        length(cleanRegion) AS len2
    ...: FROM population
    ...: WHERE len1 BETWEEN 20 AND 30
    ...: LIMIT 3
    ...: """)
100% ▕██████████████████████████████████████▏ (00:00:02.34 elapsed)     

┌───────────────────────────────┬───────┬──────────────────────┬───────┐
│            Region             │ len1  │     cleanRegion      │ len2  │
│            varchar            │ int64 │       varchar        │ int64 │
├───────────────────────────────┼───────┼──────────────────────┼───────┤
│ C.W. OF IND. STATES           │    20 │ C.W. OF IND. STATES  │    19 │
│ LATIN AMER. & CARIB           │    23 │ LATIN AMER. & CARIB  │    19 │
│ ASIA (EX. NEAR EAST)          │    29 │ ASIA (EX. NEAR EAST) │    20 │
└───────────────────────────────┴───────┴──────────────────────┴───────┘
```

```py
import duckdb
import pandas as pd
people = pd.DataFrame({
"name": ["Michael Hunger", "Michael Simons", "mark Needham"],
"country": ["Germany", "Germany", "Great Britain"]
})
duckdb.sql("""
SELECT *
FROM people
WHERE country = 'Germany'
""")
params = {"country": "Germany"}
duckdb.execute("""
SELECT *
FROM people
WHERE country <> $country
""", params).fetchdf()
duckdb.sql("FROM people")
duckdb.sql("FROM people").filter("country <> 'Germany'")
con
%history
    con = duckdb.connect(database=':memory:')

    con.execute("INSTALL httpfs")
    con.execute("LOAD httpfs")

    population = con.read_csv("https://bit.ly/3KoiZR0")
con.sql('select count(1) from population')
    population_table = con.table("population")
con.sql('select dinstinct Region, length(Region) AS numChars from population')
con.sql('select DISTINCT Region, length(Region) AS numChars from population')
def remove_spaces(field:str) -> str:
    if field:
        return field.lstrip().rstrip()
    else:
        return field
con.sql("""
SELECT function_name, function_type, parameters, parameter_types, return_type
from duckdb_functions()
where function_name = 'remove_spaces'
""")
con.create_function('remove_spaces', remove_spaces)
con.sql("""
SELECT function_name, function_type, parameters, parameter_types, return_type
from duckdb_functions()
where function_name = 'remove_spaces'
""")
con.sql("select length(remove_spaces(' foo '))")
con.remove_function('remove_spaces')
from duckdb.typing import *
con.create_function(
'remove_spaces',
remove_spaces,
[(VARCHAR)],
VARCHAR
)
con.sql("""
SELECT DISTINCT Region, length(Region) AS len1,
       remove_spaces(Region) AS cleanRegion,
       length(cleanRegion) AS len2
FROM population
WHERE len1 BETWEEN 20 AND 30
LIMIT 3
""")
con.sql("""
select DISTINCT Region, length(Region) AS numChars
from population
""")
con.sql("""
UPDATE population
SET Region = remove_spaces(Region);
""")
    population_table = con.table("population")
con.sql("""
UPDATE population_table
SET Region = remove_spaces(Region);
""")
population.to_table("population")
con.sql("""
UPDATE population_table
SET Region = remove_spaces(Region);
""")
con.sql("""
UPDATE population
SET Region = remove_spaces(Region);
""")
import locale
def convert_locale(field:str) -> float:
    locale.setlocale(locale.LC_ALL, 'de_DE')
    return locale.atof(field)
con.create_function('convert_locale', convert_locale)
con.sql("""
select "Coastline (coast/area ratio)" AS coastline,
convert_locale(coastline) as cleanCoastline,
"Pop. Densisy (per sq. mi.)" as popDen,
convert_locale(popDen) as cleanPopDen
from population
limit 5
""")
con.sql("""
select "Coastline (coast/area ratio)" AS coastline,
convert_locale(coastline) as cleanCoastline,
"Pop. Densisty (per sq. mi.)" as popDen,
convert_locale(popDen) as cleanPopDen
from population
limit 5
""")
con.sql("""
select "Coastline (coast/area ratio)" AS coastline,
convert_locale(coastline) as cleanCoastline,
"Pop. Density (per sq. mi.)" as popDen,
convert_locale(popDen) as cleanPopDen
from population
limit 5
""")
%history
```

      - name: surface
        description: "The surface of the court."
        tests:
          - not_null
          - accepted_values:
            values: ['Grass', 'Hard', 'Clay']


Parsing Error
  Invalid test config given in models/atp/schema.yml:
        test definition dictionary must have exactly one key, got [('accepted_values', None), ('values', ['Grass', 'Har
d', 'Clay'])] instead (2 keys)
        @: UnparsedModelUpdate(original_file_path='mode...ne)
