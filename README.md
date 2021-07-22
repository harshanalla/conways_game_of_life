Provide an implementation of Conway's game of life, written in python.

Conways game of life [rules](https://playgameoflife.com/info):

    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.	

Requirements

	- The game should run in the console/terminal/command line.

	- The game should start in a random state by default.

	- The game should be installable (using 'pip install .'), and should be launchable with the command 'game-of-life' (an entrypoint should be specified in setup.py)

	- The game should take up the entirety of the available console by default (I was not able to implement this)
		- dynamic resizing is not required, but a console of any size should be able to start a new game

	- Include instructions in a Readme.md at the root of the repository. It should include the instructions to run the application and/or any environmental setup.

Additional Features

	- The game will let you know if an arrangment was seen before

	- --refresh-rate 500 | Refresh rate (in ms)

	- --show-coordinates | The board should have the X axis coordinates along the bottom and Y coordinates along the left

	- --size             | Size of the board (size X size)

	- --clear-terminal   | clears the terminal

	- --spawn-rate       | Spawn percentage of new players after Generation 1 (default 100, guaranteed spawn)

Instructions:

	1. Clone to local dir
	2. cd to local dir
	3. run pip install .
	4. game-of-life --show-coordinates

