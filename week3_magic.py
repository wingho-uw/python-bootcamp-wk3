import numpy as np

#### function with one broad peak and one small narrow peak

def twopeaks(x):
    return 5 * np.exp(-x**2) + 0.0005 / ((x-1.5)**2 + 0.001)

#### generate four sets of independent random normal samples

np.random.seed(1001)
normal_1a = np.random.normal(0, 1, size=100)
normal_1b = np.random.normal(0, 1, size=100)
normal_2a = np.random.normal(0, 2, size=100)
normal_2b = np.random.normal(0, 2, size=100)

#### generate a uniform random sample and a dependent second sample

np.random.seed(1234)
uniform_10 = np.random.uniform(0.0, 10.0, size=100)
linear = 2.0 + 0.8 * uniform_10 + np.random.normal(0, 0.5, size=100)

#### source data for the correlation plots

np.random.seed(8)
random = np.random.randn(100)
uncorr = np.random.randn(100)
nonlinear = 0.7 * random**2 + 0.3 * uncorr
positive = 0.35 * random    + 0.65 * uncorr
negative = -0.35 * random   + 0.65 * uncorr
Positive = 0.7 * random     + 0.3 * uncorr
Negative = -0.7 * random    + 0.3 * uncorr

#### data for probability mass function to be plotted

pmf_values = np.array([0.025, 0.1, 0.2, 0.05, 0.0125, 0.0125, 0.05, 0.1, 0.3, 0.15])

#### generated a somewhat complex 2d sample

np.random.seed(101)
cauchy = np.random.standard_cauchy(size=900)
cauchy_cropped = cauchy[np.logical_and(cauchy < 1, cauchy > -1)][:420]
triangular = np.random.triangular(-1, 0, 1, 420)
unrotated = np.array([cauchy_cropped, triangular])

theta = 0.15
rotation = np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta), np.cos(theta)]])
rotated = rotation @ unrotated
rotated = rotated[:, (rotated[0, :] < 1) & (rotated[0, :] > -1) & (rotated[1, :] < 1) & (rotated[1, :] > -1)]

samples_x = rotated[0]
samples_y = rotated[1]

#### the corresponding histogram bins

bins = np.arange(-1, 1.1, 0.2)
x_counts = np.histogram(samples_x, bins)[0]
y_counts = np.histogram(samples_y, bins)[0]