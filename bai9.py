import numpy as np
vec1 = np.array([1., 3., 5.])
print(vec1 * 2)
vecsub = vec1 * vec1
print(vecsub)
vecchia = vec1 / 2
print(vecchia)
vecplus = vec1 + vec1
print(vecplus)
vec2 = np.array([2., 4.])
#print(vec1 + vec2)
vec3 = np.array([2., 4., 6.]) 
vecask = vec1 + vec3
print(vecask)
vecsec = vec1 / vec3
print(vecsec)
vecsub2 = vec1 * vec3
print(vecsub2)
print(2* vec1 + 5* vec3)
print(vec3[2])
vec4 = np.linspace(0, 20, 5)
print(vec4)
vec5 = np.zeros(5)
print(vec5)
vec6 = np.ones(5)
print(vec6)
vec7 = np.empty(5)
print(vec7)
print(np.random.rand(5))
v = np.array([1., 3., 5.])
print(np.sum(v))
print(v.shape)
print(v.transpose())
v1 = v[:2]
print(v1)
v1[:2] = [1., 2., 3.]
v1[:2] = [1., 2.]
print(v)
v3 = 2 * v[:2] + v1 * 3
print(v3)
v1 = [4, 6]
print(v3)