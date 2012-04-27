from kokki import Execute, File, Template, Service

env.cookbooks.stop_server.SimpleHTTPServer("managed_server_1",
    service_name = "managed_server_1",
    action = ['stop'],
    port = env.config.managed_server_1_port
    )

env.cookbooks.stop_server.SimpleHTTPServer("managed_server_2",
    service_name = "managed_server_2",
#    stop_command = "echo $s|return 2" % env.config.managed_server_2_port,
    action = ['stop'],
    port = env.config.managed_server_2_port
    )

env.cookbooks.stop_server.SimpleHTTPServer("admin_server",
    service_name = "SimpleHTTPServer",
    action = ['stop'],
    port = env.config.admin_server_port,
    subscribes = [('stop', env.resources['SimpleHTTPServer']['managed_server_1'], False),
                ('stop', env.resources['SimpleHTTPServer']['managed_server_2'], False)]
    )

