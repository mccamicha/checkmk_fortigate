#!/bin/bash
PKGNAME=$(python3 -c 'print(eval(open("package").read())["name"])')
ln -sv $WORKSPACE/cmk_addons/plugins/$PKGNAME $OMD_ROOT/local/lib/python3/cmk_addons/plugins/$PKGNAME

source /omd/sites/cmk/.profile && echo 'cmkadmin' | /omd/sites/cmk/bin/cmk-passwd -i cmkadmin

echo "▹ Starting OMD... "
omd restart