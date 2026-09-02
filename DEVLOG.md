# Croupier - Development Log

## [2026-08-30] - Initial Setup & Scaffolding

**Done**
- Initialized project using Poetry (`pyproject.toml`).
- Created `src/` layout to isolate domain logic (`models/`), UI, and simulation.
- Set up base architecture for `croupier` Python package.

**Architecture & Decisions**
- **Tech Stack:** `pygame-ce` for UI, `pandas` + `streamlit` + `plotly` for simulation and data visualization.
- **Scope Reduction:** Stripped down casino rules to pure probability. Removed money, betting, splits, and surrender to focus strictly on hit/stand mechanics and dealer thresholds.

---

## [2026-08-31] - Core Domain, Hand Logic & Test Suite

**Done**
- Implemented `Card` using `dataclass` and `Enum`.
- Implemented `Deck` with automatic 52-card generation, shuffling, drawing, and cloning mechanics.
- Implemented `Hand` with dynamic score calculation, tracking `is_bust` and `is_blackjack`.
- Created comprehensive `pytest` suite (`test_card.py`, `test_deck.py`, `test_hand.py`) verifying edge cases like multiple Aces, soft/hard hands, and busts.

**Architecture & Decisions**
- **Dynamic Scoring:** Avoided storing static values. Used `@property` to calculate Blackjack scores dynamically (Face cards = 10, Ace = 11).
- **Decoupling:** Removed `Deck` dependency from `Hand`. The game orchestrator will handle drawing and passing cards via `Hand.add_card()`.
- **Blackjack Strictness:** Defined `is_blackjack` strictly as a 21-point hand composed of exactly two cards.

---

## 2026-09-01 | Game Orchestrator & State Machine Implementation

**Done:**
- Implemented the `Game` orchestrator class in `src/croupier/core/game.py`.
- Defined game lifecycle states using `GameState` and outcomes using `Result`.
- Configured dealer automation rule (`dealer_stand_threshold`).
- Implemented core actions: `start()`, `hit()`, and `stand()`.
- Created and executed the complete unit test suite in `tests/test_game.py`, covering initial deals, player and dealer busts and dealer automation thresholds.

**Decisions:**
- **Decoupled Game Loop:** Maintained `Game` as a passive state machine to seamlessly support both interactive UIs and statistical simulators.
- **Rule Hierarchy:** Prioritized bust evaluations in the referee logic to correctly attribute wins and losses when a participant busts.

---

## [2026-09-02] - Strategy Pattern & Simulation Runner

**Done**
- Designed abstract base class `Strategy` and `Action` Enum in `src/croupier/strats/base.py`.
- Implemented `BasicStrategy` concrete class (threshold-based decision logic at 17).
- Built high-throughput simulation runner `run_simulation()` in `src/croupier/simulation/runner.py` returning structured `pandas.DataFrame` records.
- Added `player_score` property helper to `Game` domain orchestrator.
- Created unit tests verifying strategy decisions, runner output integrity, and DataFrame column schemas in `tests/test_simulation.py`.

**Architecture & Decisions**
- **Inversion of Control:** Injected `Strategy` instances directly into `run_simulation()`, allowing seamless benchmarking of alternative tactics without modifying simulation code.
- **Callable Strategy Interface:** Implemented `__call__` on `Strategy` base class to allow strategy instances to act as functions or class objects interchangeably (e.g., `action = strategy(hand, upcard)`).

**Next up**
- Create CLI/script entry point (`scripts/run_sim.py`) to execute batch simulations and export results to `.csv`.
- Begin exploratory data analysis (EDA) using `pandas` and `plotly`.