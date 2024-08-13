from collections import defaultdict

def calculate_conversion_rates(rates, queries):
    # Build graph
    graph = defaultdict(dict)
    for rate in rates:
        from_currency, to_currency, value = rate
        graph[from_currency][to_currency] = value
        graph[to_currency][from_currency] = 1/value
        
    # Perform DFS for each query
    result = []
    for query in queries:
        from_currency, to_currency = query
        visited = set()
        rate = dfs(graph, from_currency, to_currency, 1.0, visited)
        result.append(rate)
        
    return result
    
def dfs(graph, start, end, value, visited):
    if start not in graph:
        return -1.0
    if start == end:
        return value
    visited.add(start)
    neighbors = graph[start]
    for neighbor, neighbor_value in neighbors.items():
        if neighbor not in visited:
            rate = dfs(graph, neighbor, end, value * neighbor_value, visited)
            if rate != -1.0:
                return rate
    return -1.0


rates = [['USD', 'JPY', 100], ['JPY', 'CHN', 20], ['CHN', 'THAI', 200]]
queries = [['USD', 'CHN'], ['JPY', 'THAI'], ['USD', 'AUD']]

# Run the function and print the result
print(calculate_conversion_rates(rates, queries))

# distances = {vertex: float('inf') for vertex in graph}
# distances[src] = 0