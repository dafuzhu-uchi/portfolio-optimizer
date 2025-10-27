# Portfolio Optimizer

A quantitative portfolio weight optimization system for US equities with multi-factor risk models.

## Features

- Factor exposure calculation (size, value, momentum, quality, volatility)
- Multi-factor risk model with covariance estimation
- Portfolio optimization with multiple objective functions
- Constraint handling (sector limits, turnover, position sizing)
- Backtesting framework for US equity portfolios

## Tech Stack

- Python 3.11+
- Polars (data processing)
- MongoDB (time-series storage)
- yfinance / WRDS (US equity data)
- SciPy (optimization)

## Factor Model

Implements style factors inspired by academic research:
- **Size**: Market capitalization
- **Value**: Book-to-market, earnings yield
- **Momentum**: 12-month return (excluding last month)
- **Quality**: ROE, profit margin
- **Volatility**: Realized volatility, beta
- **Liquidity**: Trading volume, turnover

Sector factors based on GICS classification.

## Project Structure
```
src/
├── data/          # Data acquisition (yfinance, WRDS)
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

🚧 Work in progress - building US equity multi-factor optimizer