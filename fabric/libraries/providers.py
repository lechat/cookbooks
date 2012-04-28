from fabric import operations
from kokki import Provider

class FabricFileProvider(Provider):
    def action_create(self):
        path = self.resource.path
        write = False
        content = self._get_content()
        if not os.path.exists(path):
            write = True
            reason = "it doesn't exist"
        else:
            if content is not None:
                with open(path, "rb") as fp:
                    old_content = fp.read()
                if content != old_content:
                    write = True
                    reason = "contents don't match"
                    self.resource.env.backup_file(path)

        if write:
            self.log.info("Writing %s because %s" % (self.resource, reason))
            with open(path, "wb") as fp:
                if content:
                    fp.write(content)
            self.resource.updated()

        if _ensure_metadata(self.resource.path, self.resource.owner, self.resource.group, mode = self.resource.mode, log = self.log):
            self.resource.updated()

    def action_delete(self):
        path = self.resource.path
        if os.path.exists(path):
            self.log.info("Deleting %s" % self.resource)
            os.unlink(path)
            self.resource.updated()

    def action_touch(self):
        path = self.resource.path
        with open(path, "a"):
            pass

    def _get_content(self):
        content = self.resource.content
        if content is None:
            return None
        elif isinstance(content, basestring):
            return content
        elif hasattr(content, "__call__"):
            return content()
        raise Fail("Unknown source type for %s: %r" % (self, content))


