#!/usr/bin/env bash


# ====================================================
# import the utils 
. bash_utils.sh 

# ====================================================

#set -e


# ====================================================
# check if we have external options
EXTERNAL_OPTION=$1
if [[ -n "$EXTERNAL_OPTION" ]]; then
    echo "external option: $EXTERNAL_OPTION" 
fi

# check if we want to add a python interpreter check
if [[ -n "$WITH_PYTHON_INTERP_CHECK" ]]; then
    echo "WITH_PYTHON_INTERP_CHECK: $WITH_PYTHON_INTERP_CHECK " 
    EXTERNAL_OPTION="$EXTERNAL_OPTION -DWITH_PYTHON_INTERP_CHECK=$WITH_PYTHON_INTERP_CHECK"
fi
# ====================================================

if [[ -z "${USE_PYSLAM_ENV}" ]]; then
    USE_PYSLAM_ENV=0
fi
if [ $USE_PYSLAM_ENV -eq 1 ]; then
    . pyenv-activate.sh
fi  

print_blue '================================================'
print_blue "Building and installing cpp ..."

CURRENT_USED_PYENV=$(get_virtualenv_name)
print_blue "currently used pyenv: $CURRENT_USED_PYENV"

# cd cpp 

# # build utils 
# cd utils 
# . build.sh $EXTERNAL_OPTION       # use . in order to inherit python env configuration 
cd ..

cd .. 



