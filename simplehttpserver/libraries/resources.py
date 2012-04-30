from kokki import Service, ResourceArgument, ForcedListArgument, Environment

class SimpleHTTPServer(Service):
    provider = "*stop_server.SimpleHTTPServerProvider"

    # actions = ['start', 'stop', 'status']

    action = ResourceArgument(allow_override=True)
    # subscribes = ForcedListArgument(allow_override=True)
    port = ResourceArgument(required=True)
    supports_restart = False
    supports_reload = False
    supports_status = True
