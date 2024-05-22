#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
from requests.auth import HTTPBasicAuth

def run_module():
    module_args = dict(
        endpoint=dict(type='str', required=True),
        host=dict(type='str', required=True, default='localhost'),
        port=dict(type='int', required=True, default=12000),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        params=dict(type='dict', required=False, default={})
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    endpoint = module.params['endpoint']
    host = module.params['host']
    port = module.params['port']
    username = module.params['username']
    password = module.params['password']
    params = module.params['params']

    url = f"http://{host}:{port}/{endpoint}"
    try:
        response = requests.get(url, params=params, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        result['original_message'] = response.json()
        result['message'] = 'Success'
    except requests.exceptions.RequestException as e:
        module.fail_json(msg=f"Failed to contact osctl API: {str(e)}", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
