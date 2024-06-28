#!/bin/bash

set -e

# Ejecuta el script de inicialización de la base de datos
/app/init_db.sh

# Ejecuta el servidor Flask
exec "$@"