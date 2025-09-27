CREATE TABLE IF NOT EXISTS systems (
    id INTEGER PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS readings (
    system_id INTEGER NOT NULL,
    read_on TIMESTAMP NOT NULL,
    power DECIMAL(10,3) NOT NULL DEFAULT 0 CHECK(power >= 0),
    PRIMARY KEY (system_id, read_on),
    FOREIGN KEY (system_id) REFERENCES systems(id)
);

CREATE SEQUENCE IF NOT EXISTS prices_id INCREMENT BY 1 MINVALUE 10;

CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY DEFAULT nextval('prices_id'),
    value DECIMAL(5,2) NOT NULL,
    valid_from DATE NOT NULL,
    CONSTRAINT prices_uk UNIQUE (valid_from)
);

ALTER TABLE prices
ADD COLUMN IF NOT EXISTS valid_until DATE;

CREATE OR REPLACE VIEW v_power_per_day AS
SELECT system_id
     ,  date_trunc('day', read_on) AS DAY
     ,  round(sum(power) / 4 / 1000, 2) AS kwh
FROM readings
GROUP BY system_id
       , DAY
;
