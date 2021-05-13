N, K=map(int, input().split())


for i in range(K):
  if (N % 200)==0:
    N = N /200
    N=int(N)
  else:
    N=str(N)
    N=int("".join([N, "200"]))
print(N)