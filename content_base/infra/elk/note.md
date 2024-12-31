[How To Install and Use Docker on Rocky Linux 9 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-rocky-linux-9)

sudo dnf check-update
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl status docker
sudo systemctl enable docker
sudo usermod -aG docker vagrant

---

[Quick start | Elasticsearch Guide [7.17] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/getting-started.html)

docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.26
docker run --name es01-test --net elastic -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.26
docker pull docker.elastic.co/kibana/kibana:7.17.26
docker run --name kib01-test --net elastic -p 127.0.0.1:5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.17.26


---

[Installing Logstash | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/installing-logstash.html#package-repositories)

sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

/etc/yum.repos.d/logstash.repo
```
[logstash-7.x]
name=Elastic repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```
sudo yum install logstash



```log
hello world
{
       "message" => "hello world",
          "host" => "elk",
    "@timestamp" => 2024-12-31T08:23:24.272Z,
      "@version" => "1"
}
[INFO ] 2024-12-31 08:23:31.383 [[main]-pipeline-manager] javapipeline - Pipeline terminated {"pipeline.id"=>"main"}
[INFO ] 2024-12-31 08:23:31.410 [Converge PipelineAction::Delete<main>] pipelinesregistry - Removed pipeline from registry successfully {:pipeline_id=>:main}
[INFO ] 2024-12-31 08:23:31.433 [LogStash::Runner] runner - Logstash shut down.
```
[root@elk logstash]# history 2
   80  2024-12-31_08:21:49 bin/logstash -e 'input { stdin { } } output { stdout {} }'


---

[Install Elasticsearch with RPM | Elasticsearch Guide [7.17] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/rpm.html)

rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

/etc/yum.repos.d/elasticsearch.repo
```
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
```

sudo dnf install --enablerepo=elasticsearch elasticsearch



```bash
    8  2024-12-31_08:03:55 cat 4_elasticsearch_setting.sh 
    9  2024-12-31_08:04:03 sh 4_elasticsearch_setting.sh 
   10  2024-12-31_08:04:40 cat 4_elasticsearch_setting.sh 
   11  2024-12-31_08:04:45 sh 4_elasticsearch_setting.sh 
   12  2024-12-31_08:05:13 rm /etc/yum.repos.d/elasticsearch.repo
   13  2024-12-31_08:05:17 sh 4_elasticsearch_setting.sh 
   14  2024-12-31_08:06:02 ps -p 1
   15  2024-12-31_08:06:41 sudo /bin/systemctl daemon-reload
   16  2024-12-31_08:06:41 sudo /bin/systemctl enable elasticsearch.service
   17  2024-12-31_08:07:12 sudo systemctl start elasticsearch.service
   18  2024-12-31_08:07:45 docker ps
   19  2024-12-31_08:07:55 docker down 5a65d5d7bd40
   20  2024-12-31_08:08:06 docker shutdown 5a65d5d7bd40
   21  2024-12-31_08:08:10 docker help
   22  2024-12-31_08:08:17 docker stop 5a65d5d7bd40
   23  2024-12-31_08:08:25 systemctl status elasticsearch
   24  2024-12-31_08:08:37 ps -ef | grep 9200
   25  2024-12-31_08:08:51 journalctl --unit elasticsearch
   26  2024-12-31_08:09:27 curl -XGET localhost:9200
   27  2024-12-31_08:09:39 history 20
```


---

[Running Logstash on Docker | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/docker.html)

docker pull docker.elastic.co/logstash/logstash:7.17.26

---

[Configuring Logstash for Docker | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/docker-config.html)

docker run --rm -it -v ~/pipeline/:/usr/share/logstash/pipeline/ docker.elastic.co/logstash/logstash:7.17.26



docker run --rm -it -v ~/pipeline/:/usr/share/logstash/pipeline/ docker.elastic.co/logstash/logstash:7.17.26


docker run --rm -it -v ~/settings/:/usr/share/logstash/config/ docker.elastic.co/logstash/logstash:7.17.26

docker run --rm -it -v ~/settings/logstash.yml:/usr/share/logstash/config/logstash.yml docker.elastic.co/logstash/logstash:7.17.26

Dockerfile

FROM docker.elastic.co/logstash/logstash:7.17.26
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/


Table 1. Example Docker Environment Variables

Environment Variable | Logstash Setting

PIPELINE_WORKERS | pipeline.workers

LOG_LEVEL | log.level

MONITORING_ENABLED | monitoring.enabled

Docker defaults

http.host | 0.0.0.0

monitoring.elasticsearch.hosts | http://elasticsearch:9200

---

[Logstash Directory Layout | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/dir-layout.html)

Type	Description	Default Location	Setting
```bash
cat temp.txt | grep -v "^$" | paste -d "|" - - - - > docker_image_directory_layout.md

content_base/infra/elk on  main [?] via ⍱ v2.4.3 ❯ cat -n docker_image_directory_layout.md 

1	home|Home directory of the Logstash installation.|/usr/share/logstash|-
2	bin|Binary scripts, including logstash to start Logstash and logstash-plugin to install plugins|/usr/share/logstash/bin|-
3	settings|Configuration files, including logstash.yml and jvm.options|/usr/share/logstash/config|path.settings
4	conf|Logstash pipeline configuration files|/usr/share/logstash/pipeline|path.config
5	plugins|Local, non Ruby-Gem plugin files. Each plugin is contained in a subdirectory. Recommended for development only.|/usr/share/logstash/plugins|path.plugins
6	data|Data files used by logstash and its plugins for any persistence needs.|/usr/share/logstash/data|path.data

content_base/infra/elk on  main [?] via ⍱ v2.4.3 ❯ cat -n docker_image_directory_layout.md 

1	home|Home directory of the Logstash installation.|/usr/share/logstash|-
2	bin|Binary scripts, including logstash to start Logstash and logstash-plugin to install plugins|/usr/share/logstash/bin|-
3	settings|Configuration files, including logstash.yml and jvm.options|/usr/share/logstash/config|path.settings
4	conf|Logstash pipeline configuration files|/usr/share/logstash/pipeline|path.config
5	plugins|Local, non Ruby-Gem plugin files. Each plugin is contained in a subdirectory. Recommended for development only.|/usr/share/logstash/plugins|path.plugins
6	data|Data files used by logstash and its plugins for any persistence needs.|/usr/share/logstash/data|path.data
```

---

[logstash.yml | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/logstash-settings-file.html)

Setting	Description	Default value

node.name

A descriptive name for the node.

Machine’s hostname

path.data

The directory that Logstash and its plugins use for any persistent needs.

LOGSTASH_HOME/data

pipeline.id

The ID of the pipeline.

main

pipeline.java_execution

Use the Java execution engine.

true

pipeline.workers

The number of workers that will, in parallel, execute the filter and output stages of the pipeline. This setting uses the java.lang.Runtime.getRuntime.availableProcessors value as a default if not overridden by pipeline.workers in pipelines.yml or pipeline.workers from logstash.yml. If you have modified this setting and see that events are backing up, or that the CPU is not saturated, consider increasing this number to better utilize machine processing power.

Number of the host’s CPU cores

pipeline.batch.size

The maximum number of events an individual worker thread will collect from inputs before attempting to execute its filters and outputs. Larger batch sizes are generally more efficient, but come at the cost of increased memory overhead. You may need to increase JVM heap space in the jvm.options config file. See Logstash Configuration Files for more info.

125

pipeline.batch.delay

When creating pipeline event batches, how long in milliseconds to wait for each event before dispatching an undersized batch to pipeline workers.

50

pipeline.unsafe_shutdown

When set to true, forces Logstash to exit during shutdown even if there are still inflight events in memory. By default, Logstash will refuse to quit until all received events have been pushed to the outputs. Enabling this option can lead to data loss during shutdown.

false

pipeline.plugin_classloaders

(Beta) Load Java plugins in independent classloaders to isolate their dependencies.

false

pipeline.ordered

Set the pipeline event ordering.Valid options are:

auto
true
false
auto will automatically enable ordering if the pipeline.workers setting is also set to 1. true will enforce ordering on the pipeline and prevent logstash from starting if there are multiple workers. false will disable the processing required to preserve order. Ordering will not be guaranteed, but you save the processing cost of preserving order.

auto

pipeline.ecs_compatibility

Sets the pipeline’s default value for ecs_compatibility, a setting that is available to plugins that implement an ECS compatibility mode for use with the Elastic Common Schema. Possible values are:

disabled
v1
v8
This option allows the early opt-in (or preemptive opt-out) of ECS compatibility modes in plugins, which is scheduled to be on-by-default in a future major release of Logstash.

Values other than disabled are currently considered BETA, and may produce unintended consequences when upgrading Logstash.

disabled

path.config

The path to the Logstash config for the main pipeline. If you specify a directory or wildcard, config files are read from the directory in alphabetical order.

Platform-specific. See Logstash Directory Layout.

config.string

A string that contains the pipeline configuration to use for the main pipeline. Use the same syntax as the config file.

None

config.test_and_exit

When set to true, checks that the configuration is valid and then exits. Note that grok patterns are not checked for correctness with this setting. Logstash can read multiple config files from a directory. If you combine this setting with log.level: debug, Logstash will log the combined config file, annotating each config block with the source file it came from.

false

config.reload.automatic

When set to true, periodically checks if the configuration has changed and reloads the configuration whenever it is changed. This can also be triggered manually through the SIGHUP signal.

false

config.reload.interval

How often in seconds Logstash checks the config files for changes. Note that the unit qualifier (s) is required.

3s

config.debug

When set to true, shows the fully compiled configuration as a debug log message. You must also set log.level: debug. WARNING: The log message will include any password options passed to plugin configs as plaintext, and may result in plaintext passwords appearing in your logs!

false

config.support_escapes

When set to true, quoted strings will process the following escape sequences: \n becomes a literal newline (ASCII 10). \r becomes a literal carriage return (ASCII 13). \t becomes a literal tab (ASCII 9). \\ becomes a literal backslash \. \" becomes a literal double quotation mark. \' becomes a literal quotation mark.

false

modules

When configured, modules must be in the nested YAML structure described above this table.

None

queue.type

The internal queuing model to use for event buffering. Specify memory for legacy in-memory based queuing, or persisted for disk-based ACKed queueing (persistent queues).

memory

path.queue

The directory path where the data files will be stored when persistent queues are enabled (queue.type: persisted).

path.data/queue

queue.page_capacity

The size of the page data files used when persistent queues are enabled (queue.type: persisted). The queue data consists of append-only data files separated into pages.

64mb

queue.max_events

The maximum number of unread events in the queue when persistent queues are enabled (queue.type: persisted).

0 (unlimited)

queue.max_bytes

The total capacity of the queue (queue.type: persisted) in number of bytes. Make sure the capacity of your disk drive is greater than the value you specify here. If both queue.max_events and queue.max_bytes are specified, Logstash uses whichever criteria is reached first.

1024mb (1g)

queue.checkpoint.acks

The maximum number of ACKed events before forcing a checkpoint when persistent queues are enabled (queue.type: persisted). Specify queue.checkpoint.acks: 0 to set this value to unlimited.

1024

queue.checkpoint.writes

The maximum number of written events before forcing a checkpoint when persistent queues are enabled (queue.type: persisted). Specify queue.checkpoint.writes: 0 to set this value to unlimited.

1024

queue.checkpoint.retry

When enabled, Logstash will retry four times per attempted checkpoint write for any checkpoint writes that fail. Any subsequent errors are not retried. This is a workaround for failed checkpoint writes that have been seen only on Windows platform, filesystems with non-standard behavior such as SANs and is not recommended except in those specific circumstances. (queue.type: persisted)

true

queue.drain

When enabled, Logstash waits until the persistent queue (queue.type: persisted) is drained before shutting down.

false

dead_letter_queue.enable

Flag to instruct Logstash to enable the DLQ feature supported by plugins.

false

dead_letter_queue.max_bytes

The maximum size of each dead letter queue. Entries will be dropped if they would increase the size of the dead letter queue beyond this setting.

1024mb

path.dead_letter_queue

The directory path where the data files will be stored for the dead-letter queue.

path.data/dead_letter_queue

api.enabled

The HTTP API is enabled by default. It can be disabled, but features that rely on it will not work as intended.

true

api.environment

The API returns the provided string as a part of its response. Setting your environment may help to disambiguate between similarly-named nodes in production vs test environments.

production

api.http.host

The bind address for the HTTP API endpoint. By default, the Logstash HTTP API binds only to the local loopback interface. When configured securely (api.ssl.enabled: true and api.auth.type: basic), the HTTP API binds to all available interfaces.

"127.0.0.1"

api.http.port

The bind port for the HTTP API endpoint.

9600-9700

api.ssl.enabled

Set to true to enable SSL on the HTTP API. Doing so requires both api.ssl.keystore.path and api.ssl.keystore.password to be set.

false

api.ssl.keystore.path

The path to a valid JKS or PKCS12 keystore for use in securing the Logstash API. The keystore must be password-protected, and must contain a single certificate chain and a private key. This setting is ignored unless api.ssl.enabled is set to true.

N/A

api.ssl.keystore.password

The password to the keystore provided with api.ssl.keystore.path. This setting is ignored unless api.ssl.enabled is set to true.

N/A

api.auth.type

Set to basic to require HTTP Basic auth on the API using the credentials supplied with api.auth.basic.username and api.auth.basic.password.

none

api.auth.basic.username

The username to require for HTTP Basic auth Ignored unless api.auth.type is set to basic.

N/A

api.auth.basic.password

The password to require for HTTP Basic auth Ignored unless api.auth.type is set to basic.

N/A

log.level

The log level. Valid options are:

fatal
error
warn
info
debug
trace
info

log.format

The log format. Set to json to log in JSON format, or plain to use Object#.inspect.

plain

path.logs

The directory where Logstash will write its log to.

LOGSTASH_HOME/logs

pipeline.separate_logs

This a boolean setting to enable separation of logs per pipeline in different log files. If enabled Logstash will create a different log file for each pipeline, using the pipeline.id as name of the file. The destination directory is taken from the `path.log`s setting. When there are many pipelines configured in Logstash, separating each log lines per pipeline could be helpful in case you need to troubleshoot what’s happening in a single pipeline, without interference of the other ones.

false

path.plugins

Where to find custom plugins. You can specify this setting multiple times to include multiple paths. Plugins are expected to be in a specific directory hierarchy: PATH/logstash/TYPE/NAME.rb where TYPE is inputs, filters, outputs, or codecs, and NAME is the name of the plugin.

Platform-specific. See Logstash Directory Layout.

---

[Configuring Logstash | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/configuration.html)

logstash-simple.conf
```
input { stdin { } }
output {
  elasticsearch { hosts => ["localhost:9200"] }
  stdout { codec => rubydebug }
}
```

bin/logstash -f logstash-simple.conf


[Structure of a config file | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/configuration-file-structure.html)

```conf
# This is a comment. You should use comments to describe
# parts of your configuration.
input {
  ...
}

filter {
  ...
}

output {
  ...
}
```

```conf
input {
  file {
    path => "/var/log/messages"
    type => "syslog"
  }

  file {
    path => "/var/log/apache/access.log"
    type => "apache"
  }
}
```

---

[Accessing event data and fields in the configuration | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/event-dependent-configuration.html)

The logstash agent is a processing pipeline with 3 stages: inputs → filters → outputs. Inputs generate events, filters modify them, outputs ship them elsewhere.

All events have properties. For example, an apache access log would have things like status code (200, 404), request path ("/", "index.html"), HTTP verb (GET, POST), client IP address, etc. Logstash calls these properties "fields."

---

[Jdbc input plugin | Logstash Reference [7.17] | Elastic](https://www.elastic.co/guide/en/logstash/7.17/plugins-inputs-jdbc.html)

```
input {
  jdbc {
    jdbc_driver_library => "mysql-connector-java-5.1.36-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydb"
    jdbc_user => "mysql"
    parameters => { "favorite_artist" => "Beethoven" }
    schedule => "* * * * *"
    statement => "SELECT * from songs where artist = :favorite_artist"
  }
}
```

```
input {
  jdbc {
    statement => "SELECT * FROM mgd.seq_sequence WHERE _sequence_key > ? AND _sequence_key < ? + ? ORDER BY _sequence_key ASC"
    prepared_statement_bind_values => [":sql_last_value", ":sql_last_value", 4]
    prepared_statement_name => "foobar"
    use_prepared_statements => true
    use_column_value => true
    tracking_column_type => "numeric"
    tracking_column => "_sequence_key"
    last_run_metadata_path => "/elastic/tmp/testing/confs/test-jdbc-int-sql_last_value.yml"
    # ... other configuration bits
  }
}
```

---
[PostgreSQL: Linux downloads (Red Hat family)](https://www.postgresql.org/download/linux/redhat/)

sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo dnf -qy module disable postgresql
sudo dnf install -y postgresql16-server
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
sudo systemctl enable postgresql-16
sudo systemctl start postgresql-16


---


[vagrant@elk ~]$ ps -ef | grep postgres
postgres   40758       1  0 07:37 ?        00:00:00 /usr/pgsql-16/bin/postgres -D /var/lib/pgsql/16/data/
postgres   40759   40758  0 07:37 ?        00:00:00 postgres: logger 
postgres   40760   40758  0 07:37 ?        00:00:00 postgres: checkpointer 
postgres   40761   40758  0 07:37 ?        00:00:00 postgres: background writer 
postgres   40763   40758  0 07:37 ?        00:00:00 postgres: walwriter 
postgres   40764   40758  0 07:37 ?        00:00:00 postgres: autovacuum launcher 
postgres   40765   40758  0 07:37 ?        00:00:00 postgres: logical replication launcher 
vagrant    40767   39842  0 07:38 pts/0    00:00:00 grep --color=auto postgres
[vagrant@elk ~]$ psql
psql: error: connection to server on socket "/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "vagrant" does not exist
[vagrant@elk ~]$ sudo su -
[root@elk ~]# su - postgres
[postgres@elk ~]$ pwd
/var/lib/pgsql
[postgres@elk ~]$ psql
psql (16.6)
Type "help" for help.

postgres=# exit
[postgres@elk ~]$ 


---

host에서 vagrant의 postgresql DB에 연결할 수 있어야 할 것
host에서 vagrant의 elasticsearch에 curl을 날릴수 있어야 함
vagrant의 logstash가 jdbc plugin을 통해 같은 machine의 postgresql에 붙을 수 있어야 함.

index 생성
db 생성
logstash 기동
elasticsearch 인덱스 확인

+ alpha
kibana 설치 및 host에서 vagrant의 kibana에 접속하여 쿼리 동작 확인

+ alpha alpah
vagrant에 elk python backend 기동
<- 이건 강의 주제에 벗어남, 안할 것임


---

[[elasticsearch]bootstrap check failure](https://darksharavim.tistory.com/780)

```
[darksharavim.tistory.com]ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 30793
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 30793
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

```
[darksharavim.tistory.com]vi /etc/security/limits.conf
# 아래내용 추가
*       soft    nofile  65536
*       hard    nofile  65536
*       soft    memlock unlimited
*       hard    memlock unlimited
```

```
[darksharavim.tistory.com]ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 30793
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 65536
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 30793
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

```
[darksharavim.tistory.com]vi /etc/sysctl.conf
# 아래내용추가
fs.file-max = 6815744
vm.max_map_count = 262144

[darksharavim.tistory.com]sysctl -p
fs.file-max = 6815744
vm.max_map_count = 262144
```

```

[darksharavim.tistory.com]vi /usr/lib/systemd/system/elasticsearch.service
# [service]라인 하위에 아래내용추가
LimitMEMLOCK=infinity
```

```
[darksharavim.tistory.com]systemctl daemon-reload

[darksharavim.tistory.com]systemctl start elasticsearch

[darksharavim.tistory.com]systemctl status elasticsearch
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2022-06-17 11:31:59 KST; 11min ago
     Docs: https://www.elastic.co
 Main PID: 3964 (java)
    Tasks: 61 (limit: 100878)
   Memory: 8.4G
   CGroup: /system.slice/elasticsearch.service
           ├─3964 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networka>
           └─4256 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller

 6월 17 11:31:50 localhost.localdomain systemd[1]: Starting Elasticsearch...
 6월 17 11:31:59 localhost.localdomain systemd[1]: Started Elasticsearch.
 
```

```
[darksharavim.tistory.com]systemctl show | grep Limit
DefaultStartLimitIntervalUSec=10s
DefaultStartLimitBurst=5
DefaultLimitCPU=infinity
DefaultLimitCPUSoft=infinity
DefaultLimitFSIZE=infinity
DefaultLimitFSIZESoft=infinity
DefaultLimitDATA=infinity
DefaultLimitDATASoft=infinity
DefaultLimitSTACK=infinity
DefaultLimitSTACKSoft=8388608
DefaultLimitCORE=infinity
DefaultLimitCORESoft=0
DefaultLimitRSS=infinity
DefaultLimitRSSSoft=infinity
DefaultLimitNOFILE=262144
DefaultLimitNOFILESoft=1024
DefaultLimitAS=infinity
DefaultLimitASSoft=infinity
DefaultLimitNPROC=63049
DefaultLimitNPROCSoft=63049
DefaultLimitMEMLOCK=65536
DefaultLimitMEMLOCKSoft=65536
DefaultLimitLOCKS=infinity
DefaultLimitLOCKSSoft=infinity
DefaultLimitSIGPENDING=63049
DefaultLimitSIGPENDINGSoft=63049
DefaultLimitMSGQUEUE=819200
DefaultLimitMSGQUEUESoft=819200
DefaultLimitNICE=0
DefaultLimitNICESoft=0
DefaultLimitRTPRIO=0
DefaultLimitRTPRIOSoft=0
DefaultLimitRTTIME=infinity
DefaultLimitRTTIMESoft=infinity
```

---


[2024-12-31T09:47:03,302][ERROR][o.e.b.Bootstrap          ] [elk] node validation exception
[1] bootstrap checks failed. You must address the points described in the following [1] lines before starting Elasticsearch.
bootstrap check failure [1] of [1]: the default discovery settings are unsuitable for production use; at least one of [discovery.seed_hosts, discovery.seed_providers, cluster.initial_master_nodes] must be configured


at least one of [discovery.seed_hosts, discovery.seed_providers, cluster.initial_master_nodes] must be configured


중요!!!

```
sudo tail -n 50 /var/log/elasticsearch/elasticsearch.log
```

resolve it!


```json
infra/elk/config on  main [?] ❯ curl -XGET localhost:19200
{
  "name" : "elk",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "ktyLSEF7T2isrx8CaVEWeA",
  "version" : {
    "number" : "7.17.26",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "f40328375bfa289242f942fb3d992032ab662e14",
    "build_date" : "2024-11-28T08:05:55.550508263Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.3",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

---


[root@elk config]# netstat -tnpl | grep 5432
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      40058/postgres      
tcp6       0      0 ::1:5432                :::*                    LISTEN      40058/postgres      


[root@elk config]# su - postgres
[postgres@elk ~]$ psql -c "SHOW data_directory;"
     data_directory     
------------------------
 /var/lib/pgsql/16/data
(1 row)
[postgres@elk ~]$ ls /var/lib/pgsql/16/data
base              pg_hba.conf    pg_serial     pg_twophase           postmaster.opts
current_logfiles  pg_ident.conf  pg_snapshots  PG_VERSION            postmaster.pid
global            pg_logical     pg_stat       pg_wal
log               pg_multixact   pg_stat_tmp   pg_xact
pg_commit_ts      pg_notify      pg_subtrans   postgresql.auto.conf
pg_dynshmem       pg_replslot    pg_tblspc     postgresql.conf



[root@elk config]# sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /var/lib/pgsql/16/data/postgresql.conf
[root@elk config]# systemctl restart postgresql-16
[root@elk config]# netstat -tnlp | grep 5432
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      46907/postgres      
tcp6       0      0 :::5432                 :::*                    LISTEN      46907/postgres      

---

[Important Elasticsearch configuration | Elasticsearch Guide [7.17] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/important-settings.html)


[2024-12-31T11:46:29,400][WARN ][o.e.c.c.ClusterFormationFailureHelper] [elk] master not discovered yet, this node has not previously joined a bootstrapped (v7+) cluster, and this node must discover master-eligible nodes [node-1, node-2] to bootstrap a cluster: have discovered [{elk}{PhxRK046RQqUeXQP1su77w}{DUL9MKRjTQSoJYRftB2mHg}{10.0.2.15}{10.0.2.15:9300}{cdfhilmrstw}]; discovery will continue using [0.0.0.0:9300] from hosts providers and [{elk}{PhxRK046RQqUeXQP1su77w}{DUL9MKRjTQSoJYRftB2mHg}{10.0.2.15}{10.0.2.15:9300}{cdfhilmrstw}] from last-known cluster state; node term 0, last-accepted version 0 in term 0



sed -i 's/#cluster.name: my-application/cluster.name: elk-playground/' /etc/elasticsearch/elasticsearch.yml
sed -i 's/#node.name: node-1/node.name: node-1/' /etc/elasticsearch/elasticsearch.yml

---


[root@elk bin]# /usr/share/logstash/jdk/bin/java --version
openjdk 11.0.24 2024-07-16
OpenJDK Runtime Environment Temurin-11.0.24+8 (build 11.0.24+8)
OpenJDK 64-Bit Server VM Temurin-11.0.24+8 (build 11.0.24+8, mixed mode)
[root@elk bin]# /usr/share/elasticsearch/jdk/bin/java --version
openjdk 22.0.2 2024-07-16
OpenJDK Runtime Environment (build 22.0.2+9-70)
OpenJDK 64-Bit Server VM (build 22.0.2+9-70, mixed mode, sharing)

---

[Download | pgJDBC](https://jdbc.postgresql.org/download/)
wget https://jdbc.postgresql.org/download/postgresql-42.7.4.jar


---

/usr/share/logstash/logstash-core/lib/jars/postgresql-42.7.4.jar
org.postgresql.Driver

input {
  jdbc {
    jdbc_driver_library => "mysql-connector-java-5.1.36-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:postgresql://localhost:5432/postgres"
    jdbc_user => "mysql"
    schedule => "* * * * *"
    statement => "SELECT * from songs where artist = :favorite_artist"
  }
}


input {
  jdbc {
    jdbc_driver_library => "/usr/share/logstash/logstash-core/lib/jars/postgresql-42.7.4.jar"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_connection_string => "jdbc:postgresql://localhost:5432/postgres"
    jdbc_user => "postgresql"
    jdbc_password => "postgresql"
    schedule => "*/1 * * * *"
    statement => "SELECT * from pg_am;"
  }
}

filter {

}

output {
    stdout {
        codec => rubydebug
    }
}



```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)

postgres=# \dt
Did not find any relations.
postgres=# \dS
                        List of relations
   Schema   |              Name               | Type  |  Owner   
------------+---------------------------------+-------+----------
 pg_catalog | pg_aggregate                    | table | postgres
 pg_catalog | pg_am                           | table | postgres
postgres=# select count(1) from pg_am;
 count 
-------
     7
(1 row)

postgres=# select * from pg_am;
 oid  | amname |      amhandler       | amtype 
------+--------+----------------------+--------
    2 | heap   | heap_tableam_handler | t
  403 | btree  | bthandler            | i
  405 | hash   | hashhandler          | i
  783 | gist   | gisthandler          | i
 2742 | gin    | ginhandler           | i
 4000 | spgist | spghandler           | i
 3580 | brin   | brinhandler          | i
(7 rows)

```


---

[root@elk logstash]# find /etc/logstash/
/etc/logstash/
/etc/logstash/conf.d
/etc/logstash/jvm.options
/etc/logstash/log4j2.properties
/etc/logstash/logstash-sample.conf
/etc/logstash/logstash.yml
/etc/logstash/pipelines.yml
/etc/logstash/startup.options



[root@elk logstash]# grep -v "^#" logstash.yml 
path.data: /var/lib/logstash



path.logs: /var/log/logstash

[root@elk logstash]# cat pipelines.yml 
# This file is where you define your pipelines. You can define multiple.
# For more information on multiple pipelines, see the documentation:
#   https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html

- pipeline.id: main
  path.config: "/etc/logstash/conf.d/*.conf"

---


[root@elk logstash]# grep -v "^#" startup.options 


LS_HOME=/usr/share/logstash

LS_SETTINGS_DIR=/etc/logstash

LS_OPTS="--path.settings ${LS_SETTINGS_DIR}"

LS_JAVA_OPTS=""

LS_PIDFILE=/var/run/logstash.pid

LS_USER=logstash
LS_GROUP=logstash

LS_GC_LOG_FILE=/var/log/logstash/gc.log

LS_OPEN_FILES=16384

LS_NICE=19

SERVICE_NAME="logstash"
SERVICE_DESCRIPTION="logstash"



---


[root@elk logstash]# /usr/share/logstash/bin/logstash
Using bundled JDK: /usr/share/logstash/jdk
OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
WARNING: Could not find logstash.yml which is typically located in $LS_HOME/config or /etc/logstash. You can specify the path using --path.settings. Continuing using the defaults
Could not find log4j2 configuration at path /usr/share/logstash/config/log4j2.properties. Using default config which logs errors to the console
[INFO ] 2024-12-31 14:27:06.587 [main] runner - Starting Logstash {"logstash.version"=>"7.17.26", "jruby.version"=>"jruby 9.2.20.1 (2.5.8) 2021-11-30 2a2962fbd1 OpenJDK 64-Bit Server VM 11.0.24+8 on 11.0.24+8 +indy +jit [linux-x86_64]"}
[INFO ] 2024-12-31 14:27:06.591 [main] runner - JVM bootstrap flags: [-Xms1g, -Xmx1g, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djdk.io.File.enableADS=true, -Djruby.compile.invokedynamic=true, -Djruby.jit.threshold=0, -Djruby.regexp.interruptible=true, -XX:+HeapDumpOnOutOfMemoryError, -Djava.security.egd=file:/dev/urandom, -Dlog4j2.isThreadContextMapInheritable=true]
ERROR: Failed to read pipelines yaml file. Location: /usr/share/logstash/config/pipelines.yml
usage:
  bin/logstash -f CONFIG_PATH [-t] [-r] [] [-w COUNT] [-l LOG]
  bin/logstash --modules MODULE_NAME [-M "MODULE_NAME.var.PLUGIN_TYPE.PLUGIN_NAME.VARIABLE_NAME=VALUE"] [-t] [-w COUNT] [-l LOG]
  bin/logstash -e CONFIG_STR [-t] [--log.level fatal|error|warn|info|debug|trace] [-w COUNT] [-l LOG]
  bin/logstash -i SHELL [--log.level fatal|error|warn|info|debug|trace]
  bin/logstash -V [--log.level fatal|error|warn|info|debug|trace]
  bin/logstash --help
[FATAL] 2024-12-31 14:27:06.895 [LogStash::Runner] Logstash - Logstash stopped processing because of an error: (SystemExit) exit
org.jruby.exceptions.SystemExit: (SystemExit) exit
	at org.jruby.RubyKernel.exit(org/jruby/RubyKernel.java:747) ~[jruby-complete-9.2.20.1.jar:?]
	at org.jruby.RubyKernel.exit(org/jruby/RubyKernel.java:710) ~[jruby-complete-9.2.20.1.jar:?]
	at usr.share.logstash.lib.bootstrap.environment.<main>(/usr/share/logstash/lib/bootstrap/environment.rb:94) ~[?:?]

---

[root@elk bin]# ./logstash --help
Using bundled JDK: /usr/share/logstash/jdk
OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.

WARNING: Could not find logstash.yml which is typically located in $LS_HOME/config or /etc/logstash. You can specify the path using --path.settings. Continuing using the defaults
Usage:
    bin/logstash [OPTIONS]

Options:
    -n, --node.name NAME          Specify the name of this logstash instance, if no value is given
                                  it will default to the current hostname.
                                   (default: "elk")
    --enable-local-plugin-development Allow Gemfile to be manipulated directly
                                  to facilitate simpler local plugin
                                  development.
                                  This is an advanced setting, intended
                                  only for use by Logstash developers,
                                  and should not be used in production.
                                   (default: false)
    -f, --path.config CONFIG_PATH Load the logstash config from a specific file
                                  or directory.  If a directory is given, all
                                  files in that directory will be concatenated
                                  in lexicographical order and then parsed as a
                                  single config file. You can also specify
                                  wildcards (globs) and any matched files will
                                  be loaded in the order described above.
    -e, --config.string CONFIG_STRING Use the given string as the configuration
                                  data. Same syntax as the config file. If no
                                  input is specified, then the following is
                                  used as the default input:
                                  "input { stdin { type => stdin } }"
                                  and if no output is specified, then the
                                  following is used as the default output:
                                  "output { stdout { codec => rubydebug } }"
                                  If you wish to use both defaults, please use
                                  the empty string for the '-e' flag.
                                   (default: nil)
    --field-reference-parser MODE (DEPRECATED) This option is no longer
                                  configurable.
                                  
                                  Use the given MODE when parsing field
                                  references.
                                  
                                  The field reference parser is used to expand
                                  field references in your pipeline configs,
                                  and has become more strict to better handle
                                  ambiguous- and illegal-syntax inputs.
                                  
                                  The only available MODE is:
                                   - `STRICT`: parse in a strict manner; when
                                     given ambiguous- or illegal-syntax input,
                                     raises a runtime exception that should
                                     be handled by the calling plugin.
                                  
                                   (default: "STRICT")
    --modules MODULES             Load Logstash modules.
                                  Modules can be defined using multiple instances
                                  '--modules module1 --modules module2',
                                     or comma-separated syntax
                                  '--modules=module1,module2'
                                  Cannot be used in conjunction with '-e' or '-f'
                                  Use of '--modules' will override modules declared
                                  in the 'logstash.yml' file.
    -M, --modules.variable MODULES_VARIABLE Load variables for module template.
                                  Multiple instances of '-M' or
                                  '--modules.variable' are supported.
                                  Ignored if '--modules' flag is not used.
                                  Should be in the format of
                                  '-M "MODULE_NAME.var.PLUGIN_TYPE.PLUGIN_NAME.VARIABLE_NAME=VALUE"'
                                  as in
                                  '-M "example.var.filter.mutate.fieldname=fieldvalue"'
    --setup                       Load index template into Elasticsearch, and saved searches, 
                                  index-pattern, visualizations, and dashboards into Kibana when
                                  running modules.
                                   (default: false)
    --cloud.id CLOUD_ID           Sets the elasticsearch and kibana host settings for
                                  module connections in Elastic Cloud.
                                  Your Elastic Cloud User interface or the Cloud support
                                  team should provide this.
                                  Add an optional label prefix '<label>:' to help you
                                  identify multiple cloud.ids.
                                  e.g. 'staging:dXMtZWFzdC0xLmF3cy5mb3VuZC5pbyRub3RhcmVhbCRpZGVudGlmaWVy'
    --cloud.auth CLOUD_AUTH       Sets the elasticsearch and kibana username and password
                                  for module connections in Elastic Cloud
                                  e.g. 'username:<password>'
    --pipeline.id ID              Sets the ID of the pipeline.
                                   (default: "main")
    -w, --pipeline.workers COUNT  Sets the number of pipeline workers to run.
                                   (default: 2)
    --pipeline.ordered ORDERED    Preserve events order. Possible values are `auto` (default), `true` and `false`.
                                  This setting
                                  will only work when also using a single worker for the pipeline.
                                  Note that when enabled, it may impact the performance of the filters
                                  and ouput processing.
                                  The `auto` option will automatically enable ordering if the
                                  `pipeline.workers` setting is set to `1`.
                                  Use `true` to enable ordering on the pipeline and prevent logstash
                                  from starting if there are multiple workers.
                                  Use `false` to disable any extra processing necessary for preserving
                                  ordering.
                                   (default: "auto")
    --java-execution              Use Java execution engine.
                                   (default: true)
    --plugin-classloaders         (Beta) Load Java plugins in independent classloaders to isolate their dependencies.
                                   (default: false)
    -b, --pipeline.batch.size SIZE Size of batches the pipeline is to work in.
                                   (default: 125)
    -u, --pipeline.batch.delay DELAY_IN_MS When creating pipeline batches, how long to wait while polling
                                  for the next event.
                                   (default: 50)
    --pipeline.unsafe_shutdown    Force logstash to exit during shutdown even
                                  if there are still inflight events in memory.
                                  By default, logstash will refuse to quit until all
                                  received events have been pushed to the outputs.
                                   (default: false)
    --pipeline.ecs_compatibility STRING Sets the pipeline's default value for `ecs_compatibility`,
                                  a setting that is available to plugins that implement
                                  an ECS Compatibility mode for use with the Elastic Common
                                  Schema.
                                  Possible values are:
                                   - disabled (default)
                                   - v1
                                   - v2
                                  This option allows the early opt-in (or preemptive opt-out)
                                  of ECS Compatibility modes in plugins, which is scheduled to
                                  be on-by-default in a future major release of Logstash.
                                  
                                  Values other than `disabled` are currently considered BETA,
                                  and may produce unintended consequences when upgrading Logstash.
                                   (default: "disabled")
    --path.data PATH              This should point to a writable directory. Logstash
                                  will use this directory whenever it needs to store
                                  data. Plugins will also have access to this path.
                                   (default: "/usr/share/logstash/data")
    -p, --path.plugins PATH       A path of where to find plugins. This flag
                                  can be given multiple times to include
                                  multiple paths. Plugins are expected to be
                                  in a specific directory hierarchy:
                                  'PATH/logstash/TYPE/NAME.rb' where TYPE is
                                  'inputs' 'filters', 'outputs' or 'codecs'
                                  and NAME is the name of the plugin.
                                   (default: [])
    -l, --path.logs PATH          Write logstash internal logs to the given
                                  file. Without this flag, logstash will emit
                                  logs to standard output.
                                   (default: "/usr/share/logstash/logs")
    --log.level LEVEL             Set the log level for logstash. Possible values are:
                                    - fatal
                                    - error
                                    - warn
                                    - info
                                    - debug
                                    - trace
                                   (default: "info")
    --config.debug                Print the compiled config ruby code out as a debug log (you must also have --log.level=debug enabled).
                                  WARNING: This will include any 'password' options passed to plugin configs as plaintext, and may result
                                  in plaintext passwords appearing in your logs!
                                   (default: false)
    -i, --interactive SHELL       Drop to shell instead of running as normal.
                                  Valid shells are "irb" and "pry"
    -V, --version                 Emit the version of logstash and its friends,
                                  then exit.
    -t, --config.test_and_exit    Check configuration for valid syntax and then exit.
                                   (default: false)
    -r, --config.reload.automatic Monitor configuration changes and reload
                                  whenever it is changed.
                                  NOTE: use SIGHUP to manually reload the config
                                   (default: false)
    --config.reload.interval RELOAD_INTERVAL How frequently to poll the configuration location
                                  for changes, in seconds.
                                   (default: #<Java::OrgLogstashUtil::TimeValue:0x24ecc9fc>)
    --api.enabled ENABLED         Can be used to disable the Web API, which is
                                  enabled by default.
                                   (default: true)
    --api.http.host HTTP_HOST     Web API binding host (default: "127.0.0.1")
    --api.http.port HTTP_PORT     Web API http port (default: 9600..9700)
    --log.format FORMAT           Specify if Logstash should write its own logs in JSON form (one
                                  event per line) or in plain text (using Ruby's Object#inspect)
                                   (default: "plain")
    --path.settings SETTINGS_DIR  Directory containing logstash.yml file. This can also be
                                  set through the LS_SETTINGS_DIR environment variable.
                                   (default: "/usr/share/logstash/config")
    --verbose                     Set the log level to info.
                                  DEPRECATED: use --log.level=info instead.
    --debug                       Set the log level to debug.
                                  DEPRECATED: use --log.level=debug instead.
    --quiet                       Set the log level to info.
                                  DEPRECATED: use --log.level=info instead.
    --http.enabled                Can be used to disable the Web API, which is
                                  enabled by default.
                                  DEPRECATED: use `--api.enabled=false`
    --http.host HTTP_HOST         Web API binding host
                                  DEPRECATED: use `--api.http.host=IP`
    --http.port HTTP_PORT         Web API http port
                                  DEPRECATED: use `--api.http.port=PORT`
    -h, --help                    print help

---


```log
[2024-12-31T14:47:01,353][INFO ][logstash.inputs.jdbc     ][healthcheck][c216f07b66a38fcb329cf7dfe888c4af778a8ac01ca183f70b31ef376c9a2873] (0.010406s) SELECT * from pg_am;
[2024-12-31T14:47:01,395][WARN ][logstash.inputs.jdbc     ][healthcheck][c216f07b66a38fcb329cf7dfe888c4af778a8ac01ca183f70b31ef376c9a2873] Exception when executing JDBC query {:exception=>Sequel::DatabaseError, :message=>"Java::OrgLogstash::MissingConverterException: Missing Converter handling for full class name=org.postgresql.util.PGobject, simple name=PGobject", :cause=>"org.logstash.MissingConverterException: Missing Converter handling for full class name=org.postgresql.util.PGobject, simple name=PGobject"}
```

---


postgres=# \d employees
                                           Table "public.employees"
   Column    |          Type          | Collation | Nullable |                    Default     
                
-------------+------------------------+-----------+----------+--------------------------------
----------------
 employee_id | integer                |           | not null | nextval('employees_employee_id_
seq'::regclass)
 first_name  | character varying(50)  |           | not null | 
 last_name   | character varying(50)  |           | not null | 
 email       | character varying(100) |           |          | 
 hire_date   | date                   |           | not null | 
 salary      | numeric(10,2)          |           |          | 
Indexes:
    "employees_pkey" PRIMARY KEY, btree (employee_id)
    "employees_email_key" UNIQUE CONSTRAINT, btree (email)



postgres=# \dt
           List of relations
 Schema |   Name    | Type  |  Owner   
--------+-----------+-------+----------
 public | employees | table | postgres
(1 row)

postgres=# select * from employees;
 employee_id | first_name | last_name | email | hire_date | salary 
-------------+------------+-----------+-------+-----------+--------
(0 rows)

postgres=# insert into employees(first_name, last_name, hire_date) values('health', 'test', now());
INSERT 0 1
postgres=# select * from employees;
 employee_id | first_name | last_name | email | hire_date  | salary 
-------------+------------+-----------+-------+------------+--------
           1 | health     | test      |       | 2024-12-31 |       
(1 row)




CREATE TABLE health (
    id SERIAL PRIMARY KEY,
    first VARCHAR(50),
    second VARCHAR(50)
);

INSERT INTO health(first, second) VALUES('health', 'test');

---


content_base/infra/elk on  main [!?] via ⍱ v2.4.3 ❯ curl -X GET localhost:19200/health/_count{"count":1,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0}}content_base/infra/elk on  main [!?] via ⍱ v2.4.3 ❯ 
content_base/infra/elk on  main [!?] via ⍱ v2.4.3 ❯ curl -X GET localhost:19200/health/_search
{"took":1,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":1,"relation":"eq"},"max_score":1.0,"hits":[{"_index":"health","_type":"_doc","_id":"1","_score":1.0,"_source":{"second":"test","@version":"1","@timestamp":"2024-12-31T15:49:01.082Z","id":1,"first":"health"}}]}}content_base/infra/elk on  main [!?] via ⍱ v2.4.3 ❯ h?prettyGET localhost:19200/health/_search
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "health",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "second" : "test",
          "@version" : "1",
          "@timestamp" : "2024-12-31T15:50:00.721Z",
          "id" : 1,
          "first" : "health"
        }
      }
    ]
  }
}

---

elasticsearch를 out of box(host)에서 접근할 수 있게 하려면 초기 설치후 첫 기동에서는 불가능하다(이유는 파악 안됨)
다만, 첫 기동 후 /etc/elasticsearch/elasticsearch.yml을 원하는 방식대로 바꾸면 그때는 제대로 동작한다.
이거 알아내는데 엄청난 시간이 걸렸다.(restarting이 있는 이유)
