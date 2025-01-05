CONF_DIR="/root/config"
IN_CONF_DIR="$CONF_DIR/logstash_config"
LOGSTASH_CONF_DIR="/usr/share/logstash/config"
if [ -f /etc/yum.repos.d/logstash.repo ]
then
    echo "logstash.repo exists"
else
    sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    cp "$CONF_DIR/logstash.repo" /etc/yum.repos.d/logstash.repo
    dnf install -y logstash
    cp "$CONF_DIR/postgresql-42.7.4.jar" /usr/share/logstash/logstash-core/lib/jars/postgresql-42.7.4.jar
fi
if [ -d $LOGSTASH_CONF_DIR ]
then
    /usr/bin/rm -rf "$LOGSTASH_CONF_DIR"
fi
/usr/bin/cp -rf "$IN_CONF_DIR" "$LOGSTASH_CONF_DIR"
cat "$LOGSTASH_CONF_DIR/conf.d/healthcheck.conf"
nohup /usr/share/logstash/bin/logstash &
until curl -s -X GET localhost:9200/health/_count?pretty | grep '"count" : 1'; do
    echo "waiting for health check to pass..."
    sleep 10
done
echo "health check for logstash passed"
