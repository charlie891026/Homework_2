# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).
> Solution
> 
> ![image](https://github.com/charlie891026/Homework_2/assets/113324433/7eded9cd-88fc-47be-8419-4894145b8116)
> 
> tokenB balance= 20.129888944077443


## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.
> Solution
> 滑點是指交易前後因市場波動或大額交易影響而造成的交易價格變化。在Uniswap V2中，為了減少滑點影響，它採用了恆定乘積市場做市商模型（xy=k），這意味著任何交易都必須維持代幣儲備量的乘積不變。例如，如果你要將代幣A換成代幣B，交易前後A和B的儲備量乘積（xy）必須保持恆定。這個公式有助於抑制單個交易對價格的影響，從而減少滑點。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?
> Solution
> 在UniswapV2Pair合約的mint函數中，初始流動性鑄造時會扣除最小流動性，這是為了防止有人通過初始化合約而成為其所有者。這個最小流動性是一種安全措施，以確保合約的去中心化和公平性。具體來說，最小流動性（通常為1000個流動性代幣）被永久鎖定在合約中，防止任何人移除所有流動性導致市場失效。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
> Solution
> 在mint函數中，當不是第一次存款時，用戶存入的代幣量通過一個特定公式來計算可獲得的流動性代幣數量。這個公式確保了新增流動性與總池子中已存在的流動性成正比。其目的是維護每個流動性提供者的份額公正，避免後來者因價格變動而對早期流動性提供者不利。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?
> Solution
> 三明治攻擊是一種在去中心化交易所常見的操縱市場策略，攻擊者會在一個用戶的交易前後執行兩筆交易。攻擊者首先通過一筆大額買入推高價格，然後等待受害者的交易（通常是一個大額市場買單）執行，隨後再通過賣出把價格拉回並獲利。這種攻擊會導致普通用戶以高於市場價格的成本購買代幣，增加了交易成本和風險。

