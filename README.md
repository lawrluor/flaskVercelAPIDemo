Reference: https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k

requirements.txt file must have lower version of markupsafe installed:

https://github.com/aws/aws-sam-cli/issues/3661#issuecomment-1044340547

```
Flask==1.1.4
markupsafe==2.0.1
```
