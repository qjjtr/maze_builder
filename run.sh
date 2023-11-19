python3 -m venv env
source env/bin/activate
pip3 install requirements.txt
export PYHTONPATH=$PYTHONPATH:/$PWD
python3 maze_builder/main.py
