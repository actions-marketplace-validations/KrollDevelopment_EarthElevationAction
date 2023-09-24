#!/bin/bash

# Exit immediately on error
set -e

python /usr/src/app/getElevations.py "$INPUT_COORDINATESJSON"
