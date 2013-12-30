class Resource(object):
  def __init__ (self,resource):
    self.orig_resource = resource;
    self.patch = None;
    self.patched_resource = None;
    
  def applyPatch(self,patch):
    self.patch = patch;
    # Transform original resource from patch
    
  def getPuppetCode(self):
    # return a string with puppet code to represent this resource