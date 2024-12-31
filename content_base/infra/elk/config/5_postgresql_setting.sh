CONF_DIR="/root/config"
dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
dnf -qy module disable postgresql
dnf install -y postgresql16-server
/usr/pgsql-16/bin/postgresql-16-setup initdb
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /var/lib/pgsql/16/data/postgresql.conf
cat "$CONF_DIR/pg_hba.conf" >> /var/lib/pgsql/16/data/pg_hba.conf
systemctl enable postgresql-16
systemctl start postgresql-16
sudo -u postgres psql -c "ALTER USER postgres WITH password 'postgres';"
