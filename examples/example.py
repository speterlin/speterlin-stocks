# IMPORT script packages like in github.com/speterlin/quant-trading README.md#Another Python script for Stocks

import pandas as pd

start_day = datetime.strptime('2024_01_09 13:00:00', '%Y_%m_%d %H:%M:%S')
end_day = datetime.strptime('2026_01_09 13:00:00', '%Y_%m_%d %H:%M:%S')

# Make sure to double check 'type', 'up_down_move', 'days', 'start_day' of portfolio['constants']
# Zacks Rank only from 2020-04-24->2022-12-21, 2023-10-31->12-28 # FMP Rank from 2023-12-08->present # 'tr', 'zr' and remove up_down_move, 'tr' have to start on '2020-05-08', first day with tradingview ratings # 'up_down_move': 100, 'days': 15, 'sl': -0.15, 'tsl_a': 0.05, 'tsl_p': -0.0125, 'usd_invest': 1000, # portfolio_til100opbcpccepsf
portfolio_fmpr_test = {
    'constants': {'type': 'fmpr', 'up_down_move': 2, 'days': 10, 'sl': -0.15, 'tsl_a': 0.05, 'tsl_p': -0.0125, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_rr_test = {
    'constants': {'type': 'rr', 'up_down_move': 10, 'days': 10, 'sl': -0.15, 'tsl_a': 0.05, 'tsl_p': -0.0125, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
# LONG BACKTESTING TIME on tilupccu type needs refactoring
portfolio_tilupccu_test = {
    'constants': {'type': 'tilupccu', 'up_down_move': [1,-1], 'days': 2, 'sl': -0.15, 'tsl_a': 0.05, 'tsl_p': -0.0125, 'usd_invest': 2000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
# LONG BACKTESTING TIME on mmtv type needs refactoring
portfolio_mmtv_test = {
    'constants': {'type': 'mmtv', 'up_down_move': float("NaN"), 'days': 10, 'sl': -0.2, 'tsl_a': 0.2, 'tsl_p': -0.05, 'usd_invest': 2000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_random_sp500_test = {
    'constants': {'type': 'random_sp500', 'up_down_move': float("NaN"), 'days': 30, 'sl': -1, 'tsl_a': 10, 'tsl_p': -5, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_mm_test = {
    'constants': {'type': 'mm', 'up_down_move': float("NaN"), 'days': 365, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_airs_test = {
    'constants': {'type': 'airs', 'up_down_move': [8,4,'Financial Services'], 'days': 0, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_tngaia_test = {
    'constants': {'type': 'tngaia', 'up_down_move': [8,4], 'days': 0, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_senate_trading_test = {
    'constants': {'type': 'senate_trading', 'up_down_move': 5, 'days': 30, 'sl': -0.2, 'tsl_a': 0.2, 'tsl_p': -0.05, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
# NO BACKTESTING on sma_mm type atm
portfolio_sma_mm_test = {
    'constants': {'type': 'sma_mm', 'up_down_move': 'price-200D', 'days': 0, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_sma_mm_test_2 = {
    'constants': {'type': 'sma_mm', 'up_down_move': 'price-200D-sp500', 'days': 0, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}
portfolio_sma_mm_test_3 = {
    'constants': {'type': 'sma_mm', 'up_down_move': '5D-8D-13D', 'days': 0, 'sl': -0.3, 'tsl_a': 0.5, 'tsl_p': -0.2, 'usd_invest': 1000, 'usd_invest_min': 100, 'buy_date_gtrends_15d': False, 'end_day_open_positions_gtrends_15d': False, 'end_day_open_positions_fmp_24h_vol': False, 'start_balance': {'usd': 10000}, 'start_day': start_day.strftime('%Y-%m-%d')},
    'balance': {'usd': 10000}, # alpaca only offers margin trading so if deposit $10k actually worth $20k (meaning if it shows $10k it's actually $5k deposited)
    'max_value': {'usd': float("NaN")}, # *2 since margin trading with Alpaca
    'open': pd.DataFrame(columns=['position', 'buy_date', 'buy_price', 'balance', 'current_date', 'current_price', 'current_roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_armed', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'current_date': 'datetime64[ns]', 'current_price': 'float64', 'current_roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_armed': 'bool', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'}),
    'sold': pd.DataFrame(columns=['ticker', 'position', 'buy_date', 'buy_price', 'balance', 'sell_date', 'sell_price', 'roi', 'fmp_24h_vol', 'gtrends_15d', 'rank_rise_d', 'tsl_max_price', 'trade_notes', 'other_notes']).astype({'ticker': 'object', 'position': 'object', 'buy_date': 'datetime64[ns]', 'buy_price': 'float64', 'balance': 'float64', 'sell_date': 'datetime64[ns]', 'sell_price': 'float64', 'roi': 'float64', 'fmp_24h_vol': 'float64', 'gtrends_15d': 'float64', 'rank_rise_d': 'float64', 'tsl_max_price': 'float64', 'trade_notes': 'object', 'other_notes': 'object'})
}

# DECLARE tickers_with_stock_splits, tickers_to_avoid (and senate_timestamps_and_tickers_inflows_and_outflows if running that algo) and BACKTEST a single algorithm with different parameters on a time period like in github.com/speterlin/quant-trading README.md#Backtesting in Python virtual environment shell (or different algorithms with set parameters like below), OR BACKTEST a single algorithm with set parameters on a time period like below
paper_trading, back_testing, add_pauses_to_avoid_unsolved_error = True, True, {'engaged': True, 'time': 60, 'days': 40} # days naming reflects correct logic for all portfolio types except random_sp500 and senate_trading since back_testing increments are stop_day = stop_day + timedelta(days=DAYS) vs. stop_day = stop_day + timedelta(days=1), also doesn’t take into account weekends / holidays therefore 60 days ~ 60/5 ~ 12 weeks ~3 months vs. expected 2 months # {'engaged': True, 'time': 60, 'days': 30} # random_sp500 and senate_trading: {'engaged': True, 'time': 60, 'days': 5} # {'engaged': False, 'time': 420, 'days': 20}
portfolios = {
    'zr': portfolio_zr_test,
    'rr': portfolio_rr_test,
    'tilupccu': portfolio_tilupccu_test,
    'mmtv': portfolio_mmtv_test,
    'random_sp500': portfolio_random_sp500_test,
    'mm': portfolio_mm_test,
    'airs': portfolio_airs_test,
    'tngaia': portfolio_tngaia_test,
    'senate_trading': portfolio_senate_trading_test
    #'sma_mm': {portfolio_sma_mm_test['constants']['up_down_move']: portfolio_sma_mm_test, portfolio_sma_mm_test_2['constants']['up_down_move']: portfolio_sma_mm_test_2, portfolio_sma_mm_test_3['constants']['up_down_move']: portfolio_sma_mm_test_3}
}

# DATA FMP Issues between ticker_data and ticker_data_granular
# tickers_with_stock_splits = {'apply_corrections': False, 'only_last_split': False, 'stock_splits': pd.DataFrame()}
df_tickers_with_stock_splits = stocks.get_tickers_with_stock_splits_fmp(start_day=start_day)
# tickers_to_avoid_splitting = {ticker: 'stock split already reflected on FMP' for ticker in ['POL','EXPR','DBGI','LTRY','SNMP','IDEX','CRKN','AGRI','REE','AREB','SOND','BSFC','AQB','ISPO','WATT','XXII','KXIN','NCMI','UXIN','DXF','SHPW','ALPP','FRSX','CRGE','MIMO','DMAQR','TANH','JL', 'MMAT','GTI','KAVL','GURE','NCL','AEVA','LICN']} # 'NIVF' # {'WLL': 'stock split not updated on yf', 'MYT': 'stock split not updated on yf'} # already covered in update_portfolio_buy_and_sell_tickers() add back if Yahoo Finance decides to update (hourly price data to match past daily price data) some tickers and not others # maybe refactor and add PDS: listed as PD:CA on Fidelity, split on November 11/12/2020, same day stock rose 20x
tickers_with_stock_splits = {'apply_corrections': True, 'only_last_split': True, 'avoid_splitting': {}, 'stock_splits': df_tickers_with_stock_splits}
# tickers_with_stock_splits = {'apply_corrections': True, 'only_last_split': True, 'avoid_splitting': tickers_to_avoid_splitting, 'stock_splits': df_tickers_with_stock_splits}
# tickers_with_stock_splits = {'apply_corrections': True, 'only_last_split': False, 'stock_splits': df_tickers_with_stock_splits}

df_tickers_end_day = stocks.get_saved_tickers_data(date=end_day.strftime('%Y-%m-%d'))
tickers_to_avoid = stocks.get_tickers_to_avoid(df_tickers_end_day, end_day)
# tickers_to_avoid[''] = {'reason': 'stock information not on FMP', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')}
# NOT a REPEAT ISSUE
# tickers_to_avoid = {**{ticker: {'reason': 'stock granular market data (issue with date column) not on FMP', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')} for ticker in [
#     'ATMC', # fmpr backtest issue
# ]}, **tickers_to_avoid}
# IF ALLOWING WARRANTS
# tickers_to_avoid = {**{ticker: {'reason': 'stock 1d and granular market data (issue with date column) not on FMP', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')} for ticker in [
#     'BLEUW', # tilupccu backtest issue 2024-11-21->11-22
#     'ONYXW' # tilupccu backtest issue 2024-10-09->10-28
# ]}, **tickers_to_avoid}
# tickers_to_avoid = {**{ticker: {'reason': 'price +/- too unrealistic', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')} for ticker in [
#     'RMGCW' # 20x price jump in tilupccu backtest from 2024-04-16->19 too unrealistic
# ]}, **tickers_to_avoid}
# this is in tilupccu so prob ok
# tickers_to_avoid = {**{ticker: {'reason': 'stock 1d market data not on FMP', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')} for ticker in [
#     'GCMGW', # tilupccu backtest issue 2025-11-17->11-18
# ]}, **tickers_to_avoid}
# only_last_split RESOLVES ERROR
# tickers_to_avoid = {**{ticker: {'reason': 'stock split not updated on FMP', 'good_after_date': datetime.strptime('2029_06_06 13:00:00', '%Y_%m_%d %H:%M:%S')} for ticker in [
#     'KNW', # tilupccu backtest issue 2025-01-29->03-05
#     'VCIG', # tilupccu backtest issue 2025-03-12->03-14,03-27,08-29,07-29
#     'NITO', # tilupccu backtest issue 2025-05-19->05-20,05-21,09-19,05-08
#     'NIVF' # tilupccu backtest issue 2025-03-04->05
# ]}, **tickers_to_avoid}


# RUN portfolios
for portfolio_name, portfolio in portfolios.items():
    # if portfolio_name == 'sma_mm':
    #     for portfolio_x_name, portfolio_x in portfolio.items(): # portfolio is a list
    #         portfolio_x = stocks.run_portfolio(portfolio=portfolio_x, start_day=start_day, end_day=end_day, paper_trading=paper_trading, back_testing=back_testing, add_pauses_to_avoid_unsolved_error=add_pauses_to_avoid_unsolved_error, tickers_with_stock_splits=tickers_with_stock_splits, tickers_to_avoid=tickers_to_avoid)
    #         portfolios[portfolio_name][portfolio_x_name] = portfolio_x
    # else:
    portfolio = stocks.run_portfolio(portfolio=portfolio, start_day=start_day, end_day=end_day, paper_trading=paper_trading, back_testing=back_testing, add_pauses_to_avoid_unsolved_error=add_pauses_to_avoid_unsolved_error, tickers_with_stock_splits=tickers_with_stock_splits, tickers_to_avoid=tickers_to_avoid)
    portfolios[portfolio_name] = portfolio

# CHECK ROIs of portfolios
for portfolio_name, portfolio in portfolios.items():
    # if portfolio_name == 'sma_mm':
    #     for portfolio_x_name, portfolio_x in portfolio.items():
    #         portfolio_usd_value = portfolio_x['balance']['usd']
    #         for ticker in portfolio_x['open'].index:
    #             portfolio_usd_value += portfolio_x['open'].loc[ticker, 'current_price']*portfolio_x['open'].loc[ticker, 'balance']
    #         portfolio_usd_value_growth = (portfolio_usd_value - portfolio_x['constants']['start_balance']['usd']) / portfolio_x['constants']['start_balance']['usd'] # float(portfolio_name.split("_")[-2])
    #         print(portfolio_name + " algo: " + str(portfolio_x_name) + ", USD Value: " + str(portfolio_usd_value) + ", USD Value Growth: " + str(portfolio_usd_value_growth))
    # else:
    portfolio_usd_value = portfolio['balance']['usd']
    for ticker in portfolio['open'].index:
        portfolio_usd_value += portfolio['open'].loc[ticker, 'current_price']*portfolio['open'].loc[ticker, 'balance']
    portfolio_usd_value_growth = (portfolio_usd_value - portfolio['constants']['start_balance']['usd']) / portfolio['constants']['start_balance']['usd'] # float(portfolio_name.split("_")[-2])
    print(portfolio_name + ", USD Value: " + str(portfolio_usd_value) + ", USD Value Growth: " + str(portfolio_usd_value_growth))

# RUN single portfolio
portfolio_fmpr_test = stocks.run_portfolio(portfolio=portfolio_fmpr_test, start_day=start_day, end_day=end_day, paper_trading=paper_trading, back_testing=back_testing, add_pauses_to_avoid_unsolved_error=add_pauses_to_avoid_unsolved_error, tickers_with_stock_splits=tickers_with_stock_splits, tickers_to_avoid=tickers_to_avoid)

# CHECK ROI of single portfolio
portfolio_usd_value = portfolio_fmpr_test['balance']['usd']
for ticker in portfolio_fmpr_test['open'].index:
    portfolio_usd_value += portfolio_fmpr_test['open'].loc[ticker, 'current_price']*portfolio_fmpr_test['open'].loc[ticker, 'balance']

portfolio_usd_value_growth = (portfolio_usd_value - portfolio_fmpr_test['constants']['start_balance']['usd']) / portfolio_fmpr_test['constants']['start_balance']['usd']

# INSPECT OUTCOME of single portfolio
portfolio_fmpr_test['sold'].sort_values('roi', inplace=False, ascending=False)[['ticker', 'buy_date', 'buy_price', 'balance', 'rank_rise_d', 'sell_date', 'sell_price', 'roi', 'other_notes']]
portfolio_fmpr_test['open'].sort_values('current_roi', inplace=False, ascending=False)[['buy_date', 'buy_price', 'balance', 'rank_rise_d', 'current_date', 'current_price', 'current_roi', 'other_notes']]
