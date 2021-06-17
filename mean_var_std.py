import numpy as np

def calculate(list):
  #Handle input exception
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  #create the 3x3 matrix from list
  matrix=np.array(list)
  matrix=matrix.reshape((3,3))
  #create the calculations dictionary
  calculations={}
  #calculate means
  calculations["mean"]=[matrix.mean(0).tolist(),matrix.mean(1).tolist(),matrix.mean()]
  #calculate variance
  calculations["variance"]=[matrix.var(0).tolist(),matrix.var(1).tolist(),matrix.var()]
  #calculate standard deviation
  calculations["standard deviation"]=[matrix.std(0).tolist(),matrix.std(1).tolist(),matrix.std()]
  #calculate max
  calculations["max"]=[matrix.max(0).tolist(),matrix.max(1).tolist(),matrix.max()]
  #calculate min
  calculations["min"]=[matrix.min(0).tolist(),matrix.min(1).tolist(),matrix.min()]
  #calculate sum
  calculations["sum"]=[matrix.sum(0).tolist(),matrix.sum(1).tolist(),matrix.sum()]

  


  return calculations
