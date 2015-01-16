import cuv_python as cp
import numpy as np
import os
import random

def kmeans(dataset, num_clusters, iters):
    # initialize clusters randomly
    rand_indices = np.random.randint(0, dataset.shape[0], num_clusters)
    clusters = dataset[rand_indices,:]

    # push initial clusters and dataset to device
    dataset_dev = cp.dev_tensor_float(dataset)
    clusters_dev = cp.dev_tensor_float(clusters)

    # allocate matrices for calculations (so we don't need to allocate in loop)
    dists = cp.dev_tensor_float([dataset_dev.shape[0], num_clusters])
    nearest = cp.dev_tensor_int(dataset_dev.shape[0])
    
    # main loop
    for i in xrange(iters):
        # compute pairwise distances
        cp.pdist2(dists, dataset_dev, clusters_dev)
        # find closest cluster
        cp.reduce_to_col(nearest, dists, cp.reduce_functor.ARGMIN)
        # update cluster centers
        # (this is a special purpose function for kmeans)
        cp.compute_clusters(clusters_dev, dataset_dev, nearest)
    return [clusters_dev.np, nearest.np]

if __name__ == "__main__":

    num_clusters = 5
    mnist = np.random.rand(60000, 2).astype('float32')
    [clusters, indices] = kmeans(mnist, num_clusters, 10)

    print clusters
    print indices
