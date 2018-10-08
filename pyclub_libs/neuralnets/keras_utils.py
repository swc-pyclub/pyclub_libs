
def wrapped_partial(func, *args, **kwargs):
    """ Create a partial function that inherits the __name__ and
        __doc__ attributes from the original function. This is 
        important for keras, autograd, and some other libraries
        that use a function's __name__ in their compute graph.
    """
    from functools import partial, update_wrapper    

    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


# Tell tensorflow to only take GPU space when required. 
# This must be called before any other tensorflow/keras stuff is imported
# TODO: this is keras-flavoured, what is the pure-tf equivalent?
def tf_set_gpu_growth():
    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    set_session(tf.Session(config=config))


def setup_reproducible_keras_session(seed=123):
    """ Seed keras to get reproducible results for testing
    """
    from keras import backend as K
    import tensorflow as tf
    import numpy as np
    import random as rn

    K.clear_session()

    # Set all of the necessary seeds
    np.random.seed(seed) 
    rn.seed(seed) 
    tf.set_random_seed(seed)

    # Use single-thread operation 
    session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
    sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)

    K.set_session(sess)


