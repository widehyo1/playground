CREATE TABLE health (
    id SERIAL PRIMARY KEY,
    first VARCHAR(50),
    second VARCHAR(50)
);

INSERT INTO health(first, second) VALUES('health', 'check');
