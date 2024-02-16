# local-llm-api-server
Local LLM REST API server built for the Nvidia 2024 Gen AI on RTX PCs Developer Contest

## Requirements

- Windows 10+
- RTX 30 series graphics card

## Prerequisites

- `git` [installed for Windows](https://git-scm.com/download/win) and available as a command within the environment variable PATH.
- `python3` installed and available as a command within the environment variable PATH.

Note: If you are using VS Code and make a change to the PATH variable, please close the VS Code application and re-open it.

## Getting started

Run the following commands in a Powershell terminal:

1. `cd` to the root directory (local-llm-api-server)
2. `pip3 install -r requirements.txt` (if you want to use venv, go right ahead)
3. `.\setup.bat`

## Starting the server

To start the server, run the following command:

`python3 local-llm-api-server\app.py`