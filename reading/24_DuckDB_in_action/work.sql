INSERT INTO prices
VALUES (1, 11.59, '2018-12-01', '2019-01-01')
ON CONFLICT DO NOTHING;


INSERT INTO systems(id, name)
SELECT DISTINCT system_id, system_public_name
from 'https://oedi-data-lake.s3.amazonaws.com/pvdaq/csv/systems.csv'
ORDER BY system_id ASC
;

SELECT count(1) FROM systems;

-- INSERT INTO readings (system_id, read_on, power)
-- SELECT SiteId
--      , "Date-Time"
--      , CASE
--            WHEN ac_power < 0
--                 OR ac_power IS NULL THEN 0
--            ELSE ac_power
--        END
-- FROM read_csv_auto('https://developer.nrel.gov/api/pvdaq/v3/data_file?api_key=NQn5bLieXHkU67ecYpywPIqsAOVSbSTHfcC9aQhM&system_id=34&year=2019') ;


COPY systems FROM 'systems.parquet' (FORMAT 'parquet', COMPRESSION 'ZSTD');
COPY prices FROM 'prices.parquet' (FORMAT 'parquet', COMPRESSION 'ZSTD');
COPY readings FROM 'readings.parquet' (FORMAT 'parquet', COMPRESSION 'ZSTD');

SELECT * FROM v_power_per_day;

SELECT date_part('year', valid_from) AS YEAR
     , min(value) AS minimum_price
     , max(value) AS maximum_price
FROM prices
WHERE YEAR BETWEEN 2019 AND 2020
GROUP BY YEAR
ORDER BY YEAR;

WITH max_power AS
  (SELECT max(power) AS v
   FROM readings)
SELECT max_power.v
     , read_on
FROM max_power
JOIN readings ON power = max_power.v;

SELECT max(power)
     , arg_max(read_on, power) AS read_on
FROM readings;

WITH per_hour AS
  (SELECT system_id
        , date_trunc('hour', read_on) AS read_on
        , avg(power) / 1000 AS kwh
   FROM readings
   GROUP BY ALL)
SELECT name
     , max(kwh)
     , arg_max(read_on, kwh) AS 'Read on'
FROM per_hour
JOIN systems s ON s.id = per_hour.system_id
WHERE system_id = 34
GROUP BY s.name ;

SELECT read_on
     , power
FROM readings
WHERE power =
    (SELECT max(power)
     FROM readings);


SELECT system_id
     , read_on
     , power
FROM readings r1
WHERE power =
    (SELECT max(power)
     FROM readings r2
     WHERE r2.system_id = r1.system_id)
ORDER BY ALL ;

SELECT count(1)
     , min(power) AS min_w
     , max(power) AS max_w
     , round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings;

SELECT year(read_on) AS YEAR
     , system_id
     , count(*)
     , round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings
GROUP BY YEAR
       , system_id
ORDER BY YEAR
       , system_id;

SELECT year(read_on) AS YEAR
     , system_id
     , count(*)
     , round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings
GROUP BY GROUPING
SETS ((YEAR
     , system_id), YEAR, ())
ORDER BY YEAR NULLS FIRST, system_id NULLS FIRST;

SELECT year(read_on) AS YEAR
     , system_id
     , count(*)
     , round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings
GROUP BY ROLLUP (YEAR , system_id)
ORDER BY YEAR NULLS FIRST, system_id NULLS FIRST;

SELECT year(read_on) AS YEAR
     , system_id
     , count(*)
     , round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings
GROUP BY CUBE (YEAR , system_id)
ORDER BY YEAR NULLS FIRST, system_id NULLS FIRST;

WITH ranked_reading AS
  (SELECT *
        , dense_rank() OVER (
                             ORDER BY power DESC) AS rnk
   FROM readings)
SELECT *
FROM ranked_reading
WHERE rnk <= 3
;

WITH ranked_reading AS
  (SELECT *
        , dense_rank() OVER (PARTITION BY system_id
                             ORDER BY power DESC) AS rnk
   FROM readings)
SELECT *
FROM ranked_reading
WHERE rnk <= 2
ORDER BY system_id
       , rnk ASC ;

SELECT *
     , avg(kwh) OVER (PARTITION BY system_id) AS average_per_system
FROM v_power_per_day;

SELECT system_id
     , DAY
     , kwh
     , avg(kwh) OVER (PARTITION BY system_id
                      ORDER BY DAY ASC RANGE BETWEEN INTERVAL 3 days PRECEDING AND INTERVAL 3 days FOLLOWING) AS "kWh 7-day moving average"
FROM v_power_per_day
ORDER BY system_id
       , DAY;

SELECT system_id
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

SELECT valid_from
     , value
     , lag(value) OVER validity AS "previous value"
     , value - lag(value, 1, value) OVER validity AS CHANGE
FROM prices
WHERE date_part('year', valid_from) = 2019
WINDOW validity AS (ORDER BY valid_from)
ORDER BY valid_from;


WITH changes AS
  (SELECT value - lag(value, 1, value) OVER (
                                             ORDER BY valid_from) AS v
   FROM prices
   WHERE date_part('year', valid_from) = 2019
   ORDER BY valid_from)
SELECT sum(changes.v)
FROM changes;

SELECT dense_rank() OVER (
                          ORDER BY power DESC) AS rnk
     , *
FROM readings
QUALIFY rnk <= 3 ;


SELECT system_id
     , DAY
     , kwh
     , avg(kwh) OVER (PARTITION BY system_id
                      ORDER BY DAY ASC RANGE BETWEEN INTERVAL 3 days PRECEDING AND INTERVAL 3 days FOLLOWING) AS "kWh 7-day moving average"
FROM v_power_per_day
QUALIFY "kWh 7-day moving average" > 875
ORDER BY system_id
       , DAY;


SELECT system_id, year(day), sum(kWh) FROM v_power_per_day
GROUP BY ALL
ORDER BY system_id
;

SELECT system_id,
sum(kWh) filter (where year(day) = 2019) as 'kwh in 2019',
sum(kWh) filter (where year(day) = 2020) as 'kwh in 2020'
FROM v_power_per_day
GROUP BY system_id
;

pivot v_power_per_day on year(day) using sum(kWh);
pivot (from v_power_per_day) on year(day) using sum(kWh);
pivot (select * from v_power_per_day) on year(day) using sum(kWh);


PIVOT v_power_per_day
ON year(DAY)
USING round(sum(kwh)) AS total
    , max(kwh) AS best_day;


SELECT power.day
     , power.kWh
     , p.value AS 'ct/kWh'
     , round(sum(p.value * power.kWh) OVER (
                                        ORDER BY power.day ASC) / 100, 2) AS 'Accumulated earnings in EUR'
FROM v_power_per_day power
asof JOIN prices p ON p.valid_from <= power.day
WHERE system_id = 34
ORDER BY DAY ;

SELECT distinct on(function_name) function_name
FROM duckdb_functions()
where function_type = 'table'
ORDER BY function_name
;
