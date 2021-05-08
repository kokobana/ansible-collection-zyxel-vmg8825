#
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the zyxel facts module.
"""


class FactsArgs:  # pylint: disable=R0903
    """ The arg spec for the zyxel facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'static_dhcp',
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=choices,
                                         type='list'),
    }
