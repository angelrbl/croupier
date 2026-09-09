# Croupier

**A Blackjack engine, strategy simulator, and stats dashboard.**

Croupier strips Blackjack down to its core mechanic — deal, hit, or stand — so it can simulate hundreds of thousands of hands, compare playing strategies, and analyze the outcomes with real statistics. There's no money, betting, splitting, or surrendering: just probability, a clean layered codebase, and a full test suite.

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Table of contents

- [Features](#features)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Game rules implemented](#game-rules-implemented)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)

---

## Features

- **Pure domain engine** — `Card`, `Deck`, and `Hand` with dynamic score calculation, including automatic soft/hard Ace handling.
- **Decoupled state machine** — `Game` drives a hand through `PLAYER_TURN` → `DEALER_TURN` → `GAME_ENDED` without knowing anything about UI or simulation, so it can be reused anywhere.
- **Pluggable strategies (Strategy pattern)** — every `Strategy` is callable (`strategy(hand, upcard)`), so new tactics can be injected and benchmarked without touching the simulation code.
- **High-throughput simulator** — `run_simulation()` plays thousands of hands and returns a tidy `pandas.DataFrame`, ready for analysis.
- **Batch simulation CLI** built with `click`, with configurable options and CSV export.
- **Interactive dashboard** in Streamlit + Plotly: results distribution, bust rate, and a win-rate heatmap by initial hand vs. dealer upcard, with support for importing your own CSVs.

## Tech stack

| Category | Technology |
|---|---|
| Language | Python 3.11+ |
| Dependency manager | [Poetry](https://python-poetry.org/) |
| Data handling | [Pandas](https://pandas.pydata.org/) |
| CLI framework | [Click](https://click.palletsprojects.com/) |
| Dashboard | [Streamlit](https://streamlit.io/) |
| Charts | [Plotly](https://plotly.com/python/) |
| EDA | Jupyter, nbformat |
| Testing | [Pytest](https://docs.pytest.org/) |
| Planned UI | [pygame-ce](https://pyga.me/) *(declared dependency, not yet implemented)* |

## Project structure

```
croupier/
├── default_data/
│   └── simulation_results.csv   # Preloaded dataset (~500k hands with BasicStrategy)
├── src/
│   └── croupier/
│       ├── core/
│       │   └── game.py          # Game, GameState, Result
│       ├── models/
│       │   ├── card.py          # Card, Rank, Suit
│       │   ├── deck.py          # Deck
│       │   └── hand.py          # Hand
│       ├── strats/
│       │   ├── base.py          # Strategy (ABC), Action
│       │   └── basic.py         # BasicStrategy
│       ├── simulation/
│       │   └── runner.py        # run_simulation()
│       ├── scripts/
│       │   └── run_sim.py       # Batch simulation CLI
│       └── ui/
│           └── app.py           # Interactive dashboard (Streamlit + Plotly)
├── tests/
│   ├── core/test_game.py
│   ├── models/test_card.py
│   ├── models/test_deck.py
│   ├── models/test_hand.py
│   └── simulation/test_runner.py
├── DEVLOG.md                    # Development log & design decisions
├── pyproject.toml
└── poetry.lock
```

## Game rules implemented

| Rule | Detail |
|---|---|
| Deck | Standard 52-card deck, no jokers. `Deck` supports shuffling, drawing, and cloning. |
| Scoring | Face cards (`J`, `Q`, `K`) are worth 10. Aces are worth 11 and automatically drop to 1 while the hand is over 21. |
| Blackjack | Exactly 21 points on the first two cards dealt. |
| Dealer | Draws automatically until reaching `dealer_stand_threshold` (17 by default, configurable per game). |
| Out of scope | No money, betting, `split`, or `surrender` — the project deliberately focuses on the `hit`/`stand` mechanic (see [`DEVLOG.md`](./DEVLOG.md)). |

## Installation

### Prerequisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/angelrbl/croupier.git
   cd croupier
   ```

2. Install the dependencies:

   ```bash
   poetry install
   ```

## Usage

### Batch simulation (CLI)

Simulate thousands of hands with a strategy and export the results to CSV:

```bash
poetry run python src/croupier/scripts/run_sim.py --iterations 500000 --dealer-threshold 17 --output data/simulation_results.csv
```

| Option | Alias | Default | Description |
|---|---|---|---|
| `--iterations` | `-i` | `10000` | Number of hands to simulate |
| `--dealer-threshold` | `-t` | `17` | Score at which the dealer stops hitting |
| `--output` | `-o` | `data/simulation_results.csv` | Path to save the output CSV |

### Interactive dashboard (Streamlit)

```bash
poetry run streamlit run src/croupier/ui/app.py
```

The dashboard loads `default_data/simulation_results.csv` by default and lets you:

- Pick a strategy, iteration count, and dealer threshold from the sidebar.
- Run a fresh simulation on demand (results are cached).
- Import your own simulation results as a CSV.
- View the results distribution (win/loss/draw), the bust rate, and a heatmap of win rate by initial hand vs. dealer upcard.
- Download the data currently on screen.

## Roadmap

- [x] Core Blackjack engine (cards, deck, hand, dealer state machine)
- [x] Pluggable Strategy pattern with a baseline `BasicStrategy`
- [x] High-throughput simulation runner + batch CLI
- [x] Interactive Streamlit + Plotly dashboard
- [ ] Exploratory data analysis notebooks on simulation results
- [ ] Adaptive strategy derived from EDA findings

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Built by <a href="https://github.com/angelrbl">@angelrbl</a>
</div>
