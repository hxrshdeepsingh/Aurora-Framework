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