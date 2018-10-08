import numpy as np
import numpy.linalg as linalg


def is_vec(x):
    if np.squeeze(x).ndim == 1:
        return True
    else:
        return False


def make_vec(x):
    import numpy as np
    
    if (len(x.shape) == 1):
        x = np.expand_dims(x, axis=1)
    return x


def batch_outer(A):
    # Takes a matrix of size [n, d]
    # and takes outer product of each d*1 vector, 
    # giving output of size [n, d, d]
    n, d = A.shape
    B = np.zeros((n,d,d), dtype=A.dtype)
    for i, a_i in enumerate(A):
        B[i,:,:] = np.outer(a_i,a_i)    
    return B


def batch_diag(A):  
    #  EITHER: 
    # 1) Takes a matrix of size [n,d]
    # and creates a 2d diagonal array for 
    # each d*a vector, giving output of
    # shape [n,d,d]; OR
    # 2) Takes a matrix of size [n,d,d]
    # and extracts diag of each d*d matrix
    # giving output of shape [n,d] ; or
    
    if A.ndim == 2:
        # from https://stackoverflow.com/a/26517247
        n, d = A.shape
        B = np.zeros((n,d,d))
        diag = np.arange(d)
        B[:, diag, diag] = A    
    elif A.ndim == 3:        
        n, d, d = A.shape
        B = np.zeros((n,d), dtype=A.dtype)
        for i, a_i in enumerate(A):
            B[i,:] = np.diag(a_i)    
    else:
        raise ValueError('batch_diag expects input''s ndim to be 2 or 3')

    return B


def ordered_eig(A):
    # returns ordered from biggest eigenvalue to smallest
    # from https://stackoverflow.com/a/8093043

    # TODO: default sort order for complex eigenvalues is 
    # ordered-by-real-value-first.. I'm not sure if this is 
    # desirable (I only use this func on PSD matrices)
    vals, vecs = np.linalg.eig(A)

    idx = vals.argsort()[::-1] 

    vals = vals[idx]
    vecs = vecs[:,idx]

    return vals, vecs


def print_nparray_props(x):
    # helper function prints out stats about x

    import numpy as np
    assert(type(x).__module__ =='numpy')
    print('Shape: {}'.format(x.shape))
    print('Type: {}'.format(x.dtype))
    print('Min: {}'.format(np.nanmin(x)))
    print('Mean: {}'.format(np.nanmean(x)))
    print('Max: {}'.format(np.nanmax(x)))



