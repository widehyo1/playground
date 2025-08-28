create table if not exists geeknews( url varchar(200) primary key, title varchar(500), content text );
create table if not exists geeknews_parallel( url varchar(200) primary key, title varchar(500), content text );
create table if not exists geeknews_xargs( url varchar(200) primary key, title varchar(500), content text );
