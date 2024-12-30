# hostnamectl set-hostname mygit
# echo "127.0.0.1 localhost mygit" >> /etc/hosts
# echo "::1 localhost mygit" >> /etc/hosts
echo "ServerName mygit" >> /etc/httpd/conf/httpd.conf
echo "LoadModule cgi_module modules/mod_cgi.so" >> /etc/httpd/conf.modules.d/00-base.conf
httpd -v
systemctl start httpd
systemctl enable httpd
ifconfig
cp /root/config/mygit.conf /etc/httpd/conf.d/mygit.conf
cp -r /root/mygit /var/www/mygit
chown -R git:git /var/www/mygit/index.html
apachectl configtest
systemctl restart httpd
