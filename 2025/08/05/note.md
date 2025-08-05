```bash
48751  2025-08-05_10:52:18 vi .env
48759  2025-08-05_11:00:09 vi connect.sh
48760  2025-08-05_11:00:36 bash connect.sh 
48817  2025-08-05_11:34:03 bash dump_db.sh > 20250805_idpmart.sql
48900  2025-08-05_12:06:08 wc 20250805_idpmart.sql
48882  2025-08-05_11:54:42 bash dump_db.sh > 20250805_idpmeta.sql
48889  2025-08-05_12:00:38 wc 20250805_idpmeta.sql 
48897  2025-08-05_12:04:45 bash dump_db.sh > 20250805_smartbig.sql
48899  2025-08-05_12:05:17 wc 20250805_smartbig.sql

48835  2025-08-05_11:38:14 mkdir docker_db
48836  2025-08-05_11:38:15 cd docker_db/
48901  2025-08-05_12:06:31 vi .env 
48838  2025-08-05_11:38:24 vi Dockerfile
48839  2025-08-05_11:38:36 vi mariadb.cnf
48840  2025-08-05_11:38:49 vi docker-compose.yml
48842  2025-08-05_11:40:41 docker compose up
48910  2025-08-05_12:07:29 docker compose down

48886  2025-08-05_11:59:48 docker system prune --all
48933  2025-08-05_12:11:47 docker image ls -a
48931  2025-08-05_12:11:40 docker image rm docker_db-mariadb -f
48933  2025-08-05_12:11:47 docker image ls -a
48934  2025-08-05_12:11:51 docker ps -a
48937  2025-08-05_12:12:19 docker container ls -a
48938  2025-08-05_12:12:33 docker container prune
48939  2025-08-05_12:12:38 dokcer ps -a
48945  2025-08-05_12:13:06 docker volume rm docker_db_mariadb_data
48946  2025-08-05_12:13:14 docker volume prune
48947  2025-08-05_12:13:18 docker volume prune -a
48949  2025-08-05_12:13:32 docker volume ls -a

48907  2025-08-05_12:06:55 bash connect.sh 
48869  2025-08-05_11:51:26 vi db_import.sh
48871  2025-08-05_11:52:02 bash db_import.sh 
48996  2025-08-05_14:05:16 bash dump_schema.sh  > schema_info.sql
48997  2025-08-05_14:05:19 wc schema_info.sql 
```
