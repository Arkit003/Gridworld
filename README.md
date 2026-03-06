## GridWorld Value Iteration

This project is a small Python implementation of a GridWorld Markov Decision Process (MDP) solved with RL Algorithms.

## What It Does

- Uses deterministic actions: `up`, `down`, `left`, `right`
- Uses a step reward of `-1` (can be changed)
- Uses a single terminal state 
- Runs value iteration until convergence 

Current defaults in `Gridworld/main.py`:

- Grid size: `5 x 5`
- Discount factor (`gamma`): `1`
- Terminal state: `(2, 2)`
- Reward: `-1`

## Project Structure

- `Gridworld/main.py`: entry point that builds the environment and runs value iteration
- `Gridworld/enviroment/gridworld.py`: environment dynamics (`step`, bounds checks, terminal logic)
- `Gridworld/enviroment/action.py`: action definitions and movement deltas
- `Gridworld/enviroment/state.py`: state helper class
- `Gridworld/algorithm/value_iteration.py`: value iteration update loop and printing

## Requirements

- Python `3.11+`
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```
or
```bash
uv sync
```

## Run

From the repository root:

```bash
python -m Gridworld.main
```

or:

```bash
python Gridworld/main.py
```

## Value Iteration Update

For each non-terminal state `s`, the algorithm applies:

`V(s) = max_a [ r + gamma * V(s') ]`

where:

- `r` is the immediate reward
- `gamma` is the discount factor
- `s'` is the next state after taking action `a`

## Example Converged V (from current `main.py`)

Running the current setup converges to:

```text
[-4, -3, -2, -3, -4]
[-3, -2, -1, -2, -3]
[-2, -1,  0, -1, -2]
[-3, -2, -1, -2, -3]
[-4, -3, -2, -3, -4]
```

## Algorithms To Add

- Policy Evaluation
- Policy Iteration
