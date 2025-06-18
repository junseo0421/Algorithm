def solution(chicken):
    total_chicken = []
    
    while chicken >= 10:
        service = chicken // 10
        chicken = service + chicken % 10
        total_chicken.append(service)

    return sum(total_chicken)