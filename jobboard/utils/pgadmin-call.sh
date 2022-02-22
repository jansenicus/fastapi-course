#!/bin/sh
cd ..
clear
echo ------------------------------------------
echo PGAdmin Call
echo ------------------------------------------
IPAddress=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgadmin4_container)
echo try opening http://$IPAddress/, press ENTER to return
# Detect the platform (similar to $OSTYPE)
OS="`uname`"
case $OS in
  'Linux')
    OS='Linux'
    xdg-open http://$IPAddress/
    ;;
  'WindowsNT')
    OS='Windows'
    start http://$IPAddress/
    ;;
  'Darwin') 
    OS='Mac'
    open http://$IPAddress/
    ;;
esac
return