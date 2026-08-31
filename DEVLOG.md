# DevLog

## 2026-08-30 | Initial setup & scaffolding

**Done:**
- Initialized project using Poetry (`pyproject.toml`).
- Defined stack: `pygame-ce` (UI), `pandas` + `streamlit` + `plotly` (simulation & dashboard).
- Created `src/` layout to isolate logic, UI, and simulation.
- Placed core data structures (`Card`, `Deck`, `Hand`) inside `src/croupier/models/`.

**Decisions:**
- Stripped down casino rules: no money, betting, splits, or surrender. The focus is strictly on hit/stand mechanics and dealer thresholds for statistical analysis.

**Next up:**
- Implement `Card`, `Deck`, and `Hand` classes in `models/`.

## 2026-08-31 | Core Models Implementation & Testing

**Done:**

- Implemented `Card` class using `dataclass` and `Enum`.
- Implemented `Deck` class with automatic 52-card generation, shuffling, and drawing mechanics.
- Set up and structured the testing suite (`test_card.py` y `test_deck.py`) using `pytest`.

**Decisions:**

- **Card Logic:** Avoided storing a static `_value` attribute. Instead, used a `@property` to dynamically calculate the Blackjack score based on the rank (handling face cards as 10 and Aces as 11).

**Next up:**

- Implement the `Hand` class, focusing heavily on the logic to calculate total score and manage the dual-value nature of the Ace (1 vs 11).
- Write and execute unit tests for `Hand`.