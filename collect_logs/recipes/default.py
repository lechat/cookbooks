from kokki import File

env.include_recipe('fabric_ops')

env.cookbooks.fabric_ops.FabricFile(
        name = 'SampleFabricPut',
        action = 'put',
        local_path = env.config.local_path,
        roles = env.config.roles,
        roledefs = env.config.roledefs,
        remote_path = env.config.remote_path
)

env.cookbooks.fabric_ops.FabricFile(
        name = 'SampleFabricGet',
        action = ['get'],
        local_path = '/tmp/aaa.txt',
        roles = env.config.roles,
        roledefs = env.config.roledefs,
        remote_path = env.config.remote_path
)

File(
    name = "/tmp/aaa.txt",
    action = 'nothing',
    subscribes = [("touch", env.resources["FabricFile"]["SampleFabricGet"], True)]
)

env.cookbooks.fabric_ops.FabricExecute(
    name = 'f_exec',
    roles = env.config.roles,
    roledefs = env.config.roledefs,
    command = env.config.command
    )
