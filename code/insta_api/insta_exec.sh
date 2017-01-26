#!/bin/bash
# ------------------------------------------------------------------
# [Masaya Ogushi] Elastic Search Regist shell
#
#          library for Unix shell scripts.
#          Usage
#             you have to use this script `sudo` command in the docker enviroment
#             you have to use this script `nohup` command in the back ground
#          Reference
#              http://dev.classmethod.jp/tool/jq-manual-japanese-translation-roughly/
#
# ------------------------------------------------------------------

usage() {
    echo "$0 [Account Name] "
    exit
}
[[ "$#" -ne 1 ]] &&  usage

ACCOUNT_NAME=$1

# -- Body ---------------------------------------------------------

WORKDIR=`pwd`

# Setting virtual browser and setting firefox
export DISPLAY=:1
# If you see "selenium.common.exceptions.WebDriverException: Message: connection refused"
# you have to check $DISPLAY value
Xvfb :1 -screen 0 1024x768x24 > /dev/null &
firefox --display=:1&
mkdir ${WORKDIR}/img/${ACCOUNT_NAME}
python insta_api.py ${ACCOUNT_NAME} ${WORKDIR}/img/${ACCOUNT_NAME}
