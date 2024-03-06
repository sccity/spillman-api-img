# Spillman API Image Server [![CircleCI](https://dl.circleci.com/status-badge/img/gh/sccity/spillman-api-img/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sccity/spillman-api-img/tree/master) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/a45ad698a70240778adce56adfd55b67)](https://app.codacy.com/gh/sccity/spillman-api-img/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

The Spillman API Image Server is designed to work with the [Spillman API](https://github.com/sccity/spillman-api) to serve images securely using the authentication built into the Spillman API.

## REQUIREMENTS
*  Spillman server with proper access rights (must be installed on the Spillman Server)
*  All the requirements for [Spillman API](https://github.com/sccity/spillman-api?tab=readme-ov-file#requirements)
*  Docker & Docker Compose

## INSTALL
We highly recommend people use docker for running the Spillman API Image Server, whether you are on Windows, macOS or Linux. This assumes you have Docker and Docker Compose already installed. You may have to change the port configuration in docker-compose.yaml. Right now it is set to run on 8080, but you can change to any port that is open. You will also need to change "$PWD/config" to the folder that stores images for Spillman.
```
cd /opt
```
```
sudo git clone https://github.com/sccity/spillman-api-img.git
```
```
cd spillman-api-img
```
**Edit your settings as described below.**
```
sudo ./server.sh start
```

## BASIC COMMANDS

Start the Spillman API Image Server
```
sudo ./server.sh start
```

Restart Spillman API Image Server (useful if things get stuck)
```
sudo ./server.sh restart
```

Stop the Spillman API Image Server server (temporarily)
```
sudo ./server.sh stop
```

Halt the Spillman API Image Server server
```
sudo ./server.sh down
```

Update everything to the latest version
```
sudo ./server.sh update
```

Rebuild everything from scratch
```
sudo ./server.sh rebuild
```

## LICENSE
Copyright (c) Santa Clara City UT\
Developed for Santa Clara - Ivins Fire & Rescue

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
