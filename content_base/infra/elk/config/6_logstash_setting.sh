CONF_DIR="/root/config"
if [ -f /etc/yum.repos.d/logstash.repo ]
then
    echo "logstash.repo exists"
else
    sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    cp "$CONF_DIR/logstash.repo" /etc/yum.repos.d/logstash.repo
    dnf install -y logstash
fi
