#!/bin/bash
ln -sv $WORKSPACE/cmk_addons $OMD_ROOT/local/lib/python3/cmk_addons/

ln -sv $WORKSPACE/lib $OMD_ROOT/local/lib/python3/cmk

ln -sv $WORKSPACE/cmk $OMD_ROOT/local/lib/python3/cmk

ln -sv $WORKSPACE/plugins_legacy $OMD_ROOT/local/share/check_mk

source /omd/sites/cmk/.profile && echo 'cmkadmin' | /omd/sites/cmk/bin/cmk-passwd -i cmkadmin

echo "▹ Starting OMD... "
omd restart