# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/deelyy78/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/deelyy78/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,086 bytes of Python (0x88 board, alpha-beta search with a
transposition table, quiescence search and piece-square tables) that plays
make.fun's tiny-chess-01 gauntlet through the env at MAKEFUN_ENV_URL. The
search is fully deterministic: it counts nodes, never reads a clock.
Iterative deepening runs each depth on its own node budget and keeps the
last depth that finished; the transposition table stores bound flags
(exact / lower / upper) so cutoffs never corrupt the search. Kingside
castling is generated when the FEN rights allow it, with the rook moved
alongside the king; knights and bishops share one piece-square table.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

Locally, importing the module without MAKEFUN_ENV_URL set just loads the
engine (BM(fen) returns the best move for a position).
