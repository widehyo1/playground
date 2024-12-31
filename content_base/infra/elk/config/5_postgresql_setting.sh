CONF_DIR="/root/config"
SCRIPT_DIR="/var/lib/pgsql/scripts"
init_sql="init.sql"
dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
dnf -qy module disable postgresql
dnf install -y postgresql16-server
/usr/pgsql-16/bin/postgresql-16-setup initdb
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /var/lib/pgsql/16/data/postgresql.conf
cat "$CONF_DIR/pg_hba.conf" >> /var/lib/pgsql/16/data/pg_hba.conf
mkdir "$SCRIPT_DIR"
cp "$CONF_DIR/$init_sql" "$SCRIPT_DIR"
chown -R postgres:postgres "$SCRIPT_DIR"
systemctl enable postgresql-16
systemctl start postgresql-16
sudo -u postgres psql -c "ALTER USER postgres WITH password 'postgres';"
sudo -u postgres psql -a -f "$SCRIPT_DIR/$init_sql"
