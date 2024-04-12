liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# Set initial node for the DFS
start_token = 'B'

# List to hold swap results
trading_details = []

# Define the token network
token_network = {
    'A': ['B', 'C', 'D', "E"],
    'B': ['A', 'C', 'D', 'E'],  # Assuming B can also reach E
    'C': ['A', 'B', 'D', 'E'],  # Assuming C can also reach E
    'D': ['A', 'B', 'C', 'E'],  # Assuming D can also reach E
    'E': ['A', 'B', 'C', 'D']   # Added full connectivity for E
}

# Function to calculate the token balance through the path
def calculate_balance(route, action_flag):
    base_amount = 5
    previous_token = "tokenB"
    current_token = "tokenB"
    initial_amount = base_amount
    final_amount = base_amount
    
    for index in range(len(route)-1):
        next_token = "token" + route[index + 1]
        if previous_token > next_token:
            reserve_b, reserve_a = liquidity[(next_token, previous_token)]
        else:
            reserve_a, reserve_b = liquidity[(previous_token, next_token)]
        
        base_amount = (997 * base_amount * reserve_b) / (1000 * reserve_a + 997 * base_amount)

        if action_flag:
            final_amount = base_amount
            global trading_details
            trading_details.append([initial_amount, final_amount])
            initial_amount = final_amount

        previous_token = next_token
        
    if previous_token < "tokenB":
        reserve_a, reserve_b = liquidity[(previous_token, "tokenB")]
    else:
        reserve_b, reserve_a = liquidity[("tokenB", previous_token)]
        
    base_amount = (997 * base_amount * reserve_b) / (1000 * reserve_a + 997 * base_amount)
    if action_flag:
        final_amount = base_amount
        trading_details.append([initial_amount, final_amount])
        initial_amount = final_amount
        
    return base_amount

# Depth-First Search to explore token paths
def explore_token_paths(network_map, current_node, visited_status, route):
    visited_status[current_node] = True
    route.append(current_node)
    path_value = 0

    if len(route) > 1:
        path_value = calculate_balance(route, 0)

    if path_value >= 20:
        path_value = calculate_balance(route, 1)
        final_route = route + ['B']
        final_route = ['token' + token for token in final_route]
        print(" -> ".join(final_route), ", tokenB balance=", path_value)
        return
    else:
        for neighbour in network_map[current_node]:
            if not visited_status[neighbour]:
                explore_token_paths(network_map, neighbour, visited_status, route)

    visited_status[current_node] = False
    route.pop()

# Initiate visited status and route list
visited_tokens = {node: False for node in token_network}
current_route = []

# Start DFS from token B
explore_token_paths(token_network, 'B', visited_tokens, current_route)

# Print all swaps executed
for idx, swap in enumerate(trading_details, 1):
    print(f"SWAP {idx} : ")
    print(f"amountIn = {swap[0]}, amountOut = {swap[1]}")
