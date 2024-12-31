home|Home directory of the Logstash installation.|/usr/share/logstash|-
bin|Binary scripts including logstash to start Logstash and logstash-plugin to install plugins|/usr/share/logstash/bin|-
settings|Configuration files, including logstash.yml, jvm.options, and startup.options|/etc/logstash|path.settings
conf|Logstash pipeline configuration files|/etc/logstash/conf.d/*.conf|See /etc/logstash/pipelines.yml
logs|Log files|/var/log/logstash|path.logs
plugins|Local, non Ruby-Gem plugin files. Each plugin is contained in a subdirectory. Recommended for development only.|/usr/share/logstash/plugins|path.plugins
data|Data files used by logstash and its plugins for any persistence needs.|/var/lib/logstash|path.data
