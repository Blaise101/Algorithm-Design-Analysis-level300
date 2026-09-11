from src.algorithms import insertion_sort, linear_search, merge_sort, quicksort
from src.benchmark import run_benchmarks
from src.visualization import generate_plots


def main():
    batch_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
    
    algorithms = {
        'Mergesort': lambda data: merge_sort(data),
        'Quicksort': lambda data: quicksort(data),
        'Linear Search': lambda data: linear_search(data, -1),
        'Insertion Sort': lambda data: insertion_sort(data)
    }

    print("Running benchmarks...")
    results = run_benchmarks(batch_sizes, algorithms)
    
    print("Generating plots...")
    generate_plots(batch_sizes, results)
    print("Done! Plots saved in plots/ folder.")

if __name__ == "__main__":
    main()