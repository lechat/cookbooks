from kokki import Execute, File, Template, Service

env.cookbooks.simplehttpserver.SimpleHTTPServer("managed_server_1",
    service_name = "managed_server_1",
    action = ['start'],
    port = env.config.managed_server_1_port
    )

env.cookbooks.simplehttpserver.SimpleHTTPServer("managed_server_2",
    service_name = "managed_server_2",
#    stop_command = "echo $s|return 2" % env.config.managed_server_2_port,
    action = ['start'],
    port = env.config.managed_server_2_port
    )

env.cookbooks.simplehttpserver.SimpleHTTPServer("admin_server",
    service_name = "SimpleHTTPServer",
    action = ['start'],
    port = env.config.admin_server_port,
    subscribes = [('start', env.resources['SimpleHTTPServer']['managed_server_1'], False),
                ('start', env.resources['SimpleHTTPServer']['managed_server_2'], False)]
    )

