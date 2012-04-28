env.cookbooks.fabric.FabricFile(
        action = ['put'],
        local_path = env.config.local_path,
        role = env.config.role,
        remote_path = env.config.remote_path
)

env.cookbooks.fabric.FabricFile(
        action = ['get'],
        local_path = env.config.local_path,
        role = env.config.role,
        remote_path = env.config.remote_path
)
