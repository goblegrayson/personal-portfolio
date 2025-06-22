

The preliminary strategy produces a highly volatile equity curve, consistently running near 100 vol from 2020 through 2022, and around 50 vol onwards. At one point, the initial equity is up over 15x, but after the 
Bitcoin
crash in mid 2021, volatility drag becomes evident, and the equity dwindles to ~20% of initial capital. Overall, the strategy delivers a consistently negative Sharpe ratio. Additionally, while the analysis 
does not consider trading costs or slippage, these would degrade performance further, especially with daily execution. 

Some potential explanations for the 
underperformance of this implementation are detailed below.

#### :green[Universe Composition]
During universe selection, I only select pairs trading on Coinbase. Additionally, I narrow down the pairs trading on Coinbase to only those quoted in USDC. Due to the nature of being listed on a major 
  centralized exchange (CEX), these tokens are significantly more liquid than other non-listed tokens, and likely have already exhibited significant upward momentum. The increase in market participation likely 
leads to erosion of edge and damped trends versus tokens only traded in smaller, less liquid, decentralized exchanges (DEXs). I suspect that Scott's analysis includes DEXs as well as more CEXs. I don't currently have 
the data to study this hypothesis further, but I would like to look into this further down the line.

#### :green[Execution Frequency]
I suspect another contributing factor in the degraded performance of this implementation is my choice to use daily execution. Practically, this results in an instant stop-loss that is limiting my 
exposure to the underlying risk premium, and is whip-sawing the strategy into repeatedly buying high on the 20-day high and selling low on anything less than the 20-day high. I hypothesize that a longer execution 
window will naturally damp this whip-saw and lead to improved performance. 

Next, I'll complete a sensitivity study for execution window. For now, to be continued!