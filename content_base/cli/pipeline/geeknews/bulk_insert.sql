-- \COPY geeknews_xargs (url, title, content) FROM 'bulk_data_xargs_v2.csv' WITH (FORMAT csv);
\COPY geeknews_xargs (url, title, content) FROM 'bulk_data_lynx.csv' WITH (FORMAT csv);
