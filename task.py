import heapq

class Cable:
    def __init__(self, length, color):
        self.length = length
        self.color = color

    def __lt__(self, other):
        return self.length < other.length

def connect_cables(cables):
    heap = cables[:]
    heapq.heapify(heap)
    total_cost = 0
    connections = []

    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)

        merged_cable = Cable(cable1.length + cable2.length, f"({cable1.color} > {cable2.color})")
        connections.append(merged_cable)
        total_cost += merged_cable.length

        heapq.heappush(heap, merged_cable)

    return total_cost, connections

if __name__ == "__main__":
    cables = [Cable(3, "Red"), Cable(10, "Blue"), Cable(2, "Green"), Cable(14, "Yellow"), Cable(12, "Orange")]
    result_cost, result_connections = connect_cables(cables)

    print("З'єднання кабелів:")
    for connection in result_connections:
        print(f"{connection.color} - {connection.length}")

    print(f"Загальна вартість з'єднання: {result_cost}")
