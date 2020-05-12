# Explore your app

When you create a Deployment, Kubernetes creates a Pod to host the application instance.
A Pod is a Kubernetes abstraction that represents a group of one or more
application containers and some shared resources for those containers such as shared
storage (as Volumes), networking, information about how to run each container etc.

Nodes

A Pod always run on a Node. A Node can have multiple pods, the Kubernetes
master automatically handles scheduling the pods across the Nodes in the cluster.
Every Node runs at least:
- Kubelet, a process responsible for commucation between the Master and the
Node, it manages the Pods and the containers running on a machine
- A container runtime (Docker) responsible for pulling the container image
from a registry, unpacking the container, and running the application

$ kubectl get // list resources
$ kubectl describe // show detailed information about a resource
$ kubectl logs // print the logs from a container in a pod
$ kubectl exec // execute a command on a container in a pod

$ kubectl get pods // List existing pods
$ kubectl describe pods // To view what containers are inside pods and what
images are used to build those containers
$ kubectl proxy // Run in separate terminal - proxy access to Pods in order to debug them
$ kubectl logs $POD_NAME // Retrieves logs for a Pod with the specified name

Once the Pod is up and running, we can execute commands directly on the container.

$ kubectl exec $POD_NAME env // List environment variables, name of the Pod
can be omitted if only one is running
$ kubectl exec -ti $POD_NAME bash // Starts a bash session in the Pod’s container
$ exit // Closes the container connection
