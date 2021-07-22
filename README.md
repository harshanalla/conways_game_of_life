Provide an implementation of Conway's game of life, written in python.

Conways game of life [rules](https://playgameoflife.com/info):

    - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies, as if by overpopulation.
    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Requirements
	- The game should run in the console/terminal/command line.

	- The game should start in a random state by default.

	- The game should be installable (using 'pip install .'), and should be launchable with the command 'game-of-life' (an entrypoint should be specified in setup.py)

	- The game should take up the entirety of the available console by default
		- dynamic resizing is not required, but a console of any size should be able to start a new game

	- Include instructions in a Readme.md at the root of the repository. It should include the instructions to run the application and/or any environmental setup.

Code quality, standards, and best practices are up to you but will be considered as core to the assignment.

Don't get too carried away! Try to constrain yourself to a handful of hours. 

Don't forget that at the end of the day we're hoping you at least have some fun with it. 

When complete, send us the link to the repo (github, gitlab, etc are fine).