

def print_tensor_value(tensor, name):
    # Adds a node to the graph which prints the tensor's value
    # at runtime (can be useful for debugging)

    # In order to support jupyter notebooks we need explicit redirect to 
    # stdout since built-in tf.Print doesn't print to notebook output    
    message = 'Value of {}: '.format(name)
    def print_value(x):
        sys.stdout.write(message + " %s\n" % x)
        return x 
    
    prints = [tf.py_func(print_value, [tensor], tensor.dtype)]
    
    with tf.control_dependencies(prints):
        tensor = tf.identity(tensor)

    return tensor


def print_tensor_shape(tensor, name):
    # Adds a node to the graph which prints the tensor's shape
    # at runtime (can be useful for debugging)

    # In order to support jupyter notebooks we need explicit redirect to 
    # stdout since built-in tf.Print doesn't print to notebook output    
    # TODO: extract method, similar to local method in print_tensor_value
    message = 'Shape of {}: '.format(name)
    def print_shape(x):
        sys.stdout.write(message + " %s\n" % tf.shape(x).shape)
        return x 

    prints = [tf.py_func(print_shape, [tensor], tensor.dtype)]
    
    with tf.control_dependencies(prints):
        tensor = tf.identity(tensor)
    return tensor


def with_dependencies_debug(dependencies, output_tensor, name=None):
    """ A version of tensorflow.python.ops.control_flow_ops.with_dependencies
        which is a no-op when run with -O (optimised) flag.
        This allows us to use dependencies as a debug assertion.
    """
    if __debug__:        
        return with_dependencies(dependencies, output_tensor, name)
    else:
        return output_tensor


def tensor_shape_as_str(shape):    
    shape_str = ', '.join(str(v) for v in shape.as_list())
    shape_str = shape_str.replace('None', '?')
    return shape_str
