#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
yum -y install mod_ssl
systemctl restart httpd
sed -i 's/^/#/g' /etc/httpd/conf.d/welcome.conf
echo '<html><body><h1>hit there </h1><body></html>' > /var/www/html/index.html
