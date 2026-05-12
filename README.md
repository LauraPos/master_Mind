# master_Mind
A *mastermind* game in python

You get 10 attempts to guess the secret code, consisting of four digits.

## Good Luck!

## build the docker image by running <br>
docker build -t <naam van de docker image> .  < ----- de "." geef aan dat je in de map staat waar de Dockerfile zich bevindt

## create docker container met het gebruik van de docker image.  <br>
docker run --name <naam voor de continer> -dt --mount type=bind,src="PATH TO YOUR LOCAL MAP(waar je mastermind bestanden staan)",dst=/usr/games/mastermind <naam van de docker image>

## execute the game in the container by running <br>
docker exec -it <docker_image> /bin/bash/

## na dat je in de container bent, ga naar de map waar je mastermind bestanden staan en
run by entering <br>
`python3 master_mind.py` <br>
on the commandline




## alleen voor 3li4n en als voorbeeld. <br>
docker run --name mastermind_python -dt --mount type=bind,src="/devops/p4",dst=/usr/games/mastermind python_ubuntu

docker exec -it mastermind_python /bin/bash/usr/games