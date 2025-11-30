# speterlin-stocks

A Python package for a suite of quant-trading opportunities in stocks with API integration: Alpaca brokerage for storing USD assets and margin trading (2x) on exchanges NYSE & NASDAQ, Financial Modeling Prep (FMP) & Google Trends & Yahoo Finance & Google Finance & ExchangeRate & MarketBeat & CrunchBase for data collection, OpenAI & Google Gemini-Pro for AI analysis.

Please see [quant-trading](https://github.com/speterlin/quant-trading) for implementation. Make sure to install package like this (with python>=3.12 and latest pip) in your environment or (recommended) virtual environment:
```python
pip install speterlin-stocks
```
And then import package like this:
```python
import speterlin_stocks.module1 as stocks
```

For the following calls set up your Python virtual environment shell and import packages like in [quant-trading#Python script for Stocks](https://github.com/speterlin/quant-trading?tab=readme-ov-file#python-script-for-stocks-programsstocksstocks_alpaca_your_usernamepy)

## Get and analyze your saved Portfolio

```python
portfolio = stocks.get_saved_portfolio_backup("portfolio_rr_50_-50_20_-0.2_0.2_-0.05_2000_100_True_False_False_{'usd': 10000}_2024-12-01_to_" + datetime.now().strftime('%Y-%m-%d'))

# View open positions in two rows
print(str(portfolio['open'].drop(['fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes'], axis=1)) + "\n" + str(portfolio['open'].drop(['position', 'buy_date', 'buy_price', 'balance', 'current_date',\
'current_price', 'current_roi'], axis=1)))

# View sold positions
portfolio['sold'].tail(40).drop(['fmp_24h_vol', 'rank_rise_d', 'tsl_max_price', 'gtrends_15d'], axis=1)
```

## Check Assets

[quant-trading#Checking assets value in Python virtual environment shell](https://github.com/speterlin/quant-trading?tab=readme-ov-file#checking-assets-value-in-python-virtual-environment-shell-calling-python-and-then-entering-python-virtual-environment-shell-as-opposed-to-running-a-script-with-python-directory_pathfile_namepy-after-manually-line-by-line-importing-necessary-packages-listed-in-appropriate-script-like-python-script-for-stocks-programsstocksstocks_alpaca_your_usernamepy-to-properly-set-up-that-python-environment)

## Market calls (in Python virtual environment shell not within script)

```python
last_trade_data = stocks._fetch_data(stocks.alpaca_api.get_latest_trade, params={'symbol': ticker}, error_str=" - No last trade from Alpaca for ticker: " + ticker + " on: " + str(datetime.now()), empty_data = {})
price, timestamp = last_trade_data.price, last_trade_data.timestamp
```

## USA Holidays

```python
from pandas.tseries.holiday import USFederalHolidayCalendar # import holidays - add back if works
usa_cal = USFederalHolidayCalendar()

from pytz import timezone

eastern = timezone('US/Eastern')

usa_holidays = usa_cal.holidays(start=datetime.now(eastern).replace(month=1, day=1).strftime('%Y-%m-%d'), end=datetime.now(eastern).replace(month=12, day=31).strftime('%Y-%m-%d')).to_pydatetime()
```

## Get and save todays FMP data

Single ticker detailed data:
```python
ticker='GOOGL'
ticker_data_detailed = stocks._fetch_data(stocks.get_ticker_data_detailed_fmp, params={'ticker': ticker}, error_str=" - No ticker data detailed FMP for ticker: " + ticker + " on: " + str(datetime.now()), empty_data={})
```

All of Alpaca's USA tickers (takes roughly 2-3 hours to save):
```python
todays_date = datetime.now()
stocks.save_usa_alpaca_tickers_fmp_data(date=todays_date.strftime('%Y-%m-%d'))
```

## Retrieve past saved FMP data

```python
df_tickers_2025_11_17 = stocks.get_saved_tickers_data(date='2025-11-17')
# View the 48 saved data points on GOOGL
df_tickers_2025_11_17.loc['GOOGL']
```

## Send message to your Phone via Twilio

```python
twilio_message = stocks._fetch_data(stocks.twilio_client.messages.create, params={'to': twilio_phone_to, 'from_': twilio_phone_from, 'body': "Q Trading @stocks #" + stocks.portfolio_account + ": running on " + str(datetime.now()) + " :)"}, error_str=" - Twilio msg error to: " + twilio_phone_to + " on: " + str(datetime.now()), empty_data=None)
```
