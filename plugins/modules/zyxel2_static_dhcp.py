#!/usr/bin/python
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for zyxel_static_dhcp
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': '<support_group>'
}

DOCUMENTATION = """
---
module: zyxel_static_dhcp
version_added: 2.9
short_description: 'Manages <xxxx> attributes of <network_os> <resource>.'
description: 'Manages <xxxx> attributes of <network_os> <resource>'
author: Ansible Network Engineer
notes:
  - 'Tested against <network_os> <version>'
options:
  config:
    description: The provided configuration
    type: list
    elements: dict
    suboptions:
      index:
        description:
        - Index
        type: int
      br_wan:
        description:
        - BrWan
        type: string
        default: Default
      enable:
        description:
        - Enable
        type: bool
      mac_addr:
        description:
        - MACAddr
        type: string
      ip_addr:
        description:
        - IPAddr
        type: string
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.jwnmulder.zyxel_vmg825.plugins.module_utils.network.zyxel_vmg8825.argspec.static_dhcp.static_dhcp import Static_dhcpArgs
from ansible_collections.jwnmulder.zyxel_vmg825.plugins.module_utils.network.zyxel_vmg8825.config.static_dhcp.static_dhcp import Static_dhcp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Static_dhcpArgs.argument_spec,
                           supports_check_mode=True)

    result = Static_dhcp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
