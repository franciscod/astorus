# astorus
This is a prototype made for the **Automatic Software Repair** course by [Martin Monperrus](https://github.com/monperrus), [more info about the course](www.monperrus.net/martin/eci2015)

This uses the `TreeWalk` class from [astor](https://github.com/berkerpeksag/astor), which walks the AST and does a modification on each relevant node.

The provided examples target *off by one* errors and *bad condition* errors (negating the condition, or swapping `>` by `<` and the like)

There is also an example which targets both of these errors and produces *SyntaxError*s, which was intended to get solved at the live demo in the course that had to be shortened :(

## Installing

- Clone the repo and cd:
 ```
$ git clone git@github.com:franciscod/astorus.git && cd astorus
```
- Create a virtualenv, activate it and install the dependency with pip:
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Running

- Enter the virtualenv (maybe you're already on it if you just installed it
- Go to an example and run the `shuffler` program:
```
$ . venv/bin/activate
$ cd astorus/examples/offbyone
$ python ../../shuffler.py
```

## How it works 

The core is implemented at `shuffler.py`.

Each example has a main implementation, some tests (used as oracle) and two walk implementations:
 - `LightWalk` is ran once: it just counts the nodes that should be modified
 - `BoomWalk` is ran every time, with a number from 0 to 2^count as argument (this tries to modify all combinations of node modifications)


## Caveats

The generated patches are based on the `normalized` source after the source->ast->source roundtrip, so it loses the comments and the formatting comes a little messed up.

Also, it's now bruteforcing the whole space so it's slow on non-trivial programs.

It would be really cool to extract the walkers from the examples, so you maybe have a dozen of walkers with their strategies and you can use them all for any buggy code.
