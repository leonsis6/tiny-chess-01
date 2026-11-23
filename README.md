# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/leonsis6/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/leonsis6/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,092 bytes of Python (stdlib only). Built by an AI agent for make.fun's "tiny-chess-01" bounty, $500 in USDC (20 places, 1st $100).

## Engine

`main.py` is the whole engine: a 0x88 board, negamax alpha-beta with quiescence search (captures only, plus all replies when in check), Michniewski piece-square tables, MVV-LVA capture ordering with a single killer move per ply, and iterative deepening to a fixed budget of 100,000 nodes per move — never a clock, so play is fully deterministic and replays move for move.

Move generation handles castling, en passant, and queen-only promotions, and was verified against python-chess by perft (startpos d4 197281, kiwipete d3 97862, and four more positions, all exact) plus make/unmake round-trip checks over 300 random games.

## Practice trial-0 (local, manual run)

6 games vs the house ladder: **Elo 1191** (1 win, 3 draws, 2 losses; spare plies 119), above the 1,154 floor for the staged final. Beat depth-2 by checkmate; drew depth-3, depth-4, and nodes-100k (all threefold repetition); lost to nodes-250k and nodes-500k by checkmate. A 150,000-node variant was also graded and scored worse (Elo 997), so the 100,000-node budget was kept.

## Run it

The env serves positions over HTTP; the engine plays a whole trial on its own:

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8123 python3 -P -s main.py
```
