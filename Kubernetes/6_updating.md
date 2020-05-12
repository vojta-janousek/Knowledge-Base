# Updating an app

Rolling updates allow Deployments’ update to take place with zero downtime by
incrementally updating Pods instances with new ones. The new Pods will be
scheduled on Nodes with available resources.

Scaling application to run multiple instances is a requirement for performing
updates without affecting application availability. By default, the maximum
number of Pods that can be unavailable during the update and the maximum number
of new Pods that can be created, is one.

Similar to application Scaling, if a Deployment is exposed publicly, the
Service will load-balance the traffic only to available Pods during the update.
An available Pod is an instance that is available to the users of the application.

Rolling updates allow the following actions:
- Promote an application from one environment to another via container image updates
- Rollback to previous versions
- Continuous Integration and Continuous Delivery of application with zero downtime

$ kubectl set image deployments/deployment-name deployment-name=something/deployment-name:v2
// To update the image of the application to version 2. The command notifies
the Deployment to use a different image for your app and initiates a rolling update

$ kubectl rollout status deployments/deployment-name
