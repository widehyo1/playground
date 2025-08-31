#!/bin/bash
psql -h localhost -p 15432 -U postgres -f insert_clean_csv.sql
