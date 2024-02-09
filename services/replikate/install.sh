#!/bin/bash
cd ~
if ! [ -d myyoutube ]
then
    mkdir myyoutube
fi
cd myyoutube

if ! [ -d myyt-3 ]
then
    echo "Iniciando o clone do repo"
    git clone https://github.com/ryan-maps/myyt-3.git
    cd ./myyt-3/datanode-server/
    rm ./alias.txt
else
    echo "Atualizando o repo"
    cd ./myyt-3/datanode-server/
    git pull
    rm ./alias.txt
fi
echo "Instalando dependencias"
pip install rpyc alembic flask sqlalchemy matplotlib

if ! [ -d database ]
then
    mkdir database
    echo "Instalando o banco"
    alembic upgrade head
else
    rm -rf ./database
    mkdir database
    echo "Instalando o banco"
    alembic upgrade head
fi

echo Starting DATANODE_SERVER
pkill -f app.py

python3 app.py &

disown

