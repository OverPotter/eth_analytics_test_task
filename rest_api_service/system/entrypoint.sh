#!/bin/bash
uvicorn --host 0.0.0.0 --port 8000 src.rest_main:app
