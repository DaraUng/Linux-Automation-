#!usr/bin/python
    
import os
    
os.system('yum -y install python-pip')
os.system('pip install virtualenv')
os.system('pip install --upgrade pip')
   
##mkdir and cd into
os.mkdir('/opt/django')
os.chdir('/opt/django/')
    
##running python
os.system('yum -y install python36')
os.system('virtualenv -p python36 django')  

os.system('source /opt/django/django/bin/activate && pip install django' + \
          '&& django-admin --version ' + \
          '&& django-admin startproject project1')
   
os.system('chown -R daraung65 /opt/django')
#os.system('chown -R daraung65 /opt/django/project1')
os.system('sudo -u daraung65  sh -c "source /opt/django/django/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&" ')
