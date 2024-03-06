# Spillman API Image Server 

The Spillman API Image Server is designed to work with the Spillman API to serve images securely using the authentication built into the Spillman API.

## REQUIREMENTS
*  Spillman server with proper access rights (must be installed on the Spillman Server)
*  All the requirements for Spillman API
*  Docker & Docker Compose

## INSTALL/RUN
```
cd /opt
git clone https://github.com/sccity/spillman-api-img.git
```
Edit the docker-compose.yaml file and change $PWD/config to the location of your images. Leave unchanged to test with test.png/test.jpg. You will also need to edit the settings.yaml file with database settings.
```
./server.sh start
```

## SETTINGS
In the settings.yaml file you will notice there are database settings. The database settings are for tokens and audit trail data. This should be set as the same settings for the Spillman API

## LICENSE
Copyright (c) Santa Clara City UT\
Developed for Sanata Clara - Ivins Fire & Rescue

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
