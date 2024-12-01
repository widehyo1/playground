
root@fa12fb01593a:/var/lib/postgresql/data# psql -U postgres
psql (16.6 (Debian 16.6-1.pgdg120+1))
Type "help" for help.

postgres=# \dn
      List of schemas
  Name  |       Owner
--------+-------------------
 public | pg_database_owner
(1 row)

postgres=# \dn
      List of schemas
  Name  |       Owner
--------+-------------------
 public | pg_database_owner
(1 row)

postgres=# \dt
Did not find any relations.
postgres=# \?
postgres=# \du
                             List of roles
 Role name |                         Attributes
-----------+------------------------------------------------------------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS

postgres=# \du+
                                    List of roles
 Role name |                         Attributes                         | Description
-----------+------------------------------------------------------------+-------------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS |

postgres=# \drg
            List of role grants
 Role name | Member of | Options | Grantor
-----------+-----------+---------+---------
(0 rows)

postgres=# \?
postgres=# create user test password 'test';
CREATE ROLE
postgres=# \du+
                                    List of roles
 Role name |                         Attributes                         | Description
-----------+------------------------------------------------------------+-------------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS |
 test      |                                                            |

postgres=# \?
postgres=# \l
postgres=# create database test_db;
CREATE DATABASE
postgres=# \l
postgres=# drop database test_db;
DROP DATABASE
postgres=# =l
postgres-# ;
ERROR:  syntax error at or near "="
LINE 1: =l
        ^
postgres=# \l
postgres=# create database test_db owner test;
CREATE DATABASE
postgres=# \l
postgres=# create schema playground authorization test;
CREATE SCHEMA
postgres=# \dn
        List of schemas
    Name    |       Owner
------------+-------------------
 playground | test
 public     | pg_database_owner
(2 rows)

postgres=# create role playground;
CREATE ROLE
postgres=# \dre
invalid command \dre
Try \? for help.
postgres=# \drg
            List of role grants
 Role name | Member of | Options | Grantor
-----------+-----------+---------+---------
(0 rows)

postgres=# grant usage on schema playground to playground;
GRANT
postgres=# \drg
            List of role grants
 Role name | Member of | Options | Grantor
-----------+-----------+---------+---------
(0 rows)

postgres=# grant all previleges on database test_db to test;
ERROR:  syntax error at or near "previleges"
LINE 1: grant all previleges on database test_db to test;
                  ^
postgres=# grant all privileges on database test_db to test;
GRANT
postgres=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

postgres=# \drg
            List of role grants
 Role name | Member of | Options | Grantor
-----------+-----------+---------+---------
(0 rows)

postgres=# \c test_db;
You are now connected to database "test_db" as user "postgres".
test_db=# grant all on schema playground to test;
ERROR:  schema "playground" does not exist
test_db=# \dn
      List of schemas
  Name  |       Owner
--------+-------------------
 public | pg_database_owner
(1 row)

test_db=# create schema playground

~ via 🌙 v5.4.7 took 5s ❯ psql -p 5433 -U postgres -h localhost
Password for user postgres:
psql (16.6 (Ubuntu 16.6-1.pgdg22.04+1))
Type "help" for help.

postgres=# \dn
      List of schemas
  Name  |       Owner
--------+-------------------
 public | pg_database_owner
(1 row)

postgres=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

postgres=#

---


root@fa12fb01593a:/var/lib/postgresql/data# psql -h localhost -p 5432 -U test -n test_db
psql (16.6 (Debian 16.6-1.pgdg120+1))
Type "help" for help.

test_db=> drop table knowinfo_content;
DROP TABLE
test_db=> CREATE TABLE playground.knowinfo_content (
    page_num INTtest_db(> EGER,
    page_content TEXT,
   test_db(> test_db(>  knowinfo_id INTEGER,
    createtest_db(> _dt DATE,
    motest_db(> dified_dt DATE
)test_db(> ;
CREATE TABLE
test_db=> \dS+ knowinfo_content
                                        Table "public.knowinfo_content"
    Column    |  Type   | Collation | Nullable | Default | Storage  | Compression | Stats target | Description
--------------+---------+-----------+----------+---------+----------+-------------+--------------+-------------
 page_num     | integer |           |          |         | plain    |             |              |
 page_content | text    |           |          |         | extended |             |              |
 knowinfo_id  | integer |           |          |         | plain    |             |              |
 create_dt    | date    |           |          |         | plain    |             |              |
 modified_dt  | date    |           |          |         | plain    |             |              |
Access method: heap


            SELECT
                tkki.knlg_info_id
                , tkki.korn_nm
                , tkki.expln
                , tkki.smy_cn
                , tkki.pstg_yn
                , tkki.rls_cd
                , tkki.kwrd_ivlst
                , tkki.del_yn
                , tkki.aprv_yn
                , tkki.inq_cnt
                , tkki.dwnld_cnt 
                , tkki.frst_reg_dt
                , COALESCE(tkki.last_chg_dt, tkki.frst_reg_dt) AS last_chg_dt
                , tkki.knlg_sclsf_cd
                , tkki.doc_clsf_cd
                , tkki.knlg_lclsf_cd
                , tkki.enfc_cn 
                , tkkidm.dept_id AS dept_id
                , tkkipim.pvsn_inst_id AS pvsn_inst_id
            FROM
                koai.tm_ka_knlg_info tkki
            LEFT JOIN
                koai.tt_ka_knlg_info_dept_mapng tkkidm ON tkkidm.knlg_info_id = tkki.knlg_info_id
            LEFT JOIN
                koai.tt_ka_knlg_info_pvsn_inst_mapng tkkipim ON tkkipim.knlg_info_id = tkki.knlg_info_id
            WHERE
                COALESCE(tkki.last_chg_dt, tkki.frst_reg_dt) > :sql_last_value
            ORDER BY 
                last_chg_dt ASC
            ;

            SELECT
                  knowinfo_id
                , kor_name
                , eng_name
                , expln
                , smummary
                , resource_code
                , download_count
                , department_id
                , lcategory_name
                , mcategory_name
                , scategory_name
                , del_yn
                , create_dt
                , modified_dt
            FROM
                knowinfo_content
            ;

CREATE TABLE test2 ( kor_name VARCHAR(100) );

CREATE TABLE playground.knowinfo (
    knowinfo_id INTEGER,
    kor_name VARCHAR(100),
    eng_name VARCHAR(100),
    expln TEXT,
    smummary VARCHAR(1000),
    resource_code VARCHAR(100),
    download_count INTEGER,
    department_id INTEGER,
    lcategory_name VARCHAR(100),
    mcategory_name VARCHAR(100),
    scategory_name VARCHAR(100),
    del_yn CHAR(1),
    create_dt DATE,
    modified_dt DATE
);


test_db=> \dt
             List of relations
 Schema |       Name       | Type  | Owner
--------+------------------+-------+-------
 public | knowinfo         | table | test
 public | knowinfo_content | table | test
(2 rows)

test_db=> \dS knowinfo
                          Table "public.knowinfo"
     Column     |          Type           | Collation | Nullable | Default
----------------+-------------------------+-----------+----------+---------
 knowinfo_id    | integer                 |           |          |
 kor_name       | character varying(100)  |           |          |
 eng_name       | character varying(100)  |           |          |
 expln          | text                    |           |          |
 smummary       | character varying(1000) |           |          |
 resource_code  | character varying(100)  |           |          |
 download_count | integer                 |           |          |
 department_id  | integer                 |           |          |
 lcategory_name | character varying(100)  |           |          |
 mcategory_name | character varying(100)  |           |          |
 scategory_name | character varying(100)  |           |          |
 del_yn         | character(1)            |           |          |
 create_dt      | date                    |           |          |
 modified_dt    | date                    |           |          |

test_db=> \dS knowinfo_content
             Table "public.knowinfo_content"
    Column    |  Type   | Collation | Nullable | Default
--------------+---------+-----------+----------+---------
 page_num     | integer |           |          |
 page_content | text    |           |          |
 knowinfo_id  | integer |           |          |
 create_dt    | date    |           |          |
 modified_dt  | date    |           |          |



test_db=> create table test ( a VARCHAR );
CREATE TABLE
test_db=> \dS test
                     Table "public.test"
 Column |       Type        | Collation | Nullable | Default
--------+-------------------+-----------+----------+---------
 a      | character varying |           |          |

test_db=> CREATE TABLE test2 ( kor_name VARCHAR(100) );
CREATE TABLE
test_db=> \dS+ test2;
test_db=> \dS test2;
                        Table "public.test2"
  Column  |          Type          | Collation | Nullable | Default
----------+------------------------+-----------+----------+---------
 kor_name | character varying(100) |           |          |


test_db=# select * from pg_user;
 usename  | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+---------+--------------+----------+----------+-----------
 postgres |       10 | t           | t        | t       | t            | ******** |          |
 test     |    16388 | f           | f        | f       | f            | ******** |          |
(2 rows)

select * from pg_roles where oid='16388';

 rolname | rolsuper | rolinherit | rolcreaterole | rolcreatedb | rolcanlogin | rolreplication | rolconnlimit | rolpassword | rolvaliduntil | rolbypassrls | rolconfig |  oid
---------+----------+------------+---------------+-------------+-------------+----------------+--------------+-------------+---------------+--------------+-----------+-------
 test    | f        | t          | f             | f           | t           | f              |           -1 | ********    |               | f            |           | 16388


test_db=> CREATE TABLE playground.test_table (
    id SERItest_db(> AL PRIMARY KEY,
test_db(>     name TEXT
);
test_db(> CREATE TABLE
test_db=> \dt
             List of relations
 Schema |       Name       | Type  | Owner
--------+------------------+-------+-------
 public | knowinfo         | table | test
 public | knowinfo_content | table | test
(2 rows)

test_db=> \dt playgorund.*
Did not find any relation named "playgorund.*".
test_db=> \dt playground.*
            List of relations
   Schema   |    Name    | Type  | Owner
------------+------------+-------+-------
 playground | test_table | table | test
(1 row)


CREATE TABLE playground.knowinfo_content (
    page_num INTEGER,
    page_content TEXT,
    knowinfo_id INTEGER,
    create_dt DATE,
    modified_dt DATE
);


~ via 🌙 v5.4.7 ❯ !psql
psql -p 5433 -U postgres -h localhost
Password for user postgres:
psql (16.6 (Ubuntu 16.6-1.pgdg22.04+1))
Type "help" for help.

postgres=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

postgres=# \c test_db
You are now connected to database "test_db" as user "postgres".
test_db=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

test_db=# grant all on all tables in schema playground to playground;
GRANT
test_db=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

test_db=# drop role test;
ERROR:  role "test" cannot be dropped because some objects depend on it
DETAIL:  owner of database test_db
owner of schema playground
owner of table knowinfo_content
owner of table knowinfo
1 object in database postgres
test_db=# drop role playground;
ERROR:  role "playground" cannot be dropped because some objects depend on it
DETAIL:  1 object in database postgres
test_db=# \dt
             List of relations
 Schema |       Name       | Type  | Owner
--------+------------------+-------+-------
 public | knowinfo         | table | test
 public | knowinfo_content | table | test
(2 rows)

test_db=# select * from pg_user;
 usename  | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+---------+--------------+----------+----------+-----------
 postgres |       10 | t           | t        | t       | t            | ******** |          |
 test     |    16388 | f           | f        | f       | f            | ******** |          |
(2 rows)

test_db=# select * from database_privs('test')
test_db-# ;
ERROR:  function database_privs(unknown) does not exist
LINE 1: select * from database_privs('test')
                      ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
test_db=# select * from database_privs('test');
ERROR:  function database_privs(unknown) does not exist
LINE 1: select * from database_privs('test');
                      ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
test_db=# \du
                              List of roles
 Role name  |                         Attributes
------------+------------------------------------------------------------
 playground | Cannot login
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS
 test       |

test_db=# \du+
                                     List of roles
 Role name  |                         Attributes                         | Description
------------+------------------------------------------------------------+-------------
 playground | Cannot login                                               |
 postgres   | Superuser, Create role, Create DB, Replication, Bypass RLS |
 test       |                                                            |

test_db=# select * from database_privs;
ERROR:  relation "database_privs" does not exist
LINE 1: select * from database_privs;
                      ^
test_db=# select * from database_privs('test');
ERROR:  function database_privs(unknown) does not exist
LINE 1: select * from database_privs('test');
                      ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
test_db=# select * from database_privs(test);
ERROR:  column "test" does not exist
LINE 1: select * from database_privs(test);
                                     ^
test_db=# select * from database_privs('test');
ERROR:  function database_privs(unknown) does not exist
LINE 1: select * from database_privs('test');
                      ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
test_db=# select * from pg_roles;
test_db=# select * from pg_roles where oid='16388';
test_db=# grant usage on schema playground to test;
GRANT
test_db=# grant select on all tables in schema playtround to test;
ERROR:  schema "playtround" does not exist
test_db=# grant select on all tables in schema playround to test;
ERROR:  schema "playround" does not exist
test_db=# \dn
        List of schemas
    Name    |       Owner
------------+-------------------
 playground | test
 public     | pg_database_owner
(2 rows)

test_db=# grant select on all tables in schema playground to test;
GRANT
test_db=# ALTER DEFAULT PRIVILEGES IN SCHEMA playground GRANT SELECT ON TABLES TO test;
ALTER DEFAULT PRIVILEGES
test_db=# \dt playground.*
Did not find any relation named "playground.*".
test_db=# CREATE TABLE playground.knowinfo_content (
    page_num INTEGER,
    page_content TEXT,
    knowinfo_id INTEGER,
    create_dt DATE,
    modified_dt DATE
);
CREATE TABLE
test_db=# CREATE TABLE playground.knowinfo (
    knowinfo_id INTEGER,
    kor_name VARCHAR(100),
    eng_name VARCHAR(100),
    expln TEXT,
    smummary VARCHAR(1000),
    resource_code VARCHAR(100),
    download_count INTEGER,
    department_id INTEGER,
    lcategory_name VARCHAR(100),
    mcategory_name VARCHAR(100),
    scategory_name VARCHAR(100),
    del_yn CHAR(1),
    create_dt DATE,
    modified_dt DATE
);
CREATE TABLE



test_db=# \dt
             List of relations
 Schema |       Name       | Type  | Owner
--------+------------------+-------+-------
 public | knowinfo         | table | test
 public | knowinfo_content | table | test
(2 rows)

test_db=# \dS knowinfo
                          Table "public.knowinfo"
     Column     |          Type           | Collation | Nullable | Default
----------------+-------------------------+-----------+----------+---------
 knowinfo_id    | integer                 |           |          |
 kor_name       | character varying(100)  |           |          |
 eng_name       | character varying(100)  |           |          |
 expln          | text                    |           |          |
 smummary       | character varying(1000) |           |          |
 resource_code  | character varying(100)  |           |          |
 download_count | integer                 |           |          |
 department_id  | integer                 |           |          |
 lcategory_name | character varying(100)  |           |          |
 mcategory_name | character varying(100)  |           |          |
 scategory_name | character varying(100)  |           |          |
 del_yn         | character(1)            |           |          |
 create_dt      | date                    |           |          |
 modified_dt    | date                    |           |          |

test_db=# \dS knowinfo_content
             Table "public.knowinfo_content"
    Column    |  Type   | Collation | Nullable | Default
--------------+---------+-----------+----------+---------
 page_num     | integer |           |          |
 page_content | text    |           |          |
 knowinfo_id  | integer |           |          |
 create_dt    | date    |           |          |
 modified_dt  | date    |           |          |


lcategory:
국토/도시
주택
토지
건설
교통/물류

mcategory:
-- 국토/도시 --
건축물통계
건축허가·착공·준공통계
국토지리정보현황
도시정비사업현황
[산하기관]건물에너지사용량(세부 용도별_총괄)
[산하기관]건물에너지사용량(용도별_총괄)
[산하기관]도시계획현황
[산하기관]측량업체임금실태조사

-- 주택 --
미분양주택현황보고
아파트주거환경통계
임대주택통계
주거실태조사
주택건설실적통계(분양)
주택건설실적통계(인허가)
주택건설실적통계(준공)
주택건설실적통계(착공)
주택도시기금 및 주택분양보증현황

-- 토지 --
공간정보산업조사
부동산서비스산업 실태조사
외국인토지현황
지적통계
택지예정지구지정 및 공급현황
토지소유현황

-- 건설 --
건설공사계약통계
기계설비산업실태조사
[산하기관]건설사업관리기술인임금실태조사
[산하기관]건설업경영분석
[산하기관]건설업임금실태조사
[산하기관]국내건설수주동향조사

-- 교통물류 --
교통문화실태조사
교통부문수송실적보고
국가교통조사
대중교통현황조사(2007~2010)
대중교통현황조사(2011~ )
자동차등록현황보고
[산하기관]자동차검사현황

scategory:



knowinfo_id,kor_name,eng_name,expln,smummary,resource_code,download_count,department_id,lcategory_name,mcategory_name,scategory_name,del_yn,create_dt,modified_dt
1,국토지리정보현황,National Geographic Information,Details about national geographic information,Summary about geographic data,1,150,1,국토/도시,국토지리정보현황,,N,2023-01-01,2023-11-30
2,미분양주택현황보고,Unsold Housing Report,Details about unsold housing,Summary about unsold housing,2,90,2,주택,미분양주택현황보고,,N,2023-02-15,2023-11-15
3,공간정보산업조사,Spatial Information Industry Survey,Details about spatial information industry,Summary about spatial data,3,200,3,토지,공간정보산업조사,,N,2023-03-01,2023-11-10
4,건설공사계약통계,Construction Contract Statistics,Details about construction contracts,Summary about construction data,4,180,4,건설,건설공사계약통계,,N,2023-04-20,2023-11-20
5,자동차등록현황보고,Vehicle Registration Report,Details about vehicle registrations,Summary about vehicles,5,240,5,교통/물류,자동차등록현황보고,,N,2023-05-01,2023-11-25



page_num,page_content,knowinfo_id,create_dt,modified_dt
1,This is the first page content for National Geographic Information.,1,2023-01-01,2023-11-30
2,This is the second page content for National Geographic Information.,1,2023-01-02,2023-11-30
1,This is the first page content for Unsold Housing Report.,2,2023-02-15,2023-11-15
1,This is the first page content for Spatial Information Industry Survey.,3,2023-03-01,2023-11-10
1,This is the first page content for Construction Contract Statistics.,4,2023-04-20,2023-11-20
2,This is the second page content for Construction Contract Statistics.,4,2023-04-21,2023-11-20
1,This is the first page content for Vehicle Registration Report.,5,2023-05-01,2023-11-25





```log
logstash01-1  | 2024/12/01 10:15:27 Setting 'xpack.monitoring.enabled' from environment.
logstash01-1  | Using bundled JDK: /usr/share/logstash/jdk
logstash01-1  | Sending Logstash logs to /usr/share/logstash/logs which is now configured via log4j2.properties
logstash01-1  | [2024-12-01T10:15:46,998][WARN ][deprecation.logstash.runner] NOTICE: Running Logstash as superuser is not recommended and won't be allowed in the future. Set 'allow_superuser' to 'false' to avoid startup errors in future releases.
logstash01-1  | [2024-12-01T10:15:47,014][INFO ][logstash.runner          ] Log4j configuration path used is: /usr/share/logstash/config/log4j2.properties
logstash01-1  | [2024-12-01T10:15:47,016][INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"8.7.1", "jruby.version"=>"jruby 9.3.10.0 (2.6.8) 2023-02-01 107b2e6697 OpenJDK 64-Bit Server VM 17.0.7+7 on 17.0.7+7 +indy +jit [x86_64-linux]"}
logstash01-1  | [2024-12-01T10:15:47,020][INFO ][logstash.runner          ] JVM bootstrap flags: [-Xms1g, -Xmx1g, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djruby.compile.invokedynamic=true, -XX:+HeapDumpOnOutOfMemoryError, -Djava.security.egd=file:/dev/urandom, -Dlog4j2.isThreadContextMapInheritable=true, -Dls.cgroup.cpuacct.path.override=/, -Dls.cgroup.cpu.path.override=/, -Djruby.regexp.interruptible=true, -Djdk.io.File.enableADS=true, --add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED, --add-opens=java.base/java.security=ALL-UNNAMED, --add-opens=java.base/java.io=ALL-UNNAMED, --add-opens=java.base/java.nio.channels=ALL-UNNAMED, --add-opens=java.base/sun.nio.ch=ALL-UNNAMED, --add-opens=java.management/sun.management=ALL-UNNAMED]
logstash01-1  | [2024-12-01T10:15:48,175][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600, :ssl_enabled=>false}
logstash01-1  | [2024-12-01T10:15:48,679][INFO ][org.reflections.Reflections] Reflections took 184 ms to scan 1 urls, producing 132 keys and 462 values
logstash01-1  | [2024-12-01T10:15:49,104][INFO ][logstash.javapipeline    ] Pipeline `main` is configured with `pipeline.ecs_compatibility: v8` setting. All plugins in this pipeline will default to `ecs_compatibility => v8` unless explicitly configured otherwise.
logstash01-1  | [2024-12-01T10:15:49,130][INFO ][logstash.outputs.elasticsearch][main] New Elasticsearch output {:class=>"LogStash::Outputs::ElasticSearch", :hosts=>["https://es01:9200"]}
logstash01-1  | [2024-12-01T10:15:49,773][INFO ][logstash.outputs.elasticsearch][main] Elasticsearch pool URLs updated {:changes=>{:removed=>[], :added=>[https://elastic:xxxxxx@es01:9200/]}}
logstash01-1  | [2024-12-01T10:15:50,539][WARN ][logstash.outputs.elasticsearch][main] Restored connection to ES instance {:url=>"https://elastic:xxxxxx@es01:9200/"}
logstash01-1  | [2024-12-01T10:15:50,555][INFO ][logstash.outputs.elasticsearch][main] Elasticsearch version determined (8.7.1) {:es_version=>8}
logstash01-1  | [2024-12-01T10:15:50,556][WARN ][logstash.outputs.elasticsearch][main] Detected a 6.x and above cluster: the `type` event field won't be used to determine the document _type {:es_version=>8}
logstash01-1  | [2024-12-01T10:15:50,583][INFO ][logstash.outputs.elasticsearch][main] Not eligible for data streams because config contains one or more settings that are not compatible with data streams: {"index"=>"logstash-%{+YYYY.MM.dd}"}
logstash01-1  | [2024-12-01T10:15:50,584][INFO ][logstash.outputs.elasticsearch][main] Data streams auto configuration (`data_stream => auto` or unset) resolved to `false`
logstash01-1  | [2024-12-01T10:15:50,586][WARN ][logstash.outputs.elasticsearch][main] Elasticsearch Output configured with `ecs_compatibility => v8`, which resolved to an UNRELEASED preview of version 8.0.0 of the Elastic Common Schema. Once ECS v8 and an updated release of this plugin are publicly available, you will need to update this plugin to resolve this warning.
logstash01-1  | [2024-12-01T10:15:50,610][INFO ][logstash.outputs.elasticsearch][main] Using a default mapping template {:es_version=>8, :ecs_compatibility=>:v8}
logstash01-1  | [2024-12-01T10:15:50,629][INFO ][logstash.javapipeline    ][main] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>8, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50, "pipeline.max_inflight"=>1000, "pipeline.sources"=>["/usr/share/logstash/pipeline/logstash.conf"], :thread=>"#<Thread:0x5219239a@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}
logstash01-1  | [2024-12-01T10:15:51,737][INFO ][logstash.javapipeline    ][main] Pipeline Java execution initialization time {"seconds"=>1.11}
logstash01-1  | [2024-12-01T10:15:51,754][INFO ][logstash.inputs.file     ][main] No sincedb_path set, generating one based on the "path" setting {:sincedb_path=>"/usr/share/logstash/data/plugins/inputs/file/.sincedb_2eeb8a903dd881b1d75557987eb85a8d", :path=>["/usr/share/logstash/ingest_data/*"]}
logstash01-1  | [2024-12-01T10:15:51,757][INFO ][logstash.javapipeline    ][main] Pipeline started {"pipeline.id"=>"main"}
logstash01-1  | [2024-12-01T10:15:51,765][INFO ][filewatch.observingtail  ][main][f0985dd64cff56a34d078f7b1bfc90fa1238d158ecd15601b492f29a1ecaf1a4] START, creating Discoverer, Watch with file and sincedb collections
logstash01-1  | [2024-12-01T10:15:51,780][INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
logstash01-1  | [2024-12-01T10:15:58,727][WARN ][logstash.runner          ] SIGTERM received. Shutting down.
logstash01-1  | [2024-12-01T10:15:58,730][INFO ][filewatch.observingtail  ] QUIT - closing all files and shutting down.
logstash01-1  | [2024-12-01T10:15:59,590][INFO ][logstash.javapipeline    ][main] Pipeline terminated {"pipeline.id"=>"main"}
logstash01-1  | [2024-12-01T10:15:59,770][INFO ][logstash.pipelinesregistry] Removed pipeline from registry successfully {:pipeline_id=>:main}
logstash01-1  | [2024-12-01T10:15:59,784][INFO ][logstash.runner          ] Logstash shut down.
logstash01-1  | 2024/12/01 10:17:35 Setting 'xpack.monitoring.enabled' from environment.
logstash01-1  | Using bundled JDK: /usr/share/logstash/jdk
logstash01-1  | Sending Logstash logs to /usr/share/logstash/logs which is now configured via log4j2.properties
logstash01-1  | [2024-12-01T10:17:55,203][WARN ][deprecation.logstash.runner] NOTICE: Running Logstash as superuser is not recommended and won't be allowed in the future. Set 'allow_superuser' to 'false' to avoid startup errors in future releases.
logstash01-1  | [2024-12-01T10:17:55,219][INFO ][logstash.runner          ] Log4j configuration path used is: /usr/share/logstash/config/log4j2.properties
logstash01-1  | [2024-12-01T10:17:55,220][INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"8.7.1", "jruby.version"=>"jruby 9.3.10.0 (2.6.8) 2023-02-01 107b2e6697 OpenJDK 64-Bit Server VM 17.0.7+7 on 17.0.7+7 +indy +jit [x86_64-linux]"}
logstash01-1  | [2024-12-01T10:17:55,224][INFO ][logstash.runner          ] JVM bootstrap flags: [-Xms1g, -Xmx1g, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djruby.compile.invokedynamic=true, -XX:+HeapDumpOnOutOfMemoryError, -Djava.security.egd=file:/dev/urandom, -Dlog4j2.isThreadContextMapInheritable=true, -Dls.cgroup.cpuacct.path.override=/, -Dls.cgroup.cpu.path.override=/, -Djruby.regexp.interruptible=true, -Djdk.io.File.enableADS=true, --add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED, --add-opens=java.base/java.security=ALL-UNNAMED, --add-opens=java.base/java.io=ALL-UNNAMED, --add-opens=java.base/java.nio.channels=ALL-UNNAMED, --add-opens=java.base/sun.nio.ch=ALL-UNNAMED, --add-opens=java.management/sun.management=ALL-UNNAMED]
logstash01-1  | [2024-12-01T10:17:56,496][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600, :ssl_enabled=>false}
logstash01-1  | [2024-12-01T10:17:57,040][INFO ][org.reflections.Reflections] Reflections took 206 ms to scan 1 urls, producing 132 keys and 462 values
logstash01-1  | [2024-12-01T10:17:57,513][INFO ][logstash.javapipeline    ] Pipeline `main` is configured with `pipeline.ecs_compatibility: v8` setting. All plugins in this pipeline will default to `ecs_compatibility => v8` unless explicitly configured otherwise.
logstash01-1  | [2024-12-01T10:17:57,546][INFO ][logstash.outputs.elasticsearch][main] New Elasticsearch output {:class=>"LogStash::Outputs::ElasticSearch", :hosts=>["https://es01:9200"]}
logstash01-1  | [2024-12-01T10:17:57,774][INFO ][logstash.outputs.elasticsearch][main] Elasticsearch pool URLs updated {:changes=>{:removed=>[], :added=>[https://elastic:xxxxxx@es01:9200/]}}
logstash01-1  | [2024-12-01T10:17:58,172][WARN ][logstash.outputs.elasticsearch][main] Restored connection to ES instance {:url=>"https://elastic:xxxxxx@es01:9200/"}
logstash01-1  | [2024-12-01T10:17:58,184][INFO ][logstash.outputs.elasticsearch][main] Elasticsearch version determined (8.7.1) {:es_version=>8}
logstash01-1  | [2024-12-01T10:17:58,185][WARN ][logstash.outputs.elasticsearch][main] Detected a 6.x and above cluster: the `type` event field won't be used to determine the document _type {:es_version=>8}
logstash01-1  | [2024-12-01T10:17:58,206][INFO ][logstash.outputs.elasticsearch][main] Not eligible for data streams because config contains one or more settings that are not compatible with data streams: {"index"=>"logstash-%{+YYYY.MM.dd}"}
logstash01-1  | [2024-12-01T10:17:58,207][INFO ][logstash.outputs.elasticsearch][main] Data streams auto configuration (`data_stream => auto` or unset) resolved to `false`
logstash01-1  | [2024-12-01T10:17:58,209][WARN ][logstash.outputs.elasticsearch][main] Elasticsearch Output configured with `ecs_compatibility => v8`, which resolved to an UNRELEASED preview of version 8.0.0 of the Elastic Common Schema. Once ECS v8 and an updated release of this plugin are publicly available, you will need to update this plugin to resolve this warning.
logstash01-1  | [2024-12-01T10:17:58,224][INFO ][logstash.outputs.elasticsearch][main] Using a default mapping template {:es_version=>8, :ecs_compatibility=>:v8}
logstash01-1  | [2024-12-01T10:17:58,237][INFO ][logstash.javapipeline    ][main] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>8, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50, "pipeline.max_inflight"=>1000, "pipeline.sources"=>["/usr/share/logstash/pipeline/logstash.conf"], :thread=>"#<Thread:0x94ad35@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}
logstash01-1  | [2024-12-01T10:17:59,222][INFO ][logstash.javapipeline    ][main] Pipeline Java execution initialization time {"seconds"=>0.98}
logstash01-1  | [2024-12-01T10:17:59,240][INFO ][logstash.inputs.file     ][main] No sincedb_path set, generating one based on the "path" setting {:sincedb_path=>"/usr/share/logstash/data/plugins/inputs/file/.sincedb_2eeb8a903dd881b1d75557987eb85a8d", :path=>["/usr/share/logstash/ingest_data/*"]}
logstash01-1  | [2024-12-01T10:17:59,255][INFO ][logstash.javapipeline    ][main] Pipeline started {"pipeline.id"=>"main"}
logstash01-1  | [2024-12-01T10:17:59,269][INFO ][filewatch.observingtail  ][main][f0985dd64cff56a34d078f7b1bfc90fa1238d158ecd15601b492f29a1ecaf1a4] START, creating Discoverer, Watch with file and sincedb collections
logstash01-1  | [2024-12-01T10:17:59,271][INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
```



```
[WARN ][deprecation.logstash.runner] NOTICE: Running Logstash as superuser is not recommended and won't be allowed in the future. Set 'allow_superuser' to 'false' to avoid startup errors in future releases.
[INFO ][logstash.runner          ] Log4j configuration path used is: /usr/share/logstash/config/log4j2.properties
[INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"8.7.1", "jruby.version"=>"jruby 9.3.10.0 (2.6.8) 2023-02-01 107b2e6697 OpenJDK 64-Bit Server VM 17.0.7+7 on 17.0.7+7 +indy +jit [x86_64-linux]"}
[INFO ][logstash.runner          ] JVM bootstrap flags: [-Xms1g, -Xmx1g, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djruby.compile.invokedynamic=true, -XX:+HeapDumpOnOutOfMemoryError, -Djava.security.egd=file:/dev/urandom, -Dlog4j2.isThreadContextMapInheritable=true, -Dls.cgroup.cpuacct.path.override=/, -Dls.cgroup.cpu.path.override=/, -Djruby.regexp.interruptible=true, -Djdk.io.File.enableADS=true, --add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED, --add-opens=java.base/java.security=ALL-UNNAMED, --add-opens=java.base/java.io=ALL-UNNAMED, --add-opens=java.base/java.nio.channels=ALL-UNNAMED, --add-opens=java.base/sun.nio.ch=ALL-UNNAMED, --add-opens=java.management/sun.management=ALL-UNNAMED]
[INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600, :ssl_enabled=>false}
[INFO ][org.reflections.Reflections] Reflections took 184 ms to scan 1 urls, producing 132 keys and 462 values
[INFO ][logstash.javapipeline    ] Pipeline `main` is configured with `pipeline.ecs_compatibility: v8` setting. All plugins in this pipeline will default to `ecs_compatibility => v8` unless explicitly configured otherwise.
[INFO ][logstash.outputs.elasticsearch][main] New Elasticsearch output {:class=>"LogStash::Outputs::ElasticSearch", :hosts=>["https://es01:9200"]}
[INFO ][logstash.outputs.elasticsearch][main] Elasticsearch pool URLs updated {:changes=>{:removed=>[], :added=>[https://elastic:xxxxxx@es01:9200/]}}
[WARN ][logstash.outputs.elasticsearch][main] Restored connection to ES instance {:url=>"https://elastic:xxxxxx@es01:9200/"}
[INFO ][logstash.outputs.elasticsearch][main] Elasticsearch version determined (8.7.1) {:es_version=>8}
[WARN ][logstash.outputs.elasticsearch][main] Detected a 6.x and above cluster: the `type` event field won't be used to determine the document _type {:es_version=>8}
[INFO ][logstash.outputs.elasticsearch][main] Not eligible for data streams because config contains one or more settings that are not compatible with data streams: {"index"=>"logstash-%{+YYYY.MM.dd}"}
[INFO ][logstash.outputs.elasticsearch][main] Data streams auto configuration (`data_stream => auto` or unset) resolved to `false`
[WARN ][logstash.outputs.elasticsearch][main] Elasticsearch Output configured with `ecs_compatibility => v8`, which resolved to an UNRELEASED preview of version 8.0.0 of the Elastic Common Schema. Once ECS v8 and an updated release of this plugin are publicly available, you will need to update this plugin to resolve this warning.
[INFO ][logstash.outputs.elasticsearch][main] Using a default mapping template {:es_version=>8, :ecs_compatibility=>:v8}
[INFO ][logstash.javapipeline    ][main] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>8, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50, "pipeline.max_inflight"=>1000, "pipeline.sources"=>["/usr/share/logstash/pipeline/logstash.conf"], :thread=>"#<Thread:0x5219239a@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}
[INFO ][logstash.javapipeline    ][main] Pipeline Java execution initialization time {"seconds"=>1.11}
[INFO ][logstash.inputs.file     ][main] No sincedb_path set, generating one based on the "path" setting {:sincedb_path=>"/usr/share/logstash/data/plugins/inputs/file/.sincedb_2eeb8a903dd881b1d75557987eb85a8d", :path=>["/usr/share/logstash/ingest_data/*"]}
[INFO ][logstash.javapipeline    ][main] Pipeline started {"pipeline.id"=>"main"}
[INFO ][filewatch.observingtail  ][main][f0985dd64cff56a34d078f7b1bfc90fa1238d158ecd15601b492f29a1ecaf1a4] START, creating Discoverer, Watch with file and sincedb collections
[INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
[WARN ][logstash.runner          ] SIGTERM received. Shutting down.
[INFO ][filewatch.observingtail  ] QUIT - closing all files and shutting down.
[INFO ][logstash.javapipeline    ][main] Pipeline terminated {"pipeline.id"=>"main"}
[INFO ][logstash.pipelinesregistry] Removed pipeline from registry successfully {:pipeline_id=>:main}
[INFO ][logstash.runner          ] Logstash shut down.
ng 'xpack.monitoring.enabled' from environment.
hare/logstash/jdk
/usr/share/logstash/logs which is now configured via log4j2.properties
[WARN ][deprecation.logstash.runner] NOTICE: Running Logstash as superuser is not recommended and won't be allowed in the future. Set 'allow_superuser' to 'false' to avoid startup errors in future releases.
[INFO ][logstash.runner          ] Log4j configuration path used is: /usr/share/logstash/config/log4j2.properties
[INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"8.7.1", "jruby.version"=>"jruby 9.3.10.0 (2.6.8) 2023-02-01 107b2e6697 OpenJDK 64-Bit Server VM 17.0.7+7 on 17.0.7+7 +indy +jit [x86_64-linux]"}
[INFO ][logstash.runner          ] JVM bootstrap flags: [-Xms1g, -Xmx1g, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djruby.compile.invokedynamic=true, -XX:+HeapDumpOnOutOfMemoryError, -Djava.security.egd=file:/dev/urandom, -Dlog4j2.isThreadContextMapInheritable=true, -Dls.cgroup.cpuacct.path.override=/, -Dls.cgroup.cpu.path.override=/, -Djruby.regexp.interruptible=true, -Djdk.io.File.enableADS=true, --add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED, --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED, --add-opens=java.base/java.security=ALL-UNNAMED, --add-opens=java.base/java.io=ALL-UNNAMED, --add-opens=java.base/java.nio.channels=ALL-UNNAMED, --add-opens=java.base/sun.nio.ch=ALL-UNNAMED, --add-opens=java.management/sun.management=ALL-UNNAMED]
[INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600, :ssl_enabled=>false}
[INFO ][org.reflections.Reflections] Reflections took 206 ms to scan 1 urls, producing 132 keys and 462 values
[INFO ][logstash.javapipeline    ] Pipeline `main` is configured with `pipeline.ecs_compatibility: v8` setting. All plugins in this pipeline will default to `ecs_compatibility => v8` unless explicitly configured otherwise.
[INFO ][logstash.outputs.elasticsearch][main] New Elasticsearch output {:class=>"LogStash::Outputs::ElasticSearch", :hosts=>["https://es01:9200"]}
[INFO ][logstash.outputs.elasticsearch][main] Elasticsearch pool URLs updated {:changes=>{:removed=>[], :added=>[https://elastic:xxxxxx@es01:9200/]}}
[WARN ][logstash.outputs.elasticsearch][main] Restored connection to ES instance {:url=>"https://elastic:xxxxxx@es01:9200/"}
[INFO ][logstash.outputs.elasticsearch][main] Elasticsearch version determined (8.7.1) {:es_version=>8}
[WARN ][logstash.outputs.elasticsearch][main] Detected a 6.x and above cluster: the `type` event field won't be used to determine the document _type {:es_version=>8}
[INFO ][logstash.outputs.elasticsearch][main] Not eligible for data streams because config contains one or more settings that are not compatible with data streams: {"index"=>"logstash-%{+YYYY.MM.dd}"}
[INFO ][logstash.outputs.elasticsearch][main] Data streams auto configuration (`data_stream => auto` or unset) resolved to `false`
[WARN ][logstash.outputs.elasticsearch][main] Elasticsearch Output configured with `ecs_compatibility => v8`, which resolved to an UNRELEASED preview of version 8.0.0 of the Elastic Common Schema. Once ECS v8 and an updated release of this plugin are publicly available, you will need to update this plugin to resolve this warning.
[INFO ][logstash.outputs.elasticsearch][main] Using a default mapping template {:es_version=>8, :ecs_compatibility=>:v8}
[INFO ][logstash.javapipeline    ][main] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>8, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50, "pipeline.max_inflight"=>1000, "pipeline.sources"=>["/usr/share/logstash/pipeline/logstash.conf"], :thread=>"#<Thread:0x94ad35@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}
[INFO ][logstash.javapipeline    ][main] Pipeline Java execution initialization time {"seconds"=>0.98}
[INFO ][logstash.inputs.file     ][main] No sincedb_path set, generating one based on the "path" setting {:sincedb_path=>"/usr/share/logstash/data/plugins/inputs/file/.sincedb_2eeb8a903dd881b1d75557987eb85a8d", :path=>["/usr/share/logstash/ingest_data/*"]}
[INFO ][logstash.javapipeline    ][main] Pipeline started {"pipeline.id"=>"main"}
[INFO ][filewatch.observingtail  ][main][f0985dd64cff56a34d078f7b1bfc90fa1238d158ecd15601b492f29a1ecaf1a4] START, creating Discoverer, Watch with file and sincedb collections
[INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
```

-Xms1g
-Xmx1g
-Djava.awt.headless=true
-Dfile.encoding=UTF-8
-Djruby.compile.invokedynamic=true
-XX:+HeapDumpOnOutOfMemoryError
-Djava.security.egd=file:/dev/urandom
-Dlog4j2.isThreadContextMapInheritable=true
-Dls.cgroup.cpuacct.path.override=/
-Dls.cgroup.cpu.path.override=/
-Djruby.regexp.interruptible=true
-Djdk.io.File.enableADS=true
--add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED
--add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED
--add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED
--add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED
--add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED
--add-opens=java.base/java.security=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED
--add-opens=java.base/java.nio.channels=ALL-UNNAMED
--add-opens=java.base/sun.nio.ch=ALL-UNNAMED
--add-opens=java.management/sun.management=ALL-UNNAMED



[INFO ][logstash.javapipeline    ][main] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>8, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50, "pipeline.max_inflight"=>1000, "pipeline.sources"=>["/usr/share/logstash/pipeline/logstash.conf"], :thread=>"#<Thread:0x5219239a@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}




root@50b56c60356e:/usr/share/logstash/config# cat pipelines.yml
# This file is where you define your pipelines. You can define multiple.
# For more information on multiple pipelines, see the documentation:
#   https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html

- pipeline.id: main
  path.config: "/usr/share/logstash/pipeline"
root@50b56c60356e:/usr/share/logstash/config# exit




pipelines.yml




    volumes:
      - certs:/usr/share/logstash/certs
      - logstashdata01:/usr/share/logstash/data
      - "./logstash_ingest_data/:/usr/share/logstash/ingest_data/"
      - "./pipelines.yml:/usr/share/logstash/config/pipelines.yml:rw"
      - "./jdbc/:/usr/share/logstash/jdbc/:rw"
      - "./custom_pipeline/:/usr/share/logstash/custom_pipeline/:rw"
    command: >
      bash -c '
        chown logstash:logstash /usr/share/logstash/jdbc/postgresql-42.7.4.jar
        chmod 644 /usr/share/logstash/jdbc/postgresql-42.7.4.jar
        ls -l /usr/share/logstash/jdbc/postgresql-42.7.4.jar

        echo "test config file"
        logstash -f /usr/share/logstash/custom_pipeline/parent_knowinfo_pipeline.conf --config.test_and_exit
        logstash -f /usr/share/logstash/custom_pipeline/child_knowinfo_pipeline.conf --config.test_and_exit

        echo "executing logstash"
        logstash
        '




logstash01-1  | 2024/12/01 11:12:21 Setting 'xpack.monitoring.enabled' from environment.
logstash01-1  | -rw-r--r-- 1 logstash logstash 1086687 Dec  1 09:08 /usr/share/logstash/jdbc/postgresql-42.7.4.jar

logstash01-1  | Configuration OK
logstash01-1  | [2024-12-01T11:18:55,304][INFO ][logstash.runner          ] Using config.test_and_exit mode. Config Validation Result: OK. Exiting Logstash

logstash01-1  | Configuration OK
logstash01-1  | [2024-12-01T11:19:22,698][INFO ][logstash.runner          ] Using config.test_and_exit mode. Config Validation Result: OK. Exiting Logstash

logstash01-1  | [2024-12-01T11:19:49,999][ERROR][logstash.javapipeline    ][koai_knowinfo_child] Pipeline error {:pipeline_id=>"koai_knowinfo_child", :exception=>#<LogStash::PluginLoadingError: unable to load "/usr/share/logstash/jdbc/postgresql-42.7.4.jar" from :jdbc_driver_library, file not readable (please check user and group permissions for the path)>, :backtrace=>["/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-integration-jdbc-5.4.1/lib/logstash/plugin_mixins/jdbc/common.rb:59:in `block in load_driver_jars'", "org/jruby/RubyArray.java:1865:in `each'", "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-integration-jdbc-5.4.1/lib/logstash/plugin_mixins/jdbc/common.rb:54:in `load_driver_jars'", "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-integration-jdbc-5.4.1/lib/logstash/plugin_mixins/jdbc/common.rb:34:in `load_driver'", "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-integration-jdbc-5.4.1/lib/logstash/inputs/jdbc.rb:307:in `register'", "/usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-mixin-ecs_compatibility_support-1.3.0-java/lib/logstash/plugin_mixins/ecs_compatibility_support/target_check.rb:48:in `register'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:237:in `block in register_plugins'", "org/jruby/RubyArray.java:1865:in `each'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:236:in `register_plugins'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:395:in `start_inputs'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:320:in `start_workers'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:194:in `run'", "/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:146:in `block in start'"], "pipeline.sources"=>["/usr/share/logstash/custom_pipeline/child_knowinfo_pipeline.conf"], :thread=>"#<Thread:0x1016fed@/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:134 run>"}
logstash01-1  | [2024-12-01T11:19:50,000][INFO ][logstash.javapipeline    ][koai_knowinfo_child] Pipeline terminated {"pipeline.id"=>"koai_knowinfo_child"}
logstash01-1  | [2024-12-01T11:19:50,005][ERROR][logstash.agent           ] Failed to execute action {:id=>:koai_knowinfo_child, :action_type=>LogStash::ConvergeResult::FailedAction, :message=>"Could not execute action: PipelineAction::Create<koai_knowinfo_child>, action_result: false", :backtrace=>nil}
logstash01-1  | [2024-12-01T11:19:50,026][INFO ][logstash.runner          ] Logstash shut down.
logstash01-1  | [2024-12-01T11:19:50,031][FATAL][org.logstash.Logstash    ] Logstash stopped processing because of an error: (SystemExit) exit
logstash01-1  | org.jruby.exceptions.SystemExit: (SystemExit) exit
logstash01-1  |         at org.jruby.RubyKernel.exit(org/jruby/RubyKernel.java:790) ~[jruby.jar:?]
logstash01-1  |         at org.jruby.RubyKernel.exit(org/jruby/RubyKernel.java:753) ~[jruby.jar:?]
logstash01-1  |         at usr.share.logstash.lib.bootstrap.environment.<main>(/usr/share/logstash/lib/bootstrap/environment.rb:91) ~[?:?]



logstash01-1  | 2024/12/01 11:33:19 Setting 'xpack.monitoring.enabled' from environment.
logstash01-1  | chown: cannot access '/usr/share/logstash/jdbc/postgresql-42.7.4.jar': No such file or directory
logstash01-1  | chmod: cannot access '/usr/share/logstash/jdbc/postgresql-42.7.4.jar': No such file or directory
logstash01-1  | ls: cannot access '/usr/share/logstash/jdbc/postgresql-42.7.4.jar': No such file or directory
logstash01-1  | executing logstash
l



```
infra/docker/ELK on  main [✘!?] ❯ docker ps
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED          STATUS                            PORTS                                                 NAMES
eaa24bbc71b2   docker.elastic.co/logstash/logstash:8.7.1             "/usr/local/bin/dock…"   40 seconds ago   Up 7 seconds                      5044/tcp, 9600/tcp                                    elk_playground-logstash01-1
a78da50f0ef2   docker.elastic.co/kibana/kibana:8.7.1                 "/bin/tini -- /usr/l…"   44 minutes ago   Up 7 seconds (health: starting)   0.0.0.0:5601->5601/tcp, :::5601->5601/tcp             elk_playground-kibana-1
7769fe766469   docker.elastic.co/elasticsearch/elasticsearch:8.7.1   "/bin/tini -- /usr/l…"   44 minutes ago   Up 37 seconds (healthy)           0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 9300/tcp   elk_playground-es01-1
9d85909b203a   postgres:16                                           "docker-entrypoint.s…"   44 minutes ago   Up 39 seconds (healthy)           0.0.0.0:5433->5432/tcp, [::]:5433->5432/tcp           elk_playground-postgres01-1

infra/docker/ELK on  main [✘!?] ❯ docker exec -it eaa24bbc71b2 bash
root@eaa24bbc71b2:/usr/share/logstash# apt-get update && apt-get install -y postgresql-client
Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [128 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease [128 kB]
Get:4 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [1,278 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease [128 kB]
Get:6 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1,568 kB]
Get:7 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [30.9 kB]
Get:8 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [4,109 kB]
Get:9 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [33.5 kB]
Get:10 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [4,581 kB]
Get:11 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [4,137 kB]
Get:12 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [4,304 kB]
Get:13 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [28.6 kB]
Get:14 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [55.2 kB]
Fetched 20.5 MB in 5s (4,153 kB/s)
Reading package lists... Done
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libbsd0 libedit2 libpq5 libreadline8 netbase postgresql-client-12 postgresql-client-common
  readline-common
Suggested packages:
  postgresql-12 postgresql-doc-12 readline-doc
The following NEW packages will be installed:
  libbsd0 libedit2 libpq5 libreadline8 netbase postgresql-client postgresql-client-12
  postgresql-client-common readline-common
0 upgraded, 9 newly installed, 0 to remove and 56 not upgraded.
Need to get 1,534 kB of archives.
After this operation, 5,521 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal/main amd64 libbsd0 amd64 0.10.0-1 [45.4 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal/main amd64 readline-common all 8.0-4 [53.5 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal/main amd64 libreadline8 amd64 8.0-4 [131 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 netbase all 6.1 [13.1 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal/main amd64 libedit2 amd64 3.1-20191231-1 [87.0 kB]
Get:6 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libpq5 amd64 12.20-0ubuntu0.20.04.1 [117 kB]
Get:7 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 postgresql-client-common all 214ubuntu0.1 [28.2 kB]
Get:8 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 postgresql-client-12 amd64 12.20-0ubuntu0.20.04.1 [1,055 kB]
Get:9 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 postgresql-client all 12+214ubuntu0.1 [3,940 B]
Fetched 1,534 kB in 2s (630 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package libbsd0:amd64.
(Reading database ... 5274 files and directories currently installed.)
Preparing to unpack .../0-libbsd0_0.10.0-1_amd64.deb ...
Unpacking libbsd0:amd64 (0.10.0-1) ...
Selecting previously unselected package readline-common.
Preparing to unpack .../1-readline-common_8.0-4_all.deb ...
Unpacking readline-common (8.0-4) ...
Selecting previously unselected package libreadline8:amd64.
Preparing to unpack .../2-libreadline8_8.0-4_amd64.deb ...
Unpacking libreadline8:amd64 (8.0-4) ...
Selecting previously unselected package netbase.
Preparing to unpack .../3-netbase_6.1_all.deb ...
Unpacking netbase (6.1) ...
Selecting previously unselected package libedit2:amd64.
Preparing to unpack .../4-libedit2_3.1-20191231-1_amd64.deb ...
Unpacking libedit2:amd64 (3.1-20191231-1) ...
Selecting previously unselected package libpq5:amd64.
Preparing to unpack .../5-libpq5_12.20-0ubuntu0.20.04.1_amd64.deb ...
Unpacking libpq5:amd64 (12.20-0ubuntu0.20.04.1) ...
Selecting previously unselected package postgresql-client-common.
Preparing to unpack .../6-postgresql-client-common_214ubuntu0.1_all.deb ...
Unpacking postgresql-client-common (214ubuntu0.1) ...
Selecting previously unselected package postgresql-client-12.
Preparing to unpack .../7-postgresql-client-12_12.20-0ubuntu0.20.04.1_amd64.deb ...
Unpacking postgresql-client-12 (12.20-0ubuntu0.20.04.1) ...
Selecting previously unselected package postgresql-client.
Preparing to unpack .../8-postgresql-client_12+214ubuntu0.1_all.deb ...
Unpacking postgresql-client (12+214ubuntu0.1) ...
Setting up libpq5:amd64 (12.20-0ubuntu0.20.04.1) ...
Setting up netbase (6.1) ...
Setting up libbsd0:amd64 (0.10.0-1) ...
Setting up readline-common (8.0-4) ...
Setting up postgresql-client-common (214ubuntu0.1) ...
Setting up libedit2:amd64 (3.1-20191231-1) ...
Setting up libreadline8:amd64 (8.0-4) ...
Setting up postgresql-client-12 (12.20-0ubuntu0.20.04.1) ...
update-alternatives: using /usr/share/postgresql/12/man/man1/psql.1.gz to provide /usr/share/man/man1/psql.1.gz (psql.1.gz) in auto mode
Setting up postgresql-client (12+214ubuntu0.1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
root@eaa24bbc71b2:/usr/share/logstash# printenv
xpack.monitoring.enabled=false
ELASTIC_HOSTS=https://es01:9200
HOSTNAME=eaa24bbc71b2
ELASTIC_CONTAINER=true
PWD=/usr/share/logstash
LOGSTASH_JDBC_PASSWORD="test"
LOGSTASH_JDBC_DRIVER_JAR_LOCATION="/usr/share/logstash/jdbc/postgresql-42.7.4.jar"
LOGSTASH_JDBC_URL="jdbc:postgresql://localhost:5432/test_db"
HOME=/root
LANG=en_US.UTF-8
ELASTIC_PASSWORD=changeme
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
LOGSTASH_JDBC_DRIVER="org.postgresql.Driver"
TERM=xterm
SHLVL=1
LOGSTASH_JDBC_USERNAME="test"
ELASTIC_USER=elastic
LC_ALL=en_US.UTF-8
PATH=/usr/share/logstash/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/printenv
root@eaa24bbc71b2:/usr/share/logstash# PGPASSWORD=$POSTGRES_PASSWORD psql -h postgres01 -U $POSTGRES_USER -d $POSTGRES_DB
Password for user -d:
root@eaa24bbc71b2:/usr/share/logstash# psql -h postgres01 -U test -d test_db
Password for user test:
psql (12.20 (Ubuntu 12.20-0ubuntu0.20.04.1), server 16.6 (Debian 16.6-1.pgdg120+1))
WARNING: psql major version 12, server major version 16.
         Some psql features might not work.
Type "help" for help.

test_db=> \dn
        List of schemas
    Name    |       Owner
------------+-------------------
 playground | test
 public     | pg_database_owner
(2 rows)

test_db=> \dt
             List of relations
 Schema |       Name       | Type  | Owner
--------+------------------+-------+-------
 public | knowinfo         | table | test
 public | knowinfo_content | table | test
(2 rows)

test_db=> \dS knowinfo
                          Table "public.knowinfo"
     Column     |          Type           | Collation | Nullable | Default
----------------+-------------------------+-----------+----------+---------
 knowinfo_id    | integer                 |           |          |
 kor_name       | character varying(100)  |           |          |
 eng_name       | character varying(100)  |           |          |
 expln          | text                    |           |          |
 smummary       | character varying(1000) |           |          |
 resource_code  | character varying(100)  |           |          |
 download_count | integer                 |           |          |
 department_id  | integer                 |           |          |
 lcategory_name | character varying(100)  |           |          |
 mcategory_name | character varying(100)  |           |          |
 scategory_name | character varying(100)  |           |          |
 del_yn         | character(1)            |           |          |
 create_dt      | date                    |           |          |
 modified_dt    | date                    |           |          |

test_db=> ^C
test_db=> \q
root@eaa24bbc71b2:/usr/share/logstash#
```

logstash에서 postgresql에 연결은 가능하다


 5653  2024-12-01 12:41:30 docker cp elk_playground-es01-1:/usr/share/elasticsearch/config/certs/ca/ca.crt /tmp/.
 5654  2024-12-01 12:41:55 curl --cacert /tmp/ca.crt -u ealstic:changeme https://localhost:9200
 5655  2024-12-01 12:42:01 curl --cacert /tmp/ca.crt -u ealstic:changeme https://localhost:9200?pretty
 5656  2024-12-01 12:42:28 curl --cacert /tmp/ca.crt -u elastic:changeme https://localhost:9200?pretty
 6026  2024-12-01 21:45:37 history | grep cert

infra/docker/ELK on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme https://localhost:9200?pretty
{
  "name" : "es01",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "TosEP16zTg6_kKneoRXK4g",
  "version" : {
    "number" : "8.7.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "f229ed3f893a515d590d0f39b05f68913e2d9b53",
    "build_date" : "2023-04-27T04:33:42.127815583Z",
    "build_snapshot" : false,
    "lucene_version" : "9.5.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}



infra/docker/ELK on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -XDELETE https://loca
lhost:9200/knowinfo?pretty
{
  "acknowledged" : true
}

docker/ELK/elasticsearch on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -XGET https://localhost:9200/knowinfo/_count?pretty
{
  "count" : 0,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  }
}

docker/ELK/elasticsearch on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -XGET https://localhost:9200/_cat/indiecs?pretty
{
  "error" : "Incorrect HTTP method for uri [/_cat/indiecs?pretty] and method [GET], allowed: [POST]",
  "status" : 405
}

docker/ELK/elasticsearch on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -XGET https://localhost:9200/_cat/indices?pretty
yellow open .ds-.monitoring-kibana-8-mb-2024.12.01-000001   zt6uGDuXTkGpLJ6Iwp2reA 1 1 1237 0   1.1mb   1.1mb
green  open metrics-endpoint.metadata_current_default       m67PqD1dTtG87W9M03eDxQ 1 0    0 0    225b    225b
green  open .fleet-files-endpoint-000001                    3mxAFkgGQDOpwR_RL4hGTw 1 0    0 0    225b    225b
yellow open .ds-.monitoring-logstash-8-mb-2024.12.01-000001 OVD7tyuuSFKxZ5_-mvz5Dg 1 1  415 0 270.4kb 270.4kb
green  open .fleet-file-data-agent-000001                   rBOvhQGeTwaZTSENryuYOw 1 0    0 0    225b    225b
green  open .fleet-files-agent-000001                       6WgdvlozQ5OrwYdJ73_y_w 1 0    0 0    225b    225b
yellow open knowinfo                                        DA-dMWUxT-GANo0Djjwbaw 1 1    0 0    225b    225b
green  open .fleet-file-data-endpoint-000001                GvEkNnOpSI6VfrT7-3lC6g 1 0    0 0    225b    225b
yellow open .ds-filebeat-8.7.1-2024.12.01-000001            dvwiSYa8QhCUoJ8I_1hppw 1 1 3796 0   5.5mb   5.5mb
yellow open .ds-metricbeat-8.7.1-2024.12.01-000001          BBRfadecRvmp5yOEp4GIig 1 1 9473 0  10.7mb  10.7mb
yellow open .ds-.monitoring-es-8-mb-2024.12.01-000001       9gLVDXK3TliDzVVTU-G6Tw 1 1 8774 0   7.6mb   7.6mb



infra/docker/ELK on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -H "Content-Type: application/json" -d @elasticsearch/knowinfo_data.json -XPUT https://localhost:9200/knowinfo
{"error":{"root_cause":[{"type":"illegal_argument_exception","reason":"IOException while reading stopwords_path: /usr/share/elasticsearch/config/stopwords.txt"}],"type":"illegal_argument_exception","reason":"IOException while reading stopwords_path: /usr/share/elasticsearch/config/stopwords.txt","caused_by":{"type":"no_such_file_exception","reason":"/usr/share/elasticsearch/config/stopwords.txt"}},"status":400}
infra/docker/ELK on  main [✘!?] ❯ curl --cacert /tmp/ca.crt -u elastic:changeme -H "Content-Type: application/json" -d @elasticsearch/knowinfo_data.json -XPUT https://localhost:9200/knowinfo?pretty
{
  "error" : {
    "root_cause" : [
      {
        "type" : "illegal_argument_exception",
        "reason" : "IOException while reading stopwords_path: /usr/share/elasticsearch/config/stopwords.txt"
      }
    ],
    "type" : "illegal_argument_exception",
    "reason" : "IOException while reading stopwords_path: /usr/share/elasticsearch/config/stopwords.txt",
    "caused_by" : {
      "type" : "no_such_file_exception",
      "reason" : "/usr/share/elasticsearch/config/stopwords.txt"
    }
  },
  "status" : 400
}



# curl -X GET localhost:9200/_cat/indices # index 목록 조회
# curl -X GET localhost:9200/$INDEX/_settings # index 세팅 조회
# curl -X GET localhost:9200/$INDEX/_settings/$FIELD # index 세팅 특정 필드 조회
# curl -X GET localhost:9200/$INDEX/_mapping # index mapping 조회
# curl -X GET localhost:9200/$INDEX/_count # index document count 조회
# curl -X POST localhost:9200/$INDEX/_search # index document 조회(default 10건 조회)
# curl -X GET localhost:9200/$INDEX/_doc/$DOCUMENT_ID # index document 한 건 조회
# curl -X GET localhost:9200/$INDEX/_analyze -d '{ "tokenizer": "nori_tokenizer", "text": "$SEARCH_WORD" }' # 토크나이징 결과 조회(tokenizer 지정)
# curl -X GET localhost:9200/$INDEX/_analyze -d '{ "analyzer": "korean_analyzer", "text": "$SEARCH_WORD" }' # 토크나이징 결과 조회(analyzer 지정)
# 
# curl -X DELETE localhost:9200/$INDEX # index 제거, 정말로 필요한 경우에만 실행할 것
# curl -X POST localhost:9200/$INDEX/_clone/$INDEX_BAK # index 클론(백업)
# curl -X PUT -H "Content-Type: application/json" -d @$INDEX.json localhost:9200/$INDEX # index 생성



ELK/postgres/sql on  main [✘!?] via 🐍 v3.10.12 (python-elk-py3.10) took 33s ❯ !psql
psql -h localhost -p 5433 -U test -d test_db -f knowinfo.sql
Password for user test:
INSERT 0 5

ELK/postgres/sql on  main [✘!?] via 🐍 v3.10.12 (python-elk-py3.10) ❯ psql -h localhost -p 5433 -U test -d test_db -f knowinfo.sql
Password for user test:
INSERT 0 5

ELK/postgres/sql on  main [✘!?] via 🐍 v3.10.12 (python-elk-py3.10) took 2s ❯ psql -h localhost -p 5433 -U test -d test_db -f knowinfo_content.sql
Password for user test:
INSERT 0 7

ELK/postgres/sql on  main [✘!?] via 🐍 v3.10.12 (python-elk-py3.10) took 2s ❯ psql -h localhost -p 5433 -U test -d test_db -f knowinfo_content.sql
Password for user test:
INSERT 0 7
