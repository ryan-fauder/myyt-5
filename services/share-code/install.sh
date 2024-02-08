#!/bin/bash
cd ~
if ! [ -d sistemas_distribuidos ]
then
    mkdir sistemas_distribuidos
fi
cd sistemas_distribuidos

if ! [ -d myyt-3 ]
then
    git clone https://github.com/ryan-maps/myyt-3.git
    cd ./myyt-3/datanode-server/
    rm ./alias.txt
else
    cd ./myyt-3/datanode-server/
    git pull
    rm ./alias.txt
fi

pip install rpyc, alembic, flask, sqlalchemy

if ! [ -d database ]
then
    mkdir database
    alembic upgrade head
else
    rm -rf ./database
    mkdir database
    alembic upgrade head
fi

previous_process=$(netstat -nlp | grep 8090 | awk '{print $7}' | perl -pe "s/\/.*//")
echo previous process = $previous_process
if [ -n "$previous_process" ]; then kill $previous_process; fi
echo Starting DATANODE_SERVER
python3 app.py &
disown