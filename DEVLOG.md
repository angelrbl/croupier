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