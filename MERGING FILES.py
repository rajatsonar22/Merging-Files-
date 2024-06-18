#MERGE FILES
#MERGING FILES
print(">>> MERGING FILES ")
print("")#....space
import heapq
def merge_files(file_sizes):
    heapq.heapify(file_sizes)
    total_cost = 0
    while len(file_sizes) > 1:
        smallest1 = heapq.heappop(file_sizes)
        smallest2 = heapq.heappop(file_sizes)
        merged_files = smallest1 + smallest2
        total_cost += merged_files
        heapq.heappush(file_sizes, merged_files)
    return total_cost
print("It returns the total miniumum cost")
print("")#...space
if __name__ == "__main__":
    files = [10,5,2,30,3]
    min_cost = merge_files(files)
    print("--- Minimum cost to merge files", min_cost)
