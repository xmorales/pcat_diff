class Catalog(object):
  def __init__ (self):
    self.catalog = None;
    self.RAWresources = None;
    self.resources = [];
    
  def read(self,node,env,puppetURI = puppet):
    # Review if a puppet binary exist
    # Launch puppet master node --environment env and parse it into a JSON Object
    # Parse resources and save them into our own objects
    
  def diff(self,other_catalog):
    # return an array of patches in JSON format
    
  def applyPatches(self, patches):
    # return an array of Resource object with its JSON and its patch
    
  def getPuppetCode(self,diff_only = True):
    # return a string with the puppet code which reflects this catalog
    # if diff_only is True, then only returns the ones with patch