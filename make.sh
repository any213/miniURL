python3 -m pip install virtualenv
virtualenv miniurl-env
virtualenv -p python3 miniurl-env
. ./miniurl-env/bin/activate
pip install redis
pip install flask
python3 main.py &
