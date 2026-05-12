# master_Mind
A *mastermind* game in python

run by entering <br>
`python3 master_mind.py` <br>
on the commandline

You get 10 attempts to guess the secret code, consisting of four digits.

## Good Luck!


## start the game in a docker container by running <br>
docker run --name mastermind_python -dt --mount type=bind,src="/devops/p4",dst=/usr/games/mastermind python_ubuntu

## execute the game in the container by running <br>
docker exec -it mastermind_python /bin/bash/usr/games