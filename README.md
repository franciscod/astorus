# astorus
This is a prototype made for the **Automatic Software Repair** course by [Martin Monperrus](https://github.com/monperrus), [more info about the course](www.monperrus.net/martin/eci2015)

This uses the `TreeWalk` class from [astor](https://github.com/berkerpeksag/astor), which walks the AST and does a modification on each relevant node.

The provided examples target *off by one* errors and *bad condition* errors (negating the condition, or swapping `>` by `<` and the like)

There is also an example which targets both of these errors and produces *SyntaxError*s, which was intended to get solved at the live demo in the course that had to be shortened :(

## Usage

- Clone the repo (`git clone git@github.com:franciscod/astorus.git`) and `cd astorus`
- Create a virtualenv (`virtualenv venv`), activate it (`. venv/bin/activate`) and install the dependency with pip (`pip install -r requirements.txt`)
- Go to an example (`cd astorus/examples/offbyone`) and run the `shuffler` program: `python ../../shuffler.py`

## How it works 
The core is implemented at `shuffler.py`.

Each example has a main implementation, some tests (used as oracle) and two walk implementations:
 - `LightWalk` is ran once: it just counts the nodes that should be modified
 - `BoomWalk` is ran every time, with a number from 0 to 2^count as argument (this tries to modify all combinations of node modifications)


## Improvements

It would be really cool to extract the walkers from the examples, so you maybe have a dozen of walkers with their strategies and you can use them all for any buggy code.

Also, it's now bruteforcing the whole space so it's slow on non-trivial programs.
