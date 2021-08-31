# docker-load-graph
---

Have you ever been working with a docker stack, and been interested in how your containers fair over time? Me too.

This project exists to solve that problem.

## What does it do?

Very simply this project uses [plotext](https://github.com/piccolomo/plotext) to display the current status
of key [docker](https://www.docker.com/) container metrics in real time on the command line.

![](https://raw.githubusercontent.com/cjmcgraw/docker-load-graph/main/.docs/0000-example.gif)

## How do I use it?

I've uploaded this project to the PYPA repository for pip to access. You can simply install this using `python3.7>` with
```
pip install docker-load-graph
```

To execute this project run:

```
docker-load-graph
```

It is just that simple.

# Trouble Shooting:
---

> I cant find the command. `docker-load-graph` just doesn't seem to work

Check out where its installed with `pip show docker-load-graph`

It will be in a location like `/home/qarl/.local/lib/...`. It will also add a script to the bin in the same directory. Make sure that is available in your path
and it should work just fine. My favorite way of doing this is adding it to the path in my `.bashrc` or `.zshrc` file:

```
echo 'export $PATH=${PATH}:$HOME/.local/bin' >> ${HOME}/.bashrc
source ${HOME}/.bashrc
```

Will generally do it!
