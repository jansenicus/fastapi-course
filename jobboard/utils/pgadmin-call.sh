#!/bin/sh
cd ..
clear
echo ------------------------------------------
echo PGAdmin Browser Call
echo ------------------------------------------
INSTANCE=pgadmin4_container
IPADDRESS=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $INSTANCE)
PORT=$(docker inspect $INSTANCE | jq -r '.[].NetworkSettings.Ports."80/tcp"[].HostPort')
echo try opening http://$IPADDRESS:$PORT/
OS="`uname`"
case $OS in
  'Linux')
    OS='Linux'
    xdg-open http://$IPADDRESS:$PORT/
    exit
    ;;
  'WindowsNT')
    OS='Windows'
    start http://$IPADDRESS:$PORT/
    ;;
  'Darwin') 
    OS='Mac'
    open http://localhost:$PORT/
    ;;
esac
exit