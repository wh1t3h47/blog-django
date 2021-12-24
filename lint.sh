#!/bin/env bash

lintDir="FreiRui"
cpuCount=$(getconf _NPROCESSORS_ONLN)

autopep8 --diff -j ${cpuCount} -r ${lintDir} | patch -p1

