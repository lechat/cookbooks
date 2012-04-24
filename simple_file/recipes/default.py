
from kokki import Execute, File, Template

Execute(
        'Execute uname',
        command = 'uname %s' % env.config.uname_param,
        )

if not env.config.wl_jms:
    raise AttributeException('wl_jms is not set')

File(
    env.config.file_path,
    content = Template("simple_file/simple_file.j2", env=env),
)
