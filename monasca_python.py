import json
import datetime
import json
import os
import time
from monascaclient import client

monasca_client = client.Client(api_version='2_0',
                      username=os.environ.get('OS_USERNAME'),
                      password=os.environ.get('OS_PASSWORD'),
                      auth_url=os.environ.get('OS_AUTH_URL'),
                      project_name=os.environ.get('OS_PROJECT_NAME'),
                      user_domain_name="Default",
                      project_domain_name="Default",
                      auth_version=os.environ.get('OS_IDENTITY_API_VERSION'),
                      endpoint='http://127.0.0.1/metrics/v2.0')


def get_metrics(names=[None], dimensions={}, limit=10):
    metrics = []
    for name in names:
        # Invoke the Monasca client
        metrics = metrics + monasca_client.metrics.list(name=name, dimensions=dimensions, limit=limit)
    return metrics

metrics = get_metrics(['openstack.handson_status'])
print json.dumps(metrics, indent=4)

