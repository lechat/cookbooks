
__config__ = {
    "users": dict(
        description = "Users which will appear in file",
        default = [],
    ),
    "file_path" : dict(
        description = 'Path and file name',
        default = '/tmp/test_simple_file',
    ),
    'uname_param': dict(
        description = 'Parameter passes to uname',
        default = '-a',
        # default = None,
    )
}
