from kokki import Execute, File, Template
import tenjin
import re

class NoShellVarSubstTemplate(tenjin.Template):
    """Same as standard replacemt except that we ignore patters like this: ${...}"""
    s = '(?:\{.*?\}.*?)*'
    EXPR_PATTERN = re.compile(r'#\{(.*?' + s + r')\}|\{=(?:=(.*?)=|(.*?))=\}', re.S)
    del s

    def __init__(self, filename=None, encoding=None, iinput=None, escapefunc=None, tostrfunc=None,
                    indent=None, preamble=None, postamble=None, smarttrim=None, trace=None):
        tenjin.Template.__init__(self, filename, encoding, iinput, escapefunc, tostrfunc,
                                    indent, preamble, postamble, smarttrim, trace)

    def expr_pattern(self):
        return self.EXPR_PATTERN

    def get_expr_and_flags(self, match):
        expr1, expr2, expr3 = match.groups()
        if expr1:
            return expr1, (False, True)   # not escape,  call to_str
        if expr2:
            return expr2, (False, True)   # not escape,  call to_str
        if expr3:
            return expr3, (True,  True)   # call escape, call to_str

File(
    env.config.file_path,
    content = Template("simple_file/simple_file.tj", env=env, variables=env.config, engine='tenjin', templateclass=NoShellVarSubstTemplate),
)
