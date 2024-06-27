#!/bin/bash
# Espera hasta que PostgreSQL esté listo
while ! pg_isready -h db -p 5432 -U myuser > /dev/null 2> /dev/null; do
  sleep 1
done

python init_db.py
