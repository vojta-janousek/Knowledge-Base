# Create a cluster

Kubernetes automates the distribution and scheduling of application containers
across a cluster in a more efficient way.

- The Master coordinates the cluster
- Nodes are the workers that run applications (VMs)
- Each node has a Kubelet, an agent for managing the node and communicating
with the Master
- Nodes communicate with the master using Kubernetes API, which the master exposes

A cluster that handles production traffic should have a minimum of 3 nodes.

$ minikube version
$ minikube start // Starts a cluster. Minikube starts a VM and a cluster runs in it

kubectl - command-line interface

$ kubectl version // Client version is the kubectl version, the server version
is the Kubernetes version installed on the master

$ kubectl cluster-info
$ kubectl get nodes // Shows all nodes that can be used to host applications
