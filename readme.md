# Aurora Framework

Aurora is a backdoor framework for creating Android payloads. It consists of a control server and client payloads, and uses sockets to establish connections.

## Features
Payload can:
- Root shell ( `required Administrator permission`)
- System information
- Execute commands on target machine
- Upload/Download any type of files from remote host
- Get all processes running in a system
- Kill process by name, id etc...
- Create new user account
- Delete existing users accounts
- Change password for an existing user account
- Enable/Disable windows services
- Start/Stop windows service

# Server

A socket server that fulfills three primary functions:
- Functioning as a control server.
- Accepting target connections.
- Receiving data from these targets `.txt files` .

## Server Structure

- `server/`
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.

- `storage/` : For storing files.