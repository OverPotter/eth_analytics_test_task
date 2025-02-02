#!/bin/bash
alembic upgrade head
cron -f
