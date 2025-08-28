#!/bin/bash
psql -h localhost -p 15432 -U postgres -f delete_xargs.sql
