#!/usr/bin/env bash
#
# Remove all packages from our python environment
#
# Use to prove requirements files, or clean-slate to remove unwanted packages
#
pip freeze | xargs pip uninstall -y
