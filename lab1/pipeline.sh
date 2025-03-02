#!/bin/bash
packages=("pandas" "sklearn")  # Replace with your system packages

for pckg in "${packages[@]}"; do
    if dpkg -l | grep -q "^ii  $pckg "; then
        continue
    else
        sudo apt-get install python3-$pckg
    fi
done
python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
