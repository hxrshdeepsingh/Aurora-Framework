# Handler server

A socket server that fulfills three primary functions: accepting client connections, receiving data from these clients, functioning as a control server for efficiently recording incoming data.

## Server Structure

Server is structured with the following components:

- `server/`
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.

- `storage/` dir : For storing files.