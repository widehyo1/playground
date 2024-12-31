CONF_DIR="/root/config"
if false # [ -f /etc/yum.repos.d/elasticsearch.repo ]
then
    echo "elasticsearch.repo exists"
else
    rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    cp "$CONF_DIR/elasticsearch.repo" /etc/yum.repos.d/elasticsearch.repo
    dnf install -y --enablerepo=elasticsearch elasticsearch
    sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/' /etc/elasticsearch/elasticsearch.yml
    sed -i 's/#discovery.seed_hosts: \["host1", "host2"\]/discovery.seed_hosts: ["0.0.0.0"]/' /etc/elasticsearch/elasticsearch.yml
    cat "$CONF_DIR/limits.conf" >> /etc/security/limits.conf
    cat "$CONF_DIR/sysctl.conf" >> /etc/sysctl.conf
    cat "$CONF_DIR/elasticsearch.service" >> /usr/lib/systemd/system/elasticsearch.service
    systemctl daemon-reload
    systemctl enable elasticsearch.service
    systemctl start elasticsearch.service
    curl -XGET localhost:9200
fi
