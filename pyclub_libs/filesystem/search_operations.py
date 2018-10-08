

def find_most_recent_file_matching(glob_pattern):
    # Find newest file matching a pattern
    # e.g. find_most_recent_file_matching('code/*.py')
    import glob 
    import os

    files = glob.glob(glob_pattern)
    files.sort(key=os.path.getmtime)
    if files:
        return files[-1]
    else:
        return None


def get_enclosing_dir(fname):
    # Take the (final) folder name from a full path 
    # e.g. if path is
    # get_enclosing_dir('long/path/containing/file.txt') = 'containing'
    # get_enclosing_dir('long/path/containing/folder/') = 'containing'
    # get_enclosing_dir('long/path/containing/folder') = 'folder'
    # TODO: I'm not sure whether this is expected behaviour for directories.
    # We could insist that directories get closing slash, e.g.
    # fname = os.path.join(fname,'') but this requires that the file actually
    # exists so we can query whether it's a directory, and so far the method
    # doesn't require the path to exist (e.g. may be helpful when planning log
    # directories)
    import os
    return os.path.split(os.path.dirname(fname))[-1]

