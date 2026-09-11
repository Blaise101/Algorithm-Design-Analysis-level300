import random
import time


def run_benchmarks(batch_sizes, algorithms):
  results = {alg: [] for alg in algorithms}

  for size in batch_sizes:
    print(f"Testing array size n = {size}...")
    random_data = [random.randint(1, 1000000) for _ in range(size)]
    
    for name, func in algorithms.items():
      if name == 'Insertion Sort' and size > 32000:
        results[name].append(None)
        continue
        
      times = []
      for _ in range(3):
        arr_to_test = random_data.copy()
        start_time = time.perf_counter()
        func(arr_to_test)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        
      avg_time = sum(times) / 3.0
      results[name].append(avg_time)
            
  return results