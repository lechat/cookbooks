from kokki.exceptions import Fail
from kokki.providers.service import ServiceProvider

class SimpleHTTPServerProvider(ServiceProvider):
    # start_command =

    def __init__(self, resource):
        super(SimpleHTTPServerProvider, self).__init__(resource)
        # This is example of late (runtime validation)
        if not self.resource.port:
            raise Fail('Port attribute is required for SimpleHTTPServerProvider')

    def action_start(self):
        self.log.debug('SimpleHTTPServerProvider - action_start')
        if not getattr(self.resource, 'start_command'):
            self.resource.start_command = '/usr/bin/python -m SimpleHTTPServer %s &' % self.resource.port
        super(SimpleHTTPServerProvider, self).action_start()

    def action_stop(self):
        self.log.debug('SimpleHTTPServerProvider - action_stop')
        if not getattr(self.resource, 'stop_command'):
            self.resource.stop_command = "lsof -i tcp:%s | awk 'NR!=1 {print $2}' | xargs kill" % self.resource.port
        super(SimpleHTTPServerProvider, self).action_stop()

    def status(self):
        self.log.debug('SimpleHTTPServerProvider - status')
        if not getattr(self.resource, 'status_command'):
            self.resource.status_command = "lsof -i tcp:%s" % self.resource.port
        return super(SimpleHTTPServerProvider, self).status()

