#!/usr/bin/python

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

import googleapiclient
import pprint
import json

credentials = GoogleCredentials.get_application_default()
compute = googleapiclient.discovery.build('compute','v1', credentials=credentials)

project = "intricate-abbey-217802"
zone = "us-east1-b"

name = "dara-proj"

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']


def create_instance(compute, project, zone, name):
    # Get the latest Debian Jessie image.

    # Configure the machine
    startup_script = open('Django/python_django.py', 'r').read()
    image_response = compute.images().getFromFamily(project='centos-cloud', family='centos-7').execute()
    
    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    
    #image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    #image_caption = "Ready for dessert?"

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
        
        #enable the https/http to run on the instance
        "labes":{
            "http-server":"",
            "https-server":""
        },
        "tags":{
           "items":[
               "http-server",
               "https-server"
           ]
        },
        
        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }]
         }
    }
    
    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()

#Finish created the instance


# Being to remove the instance file
def delete_instance(compute, project, zone, name):
    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=name).execute()
        
newinstance = create_instance(compute,project, zone, name)
instance = list_instances(compute, project, zone)

pprint.pprint(newinstance)
pprint.pprint(instance)
