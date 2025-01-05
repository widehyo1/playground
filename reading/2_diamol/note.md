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



 8208  2025-01-05 09:27:56 docker container run -e DOCKER_HOST=192.168.45.78 -d -p 9090:9090 diamol/prometheus:2.13.1
 8209  2025-01-05 09:28:14 ip route get 1
 8210  2025-01-05 09:28:23 docker rm -f 42f6d1b7ad4e
 8211  2025-01-05 09:28:29 docker rm -f db9175f02be1
 8212  2025-01-05 09:28:42 docker container run -e DOCKER_HOST=172.21.128.1 -d -p 9090:9090 diamol/prometheus:2.13.1
 8213  2025-01-05 09:35:18 docker container run -e DOCKER_HOST=172.21.139.255 -d -p 9090:9090 diamol/prometheus:2.13.1
 8214  2025-01-05 09:35:27 docker rm -f b689f90021c
 8215  2025-01-05 09:35:39 docker container run -e DOCKER_HOST=172.21.139.255 -d -p 9090:9090 diamol/prometheus:2.13.1
 8216  2025-01-05 09:35:49 docker ps
 8217  2025-01-05 09:35:56 docker rm -f 0b6542114
 8218  2025-01-05 09:35:59 docker container run -e DOCKER_HOST=172.21.139.255 -d -p 9090:9090 diamol/prometheus:2.13.1
 8219  2025-01-05 09:36:48 curl localhost:9323/metrics
 8220  2025-01-05 09:38:00 ip addr show docker0
 8221  2025-01-05 09:38:52 lsof
 8222  2025-01-05 09:39:02 lsof -Pi TCP -a -c dockerd
 8223  2025-01-05 09:39:11 sudo lsof -Pi TCP -a -c dockerd
 8224  2025-01-05 09:39:54 curl 172.21.139.255:9323/metrics
 8225  2025-01-05 09:40:09 docker ps
 8226  2025-01-05 09:40:15 docker rm -f 4a826963
 8227  2025-01-05 09:40:19 docker ps
 8228  2025-01-05 09:40:44 docker container run -e DOCKER_HOST=172.21.139.255:9323 -d -p 9090:9090 diamol/prometheus:2.13.1
 8229  2025-01-05 09:41:32 docker rm -f e3ce2f28a
 8230  2025-01-05 09:41:37 docker container run -e DOCKER_HOST=172.21.139.255 -d -p 9090:9090 diamol/prometheus:2.13.1
 8231  2025-01-05 09:44:04 cdr2
 8232  2025-01-05 09:44:05 ls
 8233  2025-01-05 09:44:07 cd diamol
 8234  2025-01-05 09:44:07 ls
 8235  2025-01-05 09:44:10 cd ch09
 8236  2025-01-05 09:44:11 ls
 8237  2025-01-05 09:44:18 cd exercises/
 8238  2025-01-05 09:44:19 ls
 8239  2025-01-05 09:44:24 docker ps
 8240  2025-01-05 09:44:30 docker rm -f b204ff4
 8241  2025-01-05 09:44:37 docker compose up -d
 8242  2025-01-05 09:45:35 curl 172.21.139.255:9323/metrics
 8243  2025-01-05 09:49:07 ls
 8244  2025-01-05 09:49:15 cdr2
 8245  2025-01-05 09:49:15 ls
 8246  2025-01-05 09:49:20 mkdir ch09
 8247  2025-01-05 09:49:33 history 40 >> note.md


```
playground/reading/2_diamol on  main [✘!?] ❯ sudo lsof -Pi TCP -a -c dockerd
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
dockerd 13020 root   17u  IPv6 139077      0t0  TCP *:9323 (LISTEN)


~ via 🌙 v5.4.7 ❯ sudo lsof -Pi TCP -a -c dockerd
[sudo] password for widehyo:
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
dockerd 4514 root   17u  IPv6 115765      0t0  TCP 172.21.139.255:9323->172.17.0.2:47958 (ESTABLISHED)
dockerd 4514 root   22u  IPv6  59635      0t0  TCP *:9323 (LISTEN)

playground/reading/2_diamol on  main [✘!?] ❯
exit


playground/reading/2_diamol on  main [✘!?] ❯ ^C

playground/reading/2_diamol on  main [✘!?] ❯ ip addr show docker0
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:af:cf:18:83 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:afff:fecf:1883/64 scope link
       valid_lft forever preferred_lft forever

playground/reading/2_diamol on  main [✘!?] ❯ curl 172.21.139.255:9323/metrics
# HELP builder_builds_failed_total Number of failed image builds
# TYPE builder_builds_failed_total counter
builder_builds_failed_total{reason="build_canceled"} 0
builder_builds_failed_total{reason="build_target_not_reachable_error"} 0
swarm_store_write_tx_latency_seconds_bucket{le="5"} 0
...
swarm_store_write_tx_latency_seconds_bucket{le="10"} 0
swarm_store_write_tx_latency_seconds_bucket{le="+Inf"} 0
swarm_store_write_tx_latency_seconds_sum 0
swarm_store_write_tx_latency_seconds_count 0


playground/reading/2_diamol on  main [✘!?] ❯ cat /etc/docker/daemon.json
{
  "metrics-addr": "0.0.0.0:9323"
}

 8029  2025-01-05 09:05:45 sudo systemctl daemon-reload
 8030  2025-01-05 09:05:52 sudo systemctl restart docker
```
for i in {1..100}; do curl http://localhost:8010 > /dev/null; done

sum(image_gallary_requests_total{code="500"}) without(instance)
