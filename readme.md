# Aurora Framework

Aurora is a backdoor framework for creating windows payload. It consists of a control server and payloads, and uses sockets to establish connections.

## Features
Payload can:
- Root shell `required Administrator permission`
- System information
- Delete/Upload files on the host machine. 
- Execute commands on target machine.
- Upload/Download any type of files.
- Get all processes running in a system.
- Kill process by name, id etc...
- Enable/Disable windows services.
- Start/Stop windows service.
- Start/Restart windows system.

## Server structure

- server/
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.

## Payload structure

- payload.py
  - `command()`: Executes system commands.
  - `audio()`: Records the audio.
  - `screenshot()`: Records the audio.

## Requirements 

- `python`
- `linux | Windows`