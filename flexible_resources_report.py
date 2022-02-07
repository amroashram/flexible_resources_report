import logging
import os

import requests
import json 

_logger = logging.getLogger(__name__)

if os.environ.get('FLEXIBLESDK_DEBUG'):
    ch = logging.StreamHandler()
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(ch)
    _requests_log_level = logging.DEBUG
else:
    _requests_log_level = logging.WARNING

logging.getLogger("requests").setLevel(_requests_log_level)

class FlexibleConnection(object):

    def __init__(self, token=None , project_id=None , region=None , tenant_id=None):
                
        self.token = os.environ.get('token')
        self.project_id = project_id
        self.region = region
        self.tenant_id = tenant_id 

    def get_access_token(self, username , password , project_id , region , tenant_id):
        auth_url = "https://iam.eu-west-0.prod-cloud-ocb.orange-business.com/v3/auth/tokens"
        payload = {"auth": {"identity":{"methods": ["password"],"password":{"user": {"name":username,"password":password,"domain":{"name":tenant_id}}}},"scope": {"project": {"id": project_id}}}}
        headers = {'Content-Type' : 'application/json;charset=utf8' , 'Accept' : 'application/json'}
        res = requests.post(auth_url , data=json.dumps(payload), headers=headers)
        self.token = str(res.headers['X-Subject-Token'])
        return self.token

