"""
US equity data acquisition using yfinance and WRDS.
"""

import polars as pl
import yfinance as yf
from typing import List, Optional
from datetime import datetime


def get_sp500_tickers() -> List[str]:
    """
    Fetch current S&P 500 constituent tickers.
    
    Returns:
        List of ticker symbols
    """
    # TODO: Implement (can scrape from Wikipedia or use a static list)
    pass


def download_price_data(
    tickers: List[str],
    start_date: str,
    end_date: str
) -> pl.DataFrame:
    """
    Download historical price data using yfinance.
    
    Args:
        tickers: List of stock tickers
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        
    Returns:
        Polars DataFrame with OHLCV data
    """
    # TODO: Implement using yfinance
    pass


def get_fundamental_data(tickers: List[str]) -> pl.DataFrame:
    """
    Fetch fundamental data (market cap, book value, etc.).
    
    Args:
        tickers: List of stock tickers
        
    Returns:
        DataFrame with fundamental metrics
    """
    # TODO: Implement
    pass