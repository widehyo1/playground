CONF_DIR="/root/config"
if [ -f /etc/yum.repos.d/elasticsearch.repo ]
then
    echo "elasticsearch.repo exists"
else
    rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    cp "$CONF_DIR/elasticsearch.repo" /etc/yum.repos.d/elasticsearch.repo
    dnf install -y --enablerepo=elasticsearch elasticsearch
    cat "$CONF_DIR/limits.conf" >> /etc/security/limits.conf
    cat "$CONF_DIR/sysctl.conf" >> /etc/sysctl.conf
    cat "$CONF_DIR/elasticsearch.service" >> /usr/lib/systemd/system/elasticsearch.service
    systemctl daemon-reload
    systemctl enable elasticsearch.service
    systemctl restart elasticsearch.service
fi

curl -X GET localhost:9200
netstat -tnlp | grep 9200

echo "restarting..."

/usr/bin/cp -f "$CONF_DIR/elasticsearch.yml" /etc/elasticsearch/elasticsearch.yml
systemctl daemon-reload
systemctl enable elasticsearch.service
systemctl restart elasticsearch.service
curl -X GET localhost:9200
netstat -tnlp | grep 9200

if curl -X GET localhost:9200/_cat/indices?pretty | grep health
then
    echo "health index already exists"
    curl -X DELETE localhost:9200/health?pretty
fi
curl -X PUT -H "Content-Type: application/json" -d @"$CONF_DIR/health.json" localhost:9200/health?pretty
curl -X GET localhost:9200/_cat/indices?pretty
