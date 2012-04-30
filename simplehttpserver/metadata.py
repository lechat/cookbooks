
__config__ = {
    "managed_server_1_port": dict(
        description = "Checks if server is already running on this port",
        default = None,
        required = True
    ),
    "managed_server_2_port": dict(
        description = "Checks if server is already running on this port",
        default = None,
        required = True
    ),
    "admin_server_port": dict(
        description = "Checks if server is already running on this port",
        default = None,
        required = True
    ),
}
