#!/usr/bin/python
# (c) 2018 Rubrik, Inc
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
module: rubrik_get
short_description: Send a GET request to the provided Rubrik API endpoint.
description:
    - Send a GET request to the provided Rubrik API endpoint.
version_added: '2.8'
author: Rubrik Build Team (@drew-russell) <build@rubrik.com>
options:
  api_version:
    description:
      - The version of the Rubrik CDM API to call.
    required: True
    type: str
    choices: [v1, v2, internal]
  api_endpoint:
    description:
      - The endpoint of the Rubrik CDM API to call (ex. /cluster/me).
    required: True
    type: str
  authentication:
    description:
      - Flag that specifies whether or not to utilize authentication when making the API call.
    required: False
    type: bool
    default: True
  params:
    description:
      - An optional dict containing variables in a key:value format to send with the call.
    required: False
    type: dict
  timeout:
    description:
      - The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error.
    required: False
    type: int
    default: 30

extends_documentation_fragment: rubrikinc.cdm.credentials
requirements: [rubrik_cdm]
'''

EXAMPLES = '''
- name: Retrieve summary information for the "Ansible" SLA Domain
  rubrik_get:
    api_version: v1
    api_endpoint: "/sla_domain"
    params: {"name": "Ansible"}

- name: Retrieve summary information for the "Ansible" SLA Domain usingn params
  rubrik_get:
    api_version: v1
    api_endpoint: "/sla_domain?name=Ansible"
'''

RETURN = '''
response:
    description: The response body of the API call..
    returned: success
    type: str
    sample: {"acceptedEulaVersion": "1.1", "name": "DEVOPS-1"}
'''

from ansible.module_utils.rubrik_cdm import credentials, load_provider_variables, rubrik_argument_spec
from ansible.module_utils.basic import AnsibleModule

try:
    import rubrik_cdm
    HAS_RUBRIK_SDK = True
except ImportError:
    HAS_RUBRIK_SDK = False


def main():
    """ Main entry point for Ansible module execution.
    """

    results = {}

    argument_spec = dict(
        api_version=dict(required=True, type='str', choices=['v1', 'v2', 'internal']),
        api_endpoint=dict(required=True, type='str'),
        authentication=dict(required=False, type='bool', default=True),
        params=dict(required=False, type='dict'),
        timeout=dict(required=False, type='int', default=30),
    )

    argument_spec.update(rubrik_argument_spec)

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    ansible = module.params

    load_provider_variables(module)

    if not HAS_RUBRIK_SDK:
        module.fail_json(msg='The Rubrik Python SDK is required for this module (pip install rubrik_cdm).')

    node_ip, username, password, api_token = credentials(module)

    try:
        rubrik = rubrik_cdm.Connect(node_ip, username, password, api_token, enable_logging=True)
    except Exception as error:
        module.fail_json(msg=str(error))

    try:
        api_request = rubrik.get(ansible["api_version"], ansible["api_endpoint"], ansible["timeout"], ansible["authentication"], ansible["params"])
    except Exception as error:
        module.fail_json(msg=str(error))

    results["response"] = api_request

    module.exit_json(**results)


if __name__ == '__main__':
    main()
