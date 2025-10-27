# Portfolio Optimizer

A quantitative portfolio weight optimization system implementing Barra-style risk models.

## Features

- Factor exposure calculation for A-share equities
- Multi-factor risk model with covariance estimation
- Portfolio optimization with multiple objective functions
- Constraint handling (sector limits, turnover, position sizing)
- Backtesting framework

## Tech Stack

- Python 3.12+
- Polars (data processing)
- MongoDB (time-series storage)
- AkShare (A-shares data)
- SciPy (optimization)

## Project Structure
```
src/
├── data/          # Data acquisition and storage
├── factors/       # Factor calculation modules
├── risk_model/    # Covariance and risk decomposition
├── optimizer/     # Portfolio optimization
├── backtest/      # Backtesting framework
└── utils/         # Helper functions
```

## Setup
```bash
uv sync
```

## Development Status

🚧 Work in progress