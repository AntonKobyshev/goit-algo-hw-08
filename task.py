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
    visualize_connections = ""

    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)

        merged_cable = Cable(cable1.length + cable2.length, f"({cable1.color} > {cable2.color})")
        visualize_connections += f"{cable1.color} => {cable2.color} " if len(heap) >= 1 else ""

        heapq.heappush(heap, merged_cable)

    return heap[0].length, visualize_connections

if __name__ == "__main__":
    cables = [Cable(3, "Red"), Cable(10, "Blue"), Cable(2, "Green"), Cable(14, "Yellow"), Cable(12, "Orange")]
    result_heap, result_visualize = connect_cables(cables)

    print(f"Порядок об'єднання: {result_visualize}")
    print(f"Загальні витрати: {result_heap}")
