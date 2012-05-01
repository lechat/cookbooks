from kokki import Resource, ResourceArgument, ForcedListArgument, BooleanArgument, Execute

class FabricFile(Resource):
    provider = "*fabric_ops.FabricFileProvider"
    actions = ['put', 'get']
    local_path = ResourceArgument()
    remote_path = ResourceArgument()
    roles = ForcedListArgument()
    roledefs = ResourceArgument()

class FabricExecute(Execute):
    provider = "*fabric_ops.FabricExecuteProvider"
    roles = ForcedListArgument()
    roledefs = ResourceArgument()
    warn_only = BooleanArgument(default=True)
