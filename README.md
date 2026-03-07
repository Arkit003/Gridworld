## GridWorld RL Algorithms

This project is a small Python implementation of a GridWorld Markov Decision Process (MDP) solved with dynamic programming RL algorithms.

## What It Does

- Uses deterministic actions: `up`, `down`, `left`, `right`
- Uses a step reward of `-1` (can be changed)
- Uses a single terminal state 
- Runs value iteration until convergence
- Runs iterative policy evaluation for a fixed policy

Current value iteration defaults in `Gridworld/example_value_iteration.py`:

- Grid size: `5 x 5`
- Discount factor (`gamma`): `1`
- Terminal state: `(2, 2)`
- Reward: `-1`

## Project Structure

- `Gridworld/example_value_iteration.py`: example entry point for value iteration
- `Gridworld/example_policy_evaluation.py`: example entry point for policy evaluation
- `Gridworld/enviroment/gridworld.py`: environment dynamics (`step`, bounds checks, terminal logic)
- `Gridworld/enviroment/action.py`: action definitions and movement deltas
- `Gridworld/enviroment/state.py`: state helper class
- `Gridworld/algorithm/value_iteration.py`: value iteration update loop and printing
- `Gridworld/algorithm/policy_evaluation.py`: iterative policy evaluation loop and printing

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
python -m Gridworld.example_value_iteration
```

or:

```bash
python Gridworld/example_value_iteration.py
```

For policy evaluation:

```bash
python -m Gridworld.example_policy_evaluation
```

or:

```bash
python Gridworld/example_policy_evaluation.py
```

## Value Iteration Update

For each non-terminal state `s`, the algorithm applies:

`V(s) = max_a [ r + gamma * V(s') ]`

where:

- `r` is the immediate reward
- `gamma` is the discount factor
- `s'` is the next state after taking action `a`

## Example Converged V (from current `example_value_iteration.py`)

Running the current setup converges to:

```text
[-4, -3, -2, -3, -4]
[-3, -2, -1, -2, -3]
[-2, -1,  0, -1, -2]
[-3, -2, -1, -2, -3]
[-4, -3, -2, -3, -4]
```

## Policy Evaluation Update

For each non-terminal state `s`, policy evaluation applies:

`V(s) = sum_a pi(a|s) * [ r + gamma * V(s') ]`

where:

- `pi(a|s)` is the probability of action `a` in state `s`
- `r` is the immediate reward
- `gamma` is the discount factor
- `s'` is the next state after action `a`

In `example_policy_evaluation.py`, the policy is currently uniform (`0.25` for each action).

## Algorithms To Add

- Policy Iteration
