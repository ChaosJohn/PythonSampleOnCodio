__author__ = 'ChaosJohn'
#To change this template use Tools | Templates.

def buildConnectionString(params): 
  """
  \rBuild a connection string from a dictionary of parameters. 
  \rReturns string.
  """
  return ";".join(["%s=%s" % (k, v) for k, v in params.items()]) 

if __name__ == "__main__": 
  myParams = {
    "server": "mpilgrim", 
    "database": "master", 
    "uid": "sa", 
    "pwd": "secret" 
  }
  print buildConnnectionString(myParams) 
  