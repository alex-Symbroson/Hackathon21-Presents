#!/bin/bash

PY=`type -p python || type -p python3`
#PIP=`type -p pip || type -p pip3`

$PY presents.py $@
