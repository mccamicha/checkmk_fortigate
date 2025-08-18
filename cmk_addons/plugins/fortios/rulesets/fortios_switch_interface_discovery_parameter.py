#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# This is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation in version 2. check_mk is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with GNU Make; see the file COPYING. If not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.

# WAGNER AG
# Developer: opensource@wagner.ch

"""
Check_MK WATO rule spec for FortiOS special agent

"""

from cmk.rulesets.v1 import Title, Help
from cmk.rulesets.v1.form_specs import DictElement, Dictionary, List, String, validators
from cmk.rulesets.v1.rule_specs import DiscoveryParameters, Topic


def _form_check_fortios_switch_interface_discovery() -> Dictionary:
    return Dictionary(
        title=Title("FortiOS switch interface discovery"),
        elements={
            "item_included": DictElement(
                parameter_form=List[str](
                    title=Title("Switch interface descriptions to include in monitoring"),
                    help_text=Help("Switch interface descriptions to include in monitoring. Can be full or partial strings."),
                    element_template=String(
                        custom_validate=(validators.LengthInRange(min_value=1),),
                    ),
                    editable_order=False,
                ),
            ),
            "item_excluded": DictElement(
                parameter_form=List[str](
                    title=Title("Switch interface descriptions to exclude from monitoring"),
                    help_text=Help("Switch interface descriptions to exclude from monitoring. Can be full or partial strings."),
                    element_template=String(
                        custom_validate=(validators.LengthInRange(min_value=1),),
                    ),
                    editable_order=False,
                ),
            ),
        },
    )


rule_spec_fortios_switch_interface_discovery = DiscoveryParameters(
    title=Title("FortiOS switch interface discovery"),
    topic=Topic.NETWORKING,
    name="fortios_switch_interface_discovery",
    parameter_form=_form_check_fortios_switch_interface_discovery,
)
