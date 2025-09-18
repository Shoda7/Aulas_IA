from greedy import greedy_best_first_search
from a_star import a_star_search
from graphs import graph_romenia
from heuristics import heuristic_romenia

def run_romenia():
    
    start, goal = 'Arad', 'Bucharest'
    print(f'=== ROMENIA GRAPH (start: {start} -> goal: {goal}) ===')

    # Executa a busca Greedy Best-First Search
    g_path, g_order, g_cost = greedy_best_first_search(graph_romenia, start, goal, heuristic_romenia)
    print('[Greedy] path:', g_path)
    print('[Greedy] explored:', g_order)
    print('[Greedy] cost:', g_cost)
    print('---')

    # Executa a busca A*
    a_path, a_order, a_cost = a_star_search(graph_romenia, start, goal, heuristic_romenia)
    print('[A*]     path:', a_path)
    print('[A*]     explored:', a_order)
    print('[A*]     cost:', a_cost)


if __name__ == '__main__':
    run_romenia()