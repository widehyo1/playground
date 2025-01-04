2_diamol/diamol/2_diamol on  main [!?] ❯ docker container run -d -p 8011:80 -v todo-list:/data --name todo-v1 diamol/ch06-todo-list
f14d4c36c03fd364b763e207f858183b861b1ad7a7dfe7caaa8a02a2040d022d

2_diamol/diamol/2_diamol on  main [!?] ❯ docker volume ls
DRIVER    VOLUME NAME
local     8f88e376bcf97b36d1cfdc12ab6e34cab750d935f856433f4407f34a8ec49b90
local     c2109d4acc518f2221ea5b917f4451162b53901f90daebf707b3329be1fadd64
local     elk_playground_certs
local     elk_playground_esdata01
local     elk_playground_filebeatdata01
local     elk_playground_kibanadata
local     elk_playground_logstashdata01
local     elk_playground_metricbeatdata01
local     elk_playground_postgresdata01
local     f4b39d5351762a8aaab102d7d07de8c76d7080f29453dcd4c1d205c055f2d6dc
local     todo-list

2_diamol/diamol/2_diamol on  main [!?] ❯ docker container inspect --format '{{.Mounts}}' todo-v1
[{volume todo-list /var/lib/docker/volumes/todo-list/_data /data local z true }]

2_diamol/diamol/2_diamol on  main [!?] ❯ docker container rm -f todo-v1
todo-v1

2_diamol/diamol/2_diamol on  main [!?] ❯ docker volume ls
DRIVER    VOLUME NAME
local     8f88e376bcf97b36d1cfdc12ab6e34cab750d935f856433f4407f34a8ec49b90
local     c2109d4acc518f2221ea5b917f4451162b53901f90daebf707b3329be1fadd64
local     elk_playground_certs
local     elk_playground_esdata01
local     elk_playground_filebeatdata01
local     elk_playground_kibanadata
local     elk_playground_logstashdata01
local     elk_playground_metricbeatdata01
local     elk_playground_postgresdata01
local     f4b39d5351762a8aaab102d7d07de8c76d7080f29453dcd4c1d205c055f2d6dc
local     todo-list

2_diamol/diamol/2_diamol on  main [!?] ❯ docker container run -d -p 8011:80 -v todo-list:/data --name todo-v2 diamol/ch06-todo-list:v2
Unable to find image 'diamol/ch06-todo-list:v2' locally
v2: Pulling from diamol/ch06-todo-list
68ced04f60ab: Already exists
e936bd534ffb: Already exists
caf64655bcbb: Already exists
d1927dbcbcab: Already exists
641667054481: Already exists
9d301c563cc9: Pull complete
92dc1ae7fce7: Pull complete
12c9a1dda02c: Pull complete
Digest: sha256:d2341450aaf2c48ed48e8607bd2271e5b89d38779487c746836d42ddafa5496c
Status: Downloaded newer image for diamol/ch06-todo-list:v2
a06ae374257d7dcf3b042af4bcd5353c1a3c7afb9d678a409a16829487b87f79

2_diamol/diamol/2_diamol on  main [!?] took 12s ❯ docker container inspect --format '{{.Mounts}}' todo-v2
[{volume todo-list /var/lib/docker/volumes/todo-list/_data /data local z true }]

2_diamol/diamol/2_diamol on  main [!?] ❯ history 20
 7714  2025-01-04 11:19:08 ll
 7715  2025-01-04 11:19:37 docker container run --name todo1 -d -p 8010:80 diamol/ch06-todo-list
 7716  2025-01-04 11:22:07 ping 8.8.8.8
 7717  2025-01-04 11:26:19 docker container run --name todo1 -d -p 8010:80 diamol/ch06-todo-list
 7718  2025-01-04 11:28:11 docker container inspect --format '{{.Mounts}}' todo1
 7719  2025-01-04 11:28:42 docker volume ls
 7720  2025-01-04 11:30:12 curl http://localhost:8010
 7721  2025-01-04 11:31:48 docker container run --name todo2 -d  diamol/ch06-todo-list
 7722  2025-01-04 11:31:53 docker ps
 7723  2025-01-04 11:32:09 docker container exec todo2 ls /data
 7724  2025-01-04 11:33:04 docker container run -d --name t3 --volumes-from todo1 diamol/ch06-todo-list
 7725  2025-01-04 11:33:18 docker container exec t3 ls /data
 7726  2025-01-04 11:36:15 docker container run -d -p 8011:80 -v todo-list:/data --name todo-v1 diamol/ch06-todo-list
 7727  2025-01-04 11:37:16 docker volume ls
 7728  2025-01-04 11:38:13 docker container inspect --format '{{.Mounts}}' todo-v1
 7729  2025-01-04 11:38:38 docker container rm -f todo-v1
 7730  2025-01-04 11:38:44 docker volume ls
 7731  2025-01-04 11:39:36 docker container run -d -p 8011:80 -v todo-list:/data --name todo-v2 diamol/ch06-todo-list:v2
 7732  2025-01-04 11:40:18 docker container inspect --format '{{.Mounts}}' todo-v2
 7733  2025-01-04 11:41:20 history 20

---

diamol/2_diamol/ch06 on  main [!?] ❯ docker container run --mount type=bind,source=$source,target=$target -d -p 8012:80 diamol/ch06-todo-list
3a06d00ce7c7e691568087c9d813996ed5cec4e0ebecc2f623134ff9dd331935

> 바인드 마운트는 양방향으로 동작한다. 컨테이니에서 만든 파일을 호스트 컴퓨터에서 수정할 수도 있고, 반대로 호스틍서 만든 파일도 컨테이너에서 수정할 수 있다.
> 호스트 컴퓨터에 대한 공격을 방지하기 위해 컨테이너는 대개 최소 권한을 가진 계정으로 실행되는데, 바인드 마운트를 사용하면 호스트 컴퓨터 파일에 접근하기 위해 권한상승이 필요하다.
> 그래서 Dockerfile 스크립트에서 USER 인스트럭션을 사용해 컨테이너에 관리자 권한을 부여한다.(리눅스는 root, 윈도는 ContainerAdministrator 계정으로 실행된다.
