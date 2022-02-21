#!/bin/sh
IPAddress=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgadmin4_container)
echo $IPAddress
curl http://$IPAddress/