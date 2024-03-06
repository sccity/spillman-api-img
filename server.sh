#!/bin/bash

docker_compose="docker-compose -f docker-compose.yaml"

[ -f config/settings.yaml ] || { echo "Missing settings.yaml file. Exiting."; exit 1; }

if [[ $1 = "start" ]]; then
  echo "Starting Spillman API Image Server..."
	$docker_compose up -d
elif [[ $1 = "stop" ]]; then
	echo "Stopping Spillman API Image Server..."
	$docker_compose stop
elif [[ $1 = "restart" ]]; then
	echo "Restarting Spillman API Image Server..."
  $docker_compose down
  $docker_compose up -d
elif [[ $1 = "down" ]]; then
	echo "Tearing Down Spillman API Image Server..."
	$docker_compose down
elif [[ $1 = "rebuild" ]]; then
	echo "Rebuilding Spillman API Image Server..."
	$docker_compose down --remove-orphans
	$docker_compose build --no-cache
elif [[ $1 = "update" ]]; then
	echo "Updating Spillman API Image Server..."
	$docker_compose down --remove-orphans
	git pull origin prod
else
	echo "Unkown or missing command..."
fi