<!---
# Outline
1. Wanted to investigate the strat
2. Results with annualized vol
3. Breakdown of IID assumption for annualized vol
4. Autocorrelation study
5. New results
6. Look into slippage
7. Possible reasons for sharp shortfall
   - Universe selection
-->

For years, I've been an avid listener of Corey Hoffstein's podcast _[Flirting with Models](https://podcasts.apple.com/us/podcast/flirting-with-models/id1402620531)_. Corey finds fascinating practitioners 
from across the quantitative finance industry and brings them on for engaging and deeply technical interviews. 

[A recent episode with Scott Phillips](https://podcasts.apple.com/us/podcast/scott-phillips-finding-ugly-edges-in-crypto-markets-s7e15/id1402620531?i=1000697301707), a well-known independent crypto trader, struck me as particularly interesting. Scott goes into great detail about his philosophy on finding and exploiting edges in markets. After 
trying to trade in the traditional markets, Scott realized that, as an independent trader, he couldn't compete with the large, well-funded, well-staffed firms that dominate traditional finance. He sought "an easier 
poker table to sit at" and found a place in crypto.

Scott's strategy in the crypto markets focuses on trend following, and started with a bare-bones published trend following system. Although he's upgraded his system to a more complex vol-targeted 
CTA-style trend system, Scott points out that if no trend is present in a market, "no amount of math camp will fix it." On the other hand, he points out that if trend is present in crypto, "those trends are probably 
going to be so strong that you can trade [them] with a potato."

As an example, Scott gives the following rules for a trading system he says is 1.4 Sharpe:
- Screen for the list of coins that have made a 20-day high within the last 5 days.
- Construct an equal-weight long portfolio from this filtered list.

Upon hearing this, I immediately wanted to see if I could recreate this result for myself. I translated his high level strategy rules into the following initial implementation. Later I'll discuss the gaps I filled in 
and how they may be impacting my results.

While my initial results don't match Scott's, I intend to walk through my thoughts here as I improve my system and backtest, using Scott's result as a truth source to reproduce. 

## :green[Preliminary Setup]

1. Universe Selection
   - Start with all pairs quoted on Coinbase since 1/1/2020
     - Coinbase was chosen arbitrarily as I already had an account to acquire data.
   - For the sake of a common numeraire, narrow down to pairs quoted in USDC.
2. Data Processing
   - Pull daily price data from Coinbase using their API and Python SDK.
   - Daily data for pairs which have not yet been listed or have been delisted comes in as NaNs. Logic is added to ignore them in signal construction to avoid survivorship bias.
3. Feature Construction
   - The rolling 5-day and 20-day highs for each pair are calculated.
   - A Boolean feature is generated: 
     - True if 5-day high equals 20-day high, False otherwise. 
     - True indicates a buy.
     - False indicates a sell.
     - If a NaN is included anywhere in the rolling data, the feature value is False.
4. Portfolio Construction
   - For each period, a target equal-weight portfolio is constructed of all pairs which are indicated as buy.
   - Exposure for each pair is either bought or sold to match the target portfolio perfectly during each period.
5. Execution
   - Initially, daily execution is tested. Later different execution periods are studied.
   - It is assumed that trading occurs at the open price for each period.
   - Slippage and trading costs are neglected in this initial test to focus on signal quality.
6. Evaluation
   - An equity curve and daily return stream is computed using data starting in January 2020.
   - A risk-free rate of 4.5% is assumed.
   - Because crypto trades continuously, 365 trading days are assumed.
   - Mean returns, volatility, and Sharpe ratio are calculated on a rolling 30-day basis. All values are annualized.

## :green[Preliminary Results]
The preliminary strategy above produces the following results: