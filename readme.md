# Aurora Framework

Aurora is a backdoor framework for creating windows payload. It consists of a control server and payloads, and uses sockets to establish connections.

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

## Server structure

- `server/`
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.

- `storage/` : For storing files.

## Payload structure