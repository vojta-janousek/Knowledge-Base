## Advantages

- Runs quicker than VMs
- Saves disk space
- Dependency overlap between applications does not cause duplicity
- Portability
- New frameworks are easy to install
- Microservices become easier to manage
- Documents itself

## Docker vs VMs

- Both run on the host operating system
- They are compatible, a VM can run Docker (can be used to test OS)

- VMs use hypervisor, that runs separate guest OSes
- Guest OS contains bins/libs for an app and the app itself
- This uses a lot of memory and disk space
- Starts in minutes
- Analogy: House (higher cost, more robust)

- Docker uses a Docker daemon, which distributes resources among containers
- Each app and its bins/libs is contained within a container
- Separates individual applications, but systems
- Starts in milliseconds
- Analogy: Apartment (share resources, scalable)

## Docker architecture

- Docker daemon runs on the server
- Daemon exposes a REST API through which other tools can communicate with it
- Docker CLI: command-line tool that lets you talk to the daemon directly
- Daemon acts as a server, tools act as clients
- This client can be used to manage docker components: containers, images etc
- Docker registry is also part of this ecosystem


## Docker basics

Check whether Docker is installed and which version:

- docker info
- docker-compose --version
- docker run hello-world

There is no local hello-world image, so it is pulled from the Docker hub.
The second time running the command is much quicker, as the image now exists.

A running instance of a docker image is called a container.
Many containers can be launched from one image.

Containers are immutable - changes made to it while it's running will be lost.
If the container is running, and a file is created within it, the file will
be lost once the container is halted.

- docker run -it alpine sh (runs an alpine linux container)

Docker Registry (Hub) has many Docker repositories.
Repositories have many images, each image can have its own tag.

Dockerfile: a recipe for creating a Docker image.
