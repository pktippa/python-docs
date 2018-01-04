import sys
if sys.platform == "win32":
    import psutil
    print("psutil", psutil.Process().memory_info().rss)
else:
    # Note: if you execute Python from cygwin,
    # the sys.platform is "cygwin"
    # the grading system's sys.platform is "linux2"
    import resource
    print("ram usage in MB :", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
