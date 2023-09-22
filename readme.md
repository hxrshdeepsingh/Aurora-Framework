# Handler server

A socket server that fulfills three primary functions:
- Functioning as a control server.
- Accepting target connections.
- Receiving data from these targets.

## Server Structure

Server is structured with the following components:

- `server/`
  - `server.py`  :  Socket server initialization.
  - `handler.py` :  Functions for server validation and operations.

- `storage/` : For storing files.