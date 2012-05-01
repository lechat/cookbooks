from fabric.api import env as fenv
from fabric.api import put, get
from fabric.tasks import execute
from fabric.operations import run
from kokki import Provider, Fail

class FabricFileProvider(Provider):
    def action_put(self):
        fenv.roledefs.update(self.resource.roledefs)
        execute(put, self.resource.local_path, self.resource.remote_path, roles=self.resource.roles)
        self.resource.updated()

    def action_get(self):
        fenv.roledefs.update(self.resource.roledefs)
        execute(get, self.resource.remote_path, self.resource.local_path, roles=self.resource.roles)
        self.resource.updated()

class FabricExecuteProvider(Provider):
    def action_run(self):
        for role in self.resource.roles:
            self.log.debug('Finding hosts for role \'%s\'' % role)
            fenv.hosts.extend(self.resource.roledefs[role])

        self.log.debug('Hosts are %s' % fenv.hosts)
        if self.resource.warn_only:
            fenv.warn_only = True
        # ret = execute(run, self.resource.command, roles=self.resource.roles)
        for host in fenv.hosts:
            fenv.host_string = host
            ret = run(self.resource.command)  #, roles=self.resource.roles)
            if self.resource.returns and ret.return_code not in self.resource.returns:
                raise Fail("%s failed, returned %d instead of %s" % (self, ret.return_code, self.resource.returns))

        self.resource.updated()
        # if self.resource.creates:
        #     if os.path.exists(self.resource.creates):
        #         return

        # self.log.info("Executing %s" % self.resource)

        # ret = subprocess.call(self.resource.command, shell=True, cwd=self.resource.cwd, env=self.resource.environment, preexec_fn=_preexec_fn(self.resource))

        # if self.resource.returns and ret not in self.resource.returns:
        #     raise Fail("%s failed, returned %d instead of %s" % (self, ret, self.resource.returns))
        # self.resource.updated()

