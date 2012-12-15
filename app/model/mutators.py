import pkgutil

class Mutators:
  def __init__(self):
    self._muts = []
    for importer, pkg_name, _ in pkgutil.iter_modules(['app/mutators']):
        full = 'app.mutators.' + pkg_name
        module = importer.find_module(pkg_name).load_module(full)
        self.register(module)

  def register(self, module):
    for name in dir(module):
      attr = getattr(module, name)
      if callable(attr):
        self._muts.append(attr)

  def __iter__(self):
    for mut in self._muts:
      yield mut
