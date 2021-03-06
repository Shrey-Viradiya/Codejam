t = int(input())
matrices = [
    (2,2,[[1, 2],[2, 1]]),
    (2,4,[[2, 1],[1, 2]]),
    (3,3,[[1,2,3], [3,1,2] , [2,3,1]]),
    (3,6,[[2,3,1], [1,2,3] , [3,1,2]]),
    (3,9,[[3,1,2], [2,3,1] , [1,2,3]]),
    (4,4,[ [1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,4,1] ]),
    (4,6,[ [2,1,3,4],[1,2,4,3],[3,4,1,2],[4,3,2,1] ]),
    (4,7,[ [3,1,4,2],[1,2,3,4],[2,4,1,3],[4,3,2,1] ]),
    (4,8,[ [2,3,4,1],[1,2,3,4],[4,1,2,3],[3,4,1,2] ]),
    (4,9,[ [3,1,4,2],[2,3,1,4],[1,4,2,3],[4,2,3,1] ]),
    (4,10,[ [3,2,1,4],[2,3,4,1],[4,1,2,3],[1,4,3,2] ]),
    (4,11,[ [4,2,1,3],[2,3,4,1],[3,1,2,4],[1,4,3,2] ]),
    (4,12,[ [3,4,1,2],[2,3,4,1],[1,2,3,4],[4,1,2,3] ]),
    (4,13,[ [4,2,3,1],[3,4,1,2],[1,3,2,4],[2,1,4,3] ]),
    (4,14,[ [4,3,1,2],[3,4,2,1],[1,2,3,4],[2,1,4,3] ]),
    (4,16,[ [4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4] ]),
    (5,5,[ [1,2,3,4,5],[5,1,2,3,4],[4,5,1,2,3],[3,4,5,1,2],[2,3,4,5,1] ]),
    (5,7,[ [1,3,2,5,4],[5,2,4,3,1],[4,5,1,2,3],[2,4,3,1,5],[3,1,5,4,2] ]),
    (5,8,[ [1,4,2,5,3],[2,1,3,4,5],[3,5,1,2,4],[5,2,4,3,1],[4,3,5,1,2] ]),
    (5,9,[ [2,4,1,3,5],[3,1,5,4,2],[5,2,3,1,4],[1,5,4,2,3],[4,3,2,5,1] ]),
    (5,10,[ [2,3,4,5,1],[1,2,3,4,5],[5,1,2,3,4],[4,5,1,2,3],[3,4,5,1,2], ]),
    (5,11,[ [3,4,2,1,5],[1,2,5,4,3],[5,3,1,2,4],[2,5,4,3,1],[4,1,3,5,2], ]),
    (5,12,[[3,5,1,4,2],[2,1,4,3,5],[4,2,3,5,1],[5,4,2,1,3],[1,3,5,2,4]]),
    (5,13,[[3,4,1,2,5],[5,1,2,4,3],[2,3,4,5,1],[4,5,3,1,2],[1,2,5,3,4]]),
    (5,14,[[3,4,2,5,1],[4,2,5,1,3],[5,1,3,4,2],[1,3,4,2,5],[2,5,1,3,4]]),
    (5,15,[[3,4,5,1,2],[5,2,1,4,3],[2,1,4,3,5],[4,5,3,2,1],[1,3,2,5,4]]),
    (5,16,[[2,4,5,1,3],[5,3,1,4,2],[3,1,4,2,5],[4,5,2,3,1],[1,2,3,5,4]]),
    (5,17,[[1,5,4,2,3],[4,3,2,5,1],[3,2,5,1,4],[5,4,1,3,2],[2,1,3,4,5]]),
    (5,18,[[2,5,4,1,3],[4,3,1,5,2],[3,1,5,2,4],[5,4,2,3,1],[1,2,3,4,5]]),
    (5,19,[[1,5,3,2,4],[3,4,2,5,1],[4,2,5,1,3],[5,3,1,4,2],[2,1,4,3,5]]),
    (5,20,[[2,5,1,3,4],[1,4,3,5,2],[4,3,5,2,1],[5,1,2,4,3],[3,2,4,1,5]]),
    (5,21,[[3,5,1,2,4],[1,4,2,5,3],[4,2,5,3,1],[5,1,3,4,2],[2,3,4,1,5]]),
    (5,22,[[4,2,5,1,3],[1,5,3,2,4],[3,1,4,5,2],[5,3,2,4,1],[2,4,1,3,5]]),
    (5,23,[ [5,1,4,2,3],[2,4,3,1,5],[3,2,5,4,1],[4,3,1,5,2],[1,5,2,3,4], ]),
    (5,25,[ [5,1,2,3,4],[4,5,1,2,3],[3,4,5,1,2],[2,3,4,5,1],[1,2,3,4,5], ])
]


for i in range(1,t+1):
    n,k = list(map(int,input().split()))
    # print("({:d} {:d})".format(n,k))
    for o,j,m in matrices:
        if o == n and k == j:
            print("Case #{:d}: POSSIBLE".format(i))
            for e in range(n):
                for r in range(n):
                    print("{:d}".format(m[e][r]), end=' ')
                print()
            break
    else:
        print("Case #{:d}: IMPOSSIBLE".format(i))


