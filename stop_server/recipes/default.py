from kokki import Execute, File, Template

if not env.config.wl_jms:
    raise AttributeException('wl_jms is not set')

File(
    env.config.file_path,
    content = Template("simple_file/simple_file.j2", env=env),
)

Execute(
        'Execute uname',
        command = 'uname %s' % env.config.uname_param,
        subscribes = [("run", env.resources["File"][env.config.file_path], True)]
        )


