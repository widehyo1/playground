#!/bin/bash
sed "s/\\\n/\\\\\\\n/g" bulk_data_xargs_v2.jsonl > bulk_data_xargs_v2.txt
