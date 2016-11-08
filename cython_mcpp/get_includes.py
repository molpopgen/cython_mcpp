def get_includes():
    """
    Returns where the cython_mpp headers were installed.

    Use -I + the returned string to include these headers in
    your own projects.

    .. note:: This likely only works on POSIX systems.
    """
    import re
    import cython_mcpp
    includes=cython_mcpp.__file__
    includes=re.sub('lib','include',includes)
    includes=re.sub('site-packages/','',includes)
    includes=re.sub(r'/__init__.+','',includes)
    p=re.compile(r'python3.\d+')
    f=p.findall(includes)
    for i in f:
        includes=re.sub(i,i+'m',includes)
    return includes


