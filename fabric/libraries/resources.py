from kokki import File, ResourceArgument, Environment

class FabricFile(File):
    provider = "*fabric.FabricFileProvider"

    actions = ['put', 'get']

    local_path = ResourceArgument()
    remote_path = ResourceArgument()
    role = ResourceArgument()
