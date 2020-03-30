## Creating a Dockerfile

alpine - smallest file size

FROM python:2.7-alpine
Imports the selected image

RUN - runs a script as it would normally be ran on the operating system
of the image. Alpine is a linux based image.
RUN mkdir /app

WORKDIR /app
Makes it so that all further operation are done within the selected work
directory. Saves user from having to cd into it later on.

COPY requirements.txt requirements.txt
Copies a file. In the first argument, it is assumed that the copied file is
in the same directory as the Dockerfile. The second argument does not have to
be /app/requirements.txt, as the WORKDIR has been specified as such.

RUN pip install -r requirements.txt
Make sure the dependencies are installed first.

COPY . .
Copies everything above and on the same level as the Dockerfile into WORKDIR.

Do not switch the positions of this command and the installing of requirements
and/or dependencies, as they will rarely change and their state is cached.
This way, they will not be installed again if they were not changed.

Every command creates a separate layer, so it is always a good idea to chain
commands so as to minimise the number of layers being used.

LABEL maintainer="Vojta <my@email.com>" \
      version="1.0"
Creates labels that can be extracted by the application later. Key:Value pairs.
Chain label commands so they only use one layer.

RUN runs commands after an image has been created, CMD runs them immediately.


- docker --help
- docker image --help
- docker image build -t web1 (-t tag - so hash does not need to be used)

- docker image inspect web1
A JSON dump with a lot of information about the built image. Layers can be
checked here (WORKDIR does not create a layer).

- docker image ls
Lists all images created on the machine.

- docker image rm web1
- docker image rm web1:1.0 (1.0 is a tagged version)
Removes the image.
