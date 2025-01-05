[Install Elasticsearch with Docker | Elasticsearch Guide [7.17] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docker.html)

> docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.26
> docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.26
> sysctl -w vm.max_map_count=262144

```bash
infra/elk/docker on  main [✘!?] ❯ grep -v "^#" !$
grep -v "^#" /etc/sysctl.conf












infra/elk/docker on  main [✘!?] ❯ sysctl -w vm.max_map_count=262144
sysctl: permission denied on key "vm.max_map_count", ignoring

infra/elk/docker on  main [✘!?] ❯ sudo sysctl -w vm.max_map_count=262144
[sudo] password for widehyo:
vm.max_map_count = 262144

infra/elk/docker on  main [✘!?] took 2s ❯ !grep
grep -v "^#" /etc/sysctl.conf
```

> mkdir esdatadir
> chmod g+rwx esdatadir
> chgrp 0 esdatadir

mkdir esdatadir
chmod g+rwx esdatadir
chgrp 0 esdatadir

```bash
mkdir esdatadir
chmod g+rwx esdatadir
sudo chgrp 0 esdatadir
```

> docker run --rm docker.elastic.co/elasticsearch/elasticsearch:{version} /bin/bash -c 'ulimit -Hn && ulimit -Sn && ulimit -Hu && ulimit -Su'
> --ulimit nofile=65535:65535
> -e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1


---

[elasticsearch:7.17.26 - docker hub](https://hub.docker.com/layers/library/elasticsearch/7.17.26/images/sha256-b897cf79fc18c3e01e45ed9005e5d110295498f46c1caac56ac81997dd2bebeb)
[logstash:7.17.26 - docker hub](https://hub.docker.com/layers/library/logstash/7.17.26/images/sha256-3f0fd65748174a8cbcb12187c9e9f641084ac986715f10108464fdc6aec77f6a)
[kibana:7.17.26 - docker hub](https://hub.docker.com/layers/library/kibana/7.17.26/images/sha256-8bd133f1822584d4ebd4cbaceda8855f89f4bd78426d9164b7372a1bf6c5be2a)


docker pull logstash:7.17.26
docker pull elasticsearch:7.17.26
docker pull kibana:7.17.26
