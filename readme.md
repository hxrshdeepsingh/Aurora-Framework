# Aurora Framework

Aurora is a backdoor framework for creating windows payload. It consists of a control server and payloads, and uses sockets to establish connections.

## Features
Payload can:
- Root shell ( `required Administrator permission`)
- System information
- Execute commands on target machine
- Upload/Download any type of files
- Get all processes running in a system
- Kill process by name, id etc...
- Enable/Disable windows services
- Start/Stop windows service

## Server structure

- `server/`
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.
- `storage/` : For storing files.

## Payload structure

- `payload.py`
  - `shell()`: Establishes a remote shell session.
  - `upload()`: Sends files to the target machine.
  - `download()`: Retrieves files from the target.
  - `system()`: Fetches system information.
  - `command()`: Executes custom commands.
  - `root()`: Runs commands with elevated privileges.
  - `process_info()`: Lists running processes.
  - `service_info()`: Manages Windows services.
  - `kill()`: Terminates processes by name or ID.

## Requirements

- `python`
- `linux | Windows`