# Expose an app publicly

A Service in Kubernetes is an abstraction which defines a logical set of Pods
and a policy by which to access them. Services enable a loose coupling between
dependent Pods. A Service is defined using YAML or JSON. The set of Pods
targeted by a Service is usually determined by a LabelSelector.

Although each Pod has a unique IP address, those IPs are not exposed outside
the cluster without a Service. Services allow your applications to receive
traffic. Services can be exposed in different ways by specifying a type in
the ServiceSpec:
- ClusterIP (default): Exposes the Service on an internal IP in the cluster.
This type makes the Service from within the cluster
- NodePort: Exposes the Service on the same port of each selected Node
in the cluster using NAT. Makes a Service accessible from outside the cluster.
Superset of ClusterIP
- LoadBalancer: Creates an external load balancer in the current cloud and
assigns a fixed, external IP to the Service. Superseet of NodePort
- ExternalName: Exposes the Service using an arbitrary name by returning
a CNAME record with the name. No proxy is used.

A Service routes traffic across a set of Pods. Services are the abstraction
that allow pods to die and replicate. Services match a set of Pods using
labels and selectors, a grouping primitive that allows logical operation on
objects in Kubernetes.
Labels are key/value pairs attaches to objects and can be used in any number of ways:
- Designate objects for development, test, and production
- Embed version tags
- Classify an object using tags

Labels can be attached to object at creation time or later on.

$ kubectl expose deployment/deployment-name —type=“NodePort” —port 8080
Create a new service and expose it to external traffic
$ kubectl describe services/deployment-name // To find out what port was
opened externally (by the NodePort option)

$ export NODE_PORT=$(kubectl get services/deployment-name -o go-template=
  ‘{{(index .spec.ports 0).nodePort}}’)
// Create an environment variable called NODE_PORT that has the values of
the Node port assigned

$ kubectl describe deployment // To check the name of the label
$ kubectl get pods -l run=deployment-name // Use this label to query our list of Pods
$ kubectl get services -l run=deployment-name // Same, but for services

$ export POD_NAME=$(kubectl get pods -o go-template —template
  ‘{{range .items}}{{.metadata.name}}{{“\n”}}{{end}}’)
// Get the name of the Pod and store it in the POD_NAME environment variable
$ kubectl label pod $POD_NAME app=v1 // To apply a new label
$ kubectl get pods -l app=v1 // Query the list of pods using the new label

Deleting a service

$ kubectl delete service -l run=deployment-name // Deletes a service
$ kubectl get services // Confirm the service is gone
