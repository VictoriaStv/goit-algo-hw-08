import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Витягнути два найменших кабелі
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Об'єднати їх
        combined = first_min + second_min
        
        # Додати вартість об'єднання до загальної вартості
        total_cost += combined
        
        # Додати новий кабель назад у купу
        heapq.heappush(cables, combined)
    
    return total_cost

# Тест
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
