import sys
import collections


class debug_context():
    """ Debug context to trace any function calls inside the context.
        And log something for every new variable seen """

    def __init__(self, name, var_prop_func):
        """

        :param str name: Function name (from func.__name__)
        :param function var_prop_func: A function that takes as input any local variable,
            and outputs some property you want logging, e.g. size of variable, type of variable, value of variable.
            The output of this function must be hashable.
        """
        self.name = name
        self.var_prop = var_prop_func
        
        # cached_vars is dict {var_name: var_prop}
        # i.e. all {variable, property} pairs that have been logged already
        # This avoids duplicates whilst allow picking up changes to properties.
        self.cached_vars = {}

    def __enter__(self):
        """ Trace all events with custom function """
        sys.settrace(self.trace_calls)

    def __exit__(self, *args, **kwargs):
        """ Stop tracing all events """
        sys.settrace(None)

    def trace_calls(self, frame, event, arg): 
        """ We want to only trace our call to the decorated function """
        if event != 'call':
            return
        elif frame.f_code.co_name != self.name:
            return
        
        # return the trace function to use when you go into that function call
        return self.trace_lines

    def var_prop_hashable(self, x):
        """ Make sure that the property being returned is hashable.
            This is important since we'll be storing it in a dictionary.
        """
        prop = self.var_prop(x)
        if isinstance(prop, collections.Hashable):
            return prop
        else:
            return 'Unhashable type {}'.format(type(x))

    def trace_lines(self, frame, event, arg):        
        if event not in ['line']:
            return
        
        co = frame.f_code
        func_name = co.co_name
        line_no = frame.f_lineno
        filename = co.co_filename
        
        # Extract property we're interested in from each local variable        
        local_vars = frame.f_locals
        local_vars_with_props = {k: self.var_prop_hashable(local_vars[k]) 
                                    for k in local_vars.keys()}            

        # Remove any already logged (unless they've changed their property since logging)
        new_or_changed_vars = dict( 
            set(local_vars_with_props.items()) - 
            set(self.cached_vars.items()) )
        
        self.cached_vars = local_vars_with_props.copy()

        for name, var in new_or_changed_vars.items():
            print('   {} {} {}: variable {}: {}'.format(func_name, event, line_no, name, var))


class log_all_variables(object):
    """ Decorator that logs every new/changed local variable in a function, or
        some custom property of it.
    """

    def __init__(self, var_property_function=None):
        """
        :param function var_property_function: an optional function that takes a variable as
            input and outputs the property of the variable that you want to log.
            e.g. x: return x  # (this is the default)
                x: return x.shape()
                x: return type(x)
        """
        self.var_prop = var_property_function
        
        # default to printing out every variable if no other
        # property functor given
        if (self.var_prop is None):
            self.var_prop = lambda x: x

    def __call__(self, func):
        def wrapped_f(*args):
            with debug_context(func.__name__, self.var_prop):            
                return_val = func(*args)
            return return_val
        return wrapped_f


class log_all_variables_type(log_all_variables):
    def __init__(self):
        self.var_prop = type

