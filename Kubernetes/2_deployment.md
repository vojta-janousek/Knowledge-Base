# Deploy an app

- The Deployment instructs Kubernetes on how to create and update instances
of your application
- If the Node hosting an instance goes down or is deleted, the Deployment
controller replaces the instance with an instance on another Node in the cluster

--help after a kubectl command get additional info about possible parameters

$ kubectl create deployment deployment-name --image=my-link.com
- Searches for a suitable node where an instance of the application could be run
- Schedules the application to run on that Node
- Configures the cluster to reschedule the instance on a new Node when needed

$ kubectl get deployments // Lists current deployment
$ kubectl proxy // Proxy forwards communications into the cluster-wide,
private network. Ctrl+C to terminate

$ curl http://localhost:8001/version // Queries the version directly through the API

In order for the new deployment to be accessible without using the proxy,
a Service is required.
