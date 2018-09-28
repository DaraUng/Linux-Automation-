yum -y install httpd
systemctl enable httpd
systemctl start httpd
yum -y install mod_ssl
systemctl restart httpd
