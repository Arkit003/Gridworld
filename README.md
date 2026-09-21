# GridWorld

A minimal, NumPy-only GridWorld Markov Decision Process (MDP) in Python, solved with classic dynamic-programming RL algorithms. Built as a learning project — every example prints its value grid after every sweep so you can watch the values propagate.

## What This Repo Contains

| Path | Purpose |
| --- | --- |
| `Gridworld/enviroment/gridworld.py` | Environment dynamics: `step`, bounds checks, terminal logic |
| `Gridworld/enviroment/action.py` | Action definitions and movement deltas |
| `Gridworld/enviroment/state.py` | State helper class |
| `Gridworld/algorithm/value_iteration.py` | Value iteration update loop |
| `Gridworld/algorithm/policy_evaluation.py` | Iterative policy evaluation loop |
| `Gridworld/example_value_iteration.py` | Example entry point for value iteration |
| `Gridworld/example_policy_evaluation.py` | Example entry point for policy evaluation |

## Environment

The grid is `rows x cols` (positions are `(row, col)` tuples), with configurable size, discount factor, terminal state, and reward:

```python
GridWorld(rows, cols, action, discount_factor=1, terminal_state=(0, 0), reward=-1)
```

Semantics:

- **Deterministic actions**: `up (-1,0)`, `down (1,0)`, `left (0,-1)`, `right (0,1)`
- **Reward**: `-1` per step (configurable)
- **Off-grid moves** (bumping a wall): the agent **stays in place but still pays the step reward**
- **Terminal state**: absorbing — the algorithms never update it, so `V(terminal) = 0`, and every transition into it costs the normal step reward on the way in

## Algorithms

### Value iteration

`Gridworld/algorithm/value_iteration.py` — for each non-terminal state `s`:

```
V(s) = max_a [ r + gamma * V(s') ]
```

Sweeps repeat until the largest value change (`delta`) drops below a threshold of `0.001`, printing the grid after each sweep. Returns `(V, number_of_sweeps)`.

Example defaults in `Gridworld/example_value_iteration.py`: 5×5 grid, `gamma = 1`, terminal `(2, 2)`, reward `-1`. This converges in **5 sweeps** to:

```text
[-4, -3, -2, -3, -4]
[-3, -2, -1, -2, -3]
[-2, -1,  0, -1, -2]
[-3, -2, -1, -2, -3]
[-4, -3, -2, -3, -4]
```

i.e. minus the Manhattan distance to the terminal state (with `gamma = 1`, every step costs `-1`, and the shortest path wins under `max`).

### Policy evaluation

`Gridworld/algorithm/policy_evaluation.py` — for each non-terminal state `s`, under a fixed policy `pi`:

```
V(s) = sum_a pi(a|s) * [ r + gamma * V(s') ]
```

Sweeps repeat until `delta` drops below the configured threshold. Updates are in-place (each sweep reads partially updated values), and the grid is printed after each sweep.

Example defaults in `Gridworld/example_policy_evaluation.py`: 4×4 grid, `gamma = 1`, terminal `(0, 0)`, reward `-1`, uniform policy `pi(a|s) = 0.25`, **threshold `1`**.

> **Caveat:** with `gamma = 1` and threshold `1`, the loop stops early (after ~21 sweeps) while values are still far from the true solution — the bottom-right corner prints `-28.85` instead of the converged `-59.43`. Tighten the threshold for accurate values:

| Threshold | Sweeps | `V(3,3)` |
| --- | --- | --- |
| `1` (as shipped) | 21 | `-28.85` |
| `0.001` | 238 | `-59.40` |
| `1e-6` | 454 | `-59.43` (exact) |

For reference, the fully converged values for the uniform random policy (`gamma = 1`, terminal at `(0,0)`) equal minus the expected number of steps to reach the terminal:

```text
[  0.0, -30.0, -45.1, -51.7]
[-30.0, -40.9, -49.7, -54.3]
[-45.1, -49.7, -54.6, -57.4]
[-51.7, -54.3, -57.4, -59.4]
```

## Requirements

- Python `3.11+`
- NumPy

Install dependencies:

```bash
uv sync
```

or:

```bash
pip install -r requirements.txt
```

## Run

From the repository root:

```bash
python -m Gridworld.example_value_iteration
```

```bash
python -m Gridworld.example_policy_evaluation
```

Note: run these as **modules** from the repo root. Running the files directly (e.g. `python Gridworld/example_value_iteration.py`) fails because the imports use absolute `Gridworld.*` package paths.

## Algorithms To Add

- Policy Iteration
