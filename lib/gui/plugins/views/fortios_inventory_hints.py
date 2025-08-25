#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# WAGNER AG
# Developer: opensource@wagner.ch

"""
Check_MK agent based checks to be used with agent_fortios Datasource

"""

from cmk.gui.i18n import _l
from cmk.gui.views.inventory.registry import inventory_displayhints

inventory_displayhints.update(
    {
        ".networking.fortios.": {
            "title": _l("Fortigate Managed Devices"),
            "view": "fortiosinventory",
        },
        ".networking.fortios.accesspoints:": {
            "title": _l("Accesspoints"),
            "keyorder": ["name", "ip_address", "model", "serial_number", "version", "build", "end_of_support"],
        },
        ".networking.fortios.accesspoints:*.name": {"title": _l("Name")},
        ".networking.fortios.accesspoints:*.ip_address": {"title": _l("IP address")},
        ".networking.fortios.accesspoints:*.model": {"title": _l("Model")},
        ".networking.fortios.accesspoints:*.serial_number": {"title": _l("Serial number")},
        ".networking.fortios.accesspoints:*.version": {"title": _l("Version")},
        ".networking.fortios.accesspoints:*.build": {"title": _l("Build")},
        ".networking.fortios.accesspoints:*.end_of_support": {"title": _l("End of support")},
        ".networking.fortios.accesspoints.lldp:": {
            "title": _l("LLDP"),
            "keyorder": ["switch_name", "switch_port", "switch_description", "local_port", "local_port_description"],
        },
        ".networking.fortios.accesspoints.lldp:*.local_port": {
            "title": _l("Local Port"),
        },
        ".networking.fortios.accesspoints.lldp:*.local_port_description": {
            "title": _l("Local Port description"),
        },
        ".networking.fortios.accesspoints.lldp:*.switch_name": {
            "title": _l("Switch Name"),
        },
        ".networking.fortios.accesspoints.lldp:*.switch_port": {
            "title": _l("Switch Port"),
        },
        ".networking.fortios.accesspoints.lldp:*.switch_description": {
            "title": _l("Switch Description"),
        },
        ".networking.fortios.switches:": {
            "title": _l("Switches"),
            "keyorder": ["name", "model", "serial_number", "version", "build", "end_of_support"],
        },
        ".networking.fortios.switches:*.name": {
            "title": _l("Name"),
        },
        ".networking.fortios.switches:*.model": {
            "title": _l("Model"),
        },
        ".networking.fortios.switches:*.serial_number": {
            "title": _l("Serial number"),
        },
        ".networking.fortios.switches:*.version": {
            "title": _l("Version"),
        },
        ".networking.fortios.switches:*.build": {
            "title": _l("Build"),
        },
        ".networking.fortios.switches:*.end_of_support": {
            "title": _l("End of support"),
        },
    }
)
