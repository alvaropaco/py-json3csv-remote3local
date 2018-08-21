# How to use

> You can build this localy or pull from Dockerhub: `docker pull alvaropaco/meupedidos`

## Steps

1. Building and runnig test cases:

```bash 
docker build -t meuspedidos . && docker run -it meuspedidos
```

##### This will run the test cases to the project.

2. Running other scripts with `docker run`: 

```bash
    docker buid -t meupedidos .
    docker run -it --name meuspedidos -v "$PWD":/usr/src/myapp -w /usr/src/myapp meuspedidos /bin/bash
```

Author: [Álvaro Paçó](https://alvaropaco.github.io/my-resume/)