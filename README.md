# Spillman API Image Server Image Server 

The Spillman API Image Server Image Server is designed to work with the Spillman API Image Server to serve images securely using the authentication built into the Spillman API Image Server.

## REQUIREMENTS
*  Spillman server with proper access rights (must be installed on the Spillman Server)
*  All the requirements for Spillman API Image Server
*  Docker & Docker Compose

## INSTALL
We highly recommend people use docker for running the Spillman API Image Server, whether you are on Windows, macOS or Linux. This assumes you have Docker and Docker Compose already installed.
```
cd /opt
git clone https://github.com/sccity/spillman-api-img.git
cd spillman-api-img
./server.sh start
```

## BASIC COMMANDS
```
# Start the Spillman API Image Server
$ ./server.sh start

# Restart Spillman API Image Server (useful if things get stuck)
$ ./server.sh restart

# Stop the Spillman API Image Server server (temporarily)
$ ./server.sh stop

# Halt the Spillman API Image Server server
$ ./server.sh down

# Update everything to the latest version
$ ./server.sh update

# Rebuild everything from scratch
$ ./server.sh rebuild
```

## SETTINGS
In the settings.yaml file you will notice there are database settings. The database settings are for tokens and audit trail data. This should be set as the same settings for the Spillman API Image Server

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
