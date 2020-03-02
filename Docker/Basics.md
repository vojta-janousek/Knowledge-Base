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

- VMs use hypervisor, that runs separate guest OSes
- Guest OS contains bins/libs for an app and the app itself
- This uses a lot of memory and disk space
- Starts in minutes

- Docker uses a Docker daemon, which distributes resources among containers
- Each app and its bins/libs is contained within a container
- Starts in milliseconds
