import numpy 

def construct_templates(timeseries_data, m):
    num_windows = len(timeseries_data) - m + 1
    return numpy.array([timeseries_data[x : x + m] for x in range(0, num_windows)])

def get_matches(templates, r):
    return len(
        list(filter(lambda x: is_match(x[0], x[1], r), combinations(templates)))
    )

def combinations(x):
    idx = numpy.stack(numpy.triu_indices(len(x), k=1), axis=-1)
    return x[idx]

def is_match(template_1, template_2, r):
    return numpy.all([abs(x - y) < r for (x, y) in zip(template_1, template_2)])

def sample_entropy(timeseries_data, window_size, r):
    B = get_matches(construct_templates(timeseries_data, window_size), r)
    A = get_matches(construct_templates(timeseries_data, window_size + 1), r)
    return -numpy.log(A / B)