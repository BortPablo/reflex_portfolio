TO CREATE NEW DOCKER IMAGE
docker build -t bort44/myportfolio:0.0.X
TO PUSH NEW DOCKER IMAGE
docker push bort44/myportfolio:0.0.X
TO RUN DOCKER IMAGE
docker run -p 3000:3000 -p 8000:8000 bort44/myportfolio:0.0.X

YOU NEED TO LOG IN AS BORT44 TO PUSH TO DOCKER HUB
```