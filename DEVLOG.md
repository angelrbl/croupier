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

**Next Steps**
- Design the `Game` class in `core/game.py` to orchestrate turns, player decisions (Hit/Stand), and configurable dealer rules (e.g., stand on 17).