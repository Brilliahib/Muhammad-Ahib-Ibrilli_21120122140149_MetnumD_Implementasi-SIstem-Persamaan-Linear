# declaration for matrix A
A = [[3, 2, -1],
     [2, -2, 4],
     [-1, 0.5, -1]]
# declaration for vector b
b= [1, -2, 0]
# create function to show element of matrix
def show(matrix):
    n = len(matrix)
    for row in range(n):
      for col in range(n):
        print('%.2f' % matrix[row][col], end="\t")
      print("")
show(A)
# get number of rows from A
n = len(A)
# create zeros matrix of L and U
L = [[0 for row in range(n)]
   for col in range(n)]
U = [[0 for row in range(n)]
   for col in range(n)]
for p in range(n):
  # upper matrix
  for j in range(p,n):
    # summation of L(p,k)*U(k,j)
    sum = 0
    for k in range(p):
      sum = sum + L[p][k]*U[k][j]
    U[p][j] = A[p][j] - sum
# lower matrix
q = p
for i in range (q,n):
  if (i==q):
    # diagonal of L
    L[i][q]=1
  else:
    # summation of L(i,k)*U(k,q)
    sum = 0
    for k in range(q):
      sum = sum + L[i][k]*U[k][q]
    L[i][q] = (A[i][q] - sum)/U[q][q]
def decomposition(A):
  # get number of rows from A
  n = len(A)
  # create zeros matrix of L and U
  L = [[0 for row in range(n)]
       for col in range(n)]
  U = [[0 for row in range(n)]
       for col in range(n)]
  
  for p in range(n):
    # upper matrix
    for j in range(p,n):
      # summation of L(p,k)*U(k,j)
      sum = 0
      for k in range(p):
        sum = sum + L[p][k]*U[k][j]
      U[p][j] = A[p][j] - sum
  # lower matrix
    q = p
    for i in range (q,n):
      if (i==q):
        # diagonal of L
        L[i][q]=1
      else:
        # summation of L(i,k)*U(k,q)
        sum = 0
        for k in range(q):
          sum = sum + L[i][k]*U[k][q]
        L[i][q] = (A[i][q] - sum)/U[q][q]
  return L, U

# Kode Testing
# matrix A
A = [[1, 3, 1],
     [1, 5, 5],
     [2, 7, 5]]
# calculate L and U     
L, U = decomposition(A)
# show L and U
print("Matrix L :")
show(L)
print("\nMatrix U :")
show(U)