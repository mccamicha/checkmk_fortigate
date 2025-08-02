#!/bin/bash
ln -sv $WORKSPACE/cmk_addons/ $OMD_ROOT/local/lib/python3/cmk_addons/

ln -sv $WORKSPACE/lib $OMD_ROOT/local/lib/python3/cmk

source /omd/sites/cmk/.profile && echo 'cmkadmin' | /omd/sites/cmk/bin/cmk-passwd -i cmkadmin

echo "▹ Starting OMD... "
omd restart