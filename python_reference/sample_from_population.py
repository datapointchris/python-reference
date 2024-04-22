import multiprocessing

import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

# From a population of POPULATION_SIZE random numbers, take a sample of SAMPLE_SIZE random numbers
# and calculate the mean of the sample. Repeat this MEAN_SAMPLE_SIZE times and calculate the
# mean of the sample means. Compare this to the mean of the population.

POPULATION_SIZES = range(1000, 10_000, 1000)
SAMPLE_RATIOS = [n / 10 for n in range(1, 10)]
MEAN_SAMPLE_SIZES = range(100, 1000, 100)


def calculate_sample_mean(population_size, sample_ratio, mean_sample_size):
    population = np.random.randint(0, 500, size=population_size)
    sample = np.random.choice(population, size=int(population_size * sample_ratio))
    population_mean = np.mean(population)
    sample_mean = np.mean(sample)
    average_sample_mean = [
        np.mean(
            [
                np.mean(np.random.choice(population, size=int(population_size * sample_ratio)))
                for _ in range(mean_sample_size)
            ]
        )
    ]
    return dict(
        population_size=population_size,
        sample_ratio=sample_ratio,
        mean_sample_size=mean_sample_size,
        population_mean=population_mean,
        sample_mean=sample_mean,
        average_sample_mean=average_sample_mean,
        sample_mean_accuracy=abs(population_mean - sample_mean),
        average_sample_mean_accuracy=abs(population_mean - average_sample_mean),
    )


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = []
        for population_size in POPULATION_SIZES:
            for sample_ratio in SAMPLE_RATIOS:
                for mean_sample_size in MEAN_SAMPLE_SIZES:
                    results.append(
                        pool.apply_async(calculate_sample_mean, (population_size, sample_ratio, mean_sample_size))
                    )
        results = [result.get() for result in results]

    print(tabulate(results[:20], headers='keys'))

    for population_size in POPULATION_SIZES:
        for sample_ratio in SAMPLE_RATIOS:
            ratios = [
                result['sample_mean_accuracy']
                for result in results
                if result['population_size'] == population_size and result['sample_ratio'] == sample_ratio
            ]
            plt.plot(MEAN_SAMPLE_SIZES, ratios, label=f"{population_size} {sample_ratio}")
            plt.show()
