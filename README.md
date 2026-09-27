# Simple Clicker

A simple **clicker game** built with Python and Tkinter.

Click the button to earn coins, buy upgrades, increase your clicking power, and earn coins automatically.

## Features

* Click to earn coins
* Upgrade clicking power
* Buy automatic coin generation
* Upgrade levels
* Increasing upgrade prices
* Automatic coins every second
* Simple graphical interface
* Built with object-oriented programming

## Technologies

* Python
* Tkinter
* Object-Oriented Programming (OOP)

## Installation

Tkinter is included with most standard Python installations, so no external packages are required.

Clone the repository:

```bash
git clone https://github.com/your-username/simple-clicker.git
```

Go to the project folder:

```bash
cd simple-clicker
```

Run the game:

```bash
python main.py
```

## How to Play

### 1. Click

Press the **CLICK HERE!!!** button to earn coins.

Each click gives you the current amount of `click_power`.

For example:

```text
click_power = 1
```

One click gives:

```text
+1 coin
```

After buying an upgrade:

```text
click_power = 2
```

One click gives:

```text
+2 coins
```

### 2. Buy Upgrades

The game has two upgrades:

* **Stronger Click** — increases the number of coins earned per click.
* **Auto Coins** — automatically generates coins every second.

### 3. Upgrade Prices

After purchasing an upgrade, its price increases by 70%.

The new price is calculated with:

```python
up.cost = int(up.cost * 1.7)
```

This makes upgrades progressively more expensive.

### 4. Automatic Coins

The `auto_money()` method runs every second:

```python
self.root.after(1000, self.auto_money)
```

If you have automatic coin upgrades, the game adds coins automatically.

## Project Structure

```text
simple-clicker/
│
├── main.py
└── README.md
```

## OOP

This project uses two classes:

### `Upgrade`

Stores information about an upgrade:

* name
* cost
* power
* automatic/manual type
* level

### `ClickerGame`

Controls the game itself:

* window
* coins
* clicking
* upgrades
* shop
* automatic income
* interface updates

## Future Improvements

Possible improvements for the project:

* Add more upgrades
* Add sound effects
* Add animations
* Add a save system
* Add different currencies
* Add achievements
* Add a better interface
* Add a reset button
* Add statistics
* Add SQLite database support

## Author

Created as a Python learning project.
