{{ config(
    materialized='external',
    location='output/matches.parquet',
    format='parquet'
) }}

WITH no_win_loss AS
  (SELECT columns(col -> NOT regexp_matches(col, 'w_.*')
                  AND NOT regexp_matches(col, 'l_.*'))
   FROM {{ source('github', 'matches_file') }}
)
SELECT * REPLACE (
    cast(strptime(tourney_date::varchar, '%Y%m%d') AS date) AS tourney_date
)
FROM no_win_loss
WHERE surface IS NOT NULL
