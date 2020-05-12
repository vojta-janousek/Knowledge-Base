# Scaling an app

When traffic increases, we will need to scale the application to keep up with
the user demand. Scaling is accomplished by changing the number of replicas
in a Deployment.

Scaling out a Deployment will ensure new Pods are created and scheduled to Nodes
with available resources. Scaling will increase the number of Pods to the new
desired state.
Running multiple instances of an application will require a way to distribute
the traffic to all of them. Service have an integrated load-balancer that will
distribute network traffic to all Pods of an exposed Deployment. Services will
monitor continuously the running Pods using endpoints, to ensure the traffic
is sent only to available Pods.
Once you have multiple instances of an Application running, you would be able
to do Rolling updates without downtime.

$ kubectl get rs // To see the ReplicaSet created by the Deployment
- DESIRED: displays the desired number of replicas of the application, which
you define when you create the Deployment
- CURRENT: displays how many replicas are currently running

kubectl scale deployments/deployment-name —replicas=4
// Scales the Deployment to 4 replicas
