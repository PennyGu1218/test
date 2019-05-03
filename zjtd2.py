
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    num_lis=[]
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))

        num_lis.append(values)

    all_lis=[]
    for lis in num_lis:
        tz_num = lis[0]
        lis.pop(0)
        vec_num = int(len(lis)/2)
        vec_lis = []
        if vec_num != 0:
            
            for i in range(vec_num):
                vector = [lis[0+2*i],lis[1+2*i]]
                vec_lis.append(vector)
  
        all_lis.append(vec_lis)

    maxi = 0
    local_max = 1
    for i in range(0,m-1):
        comm = [val for val in all_lis[i] if val in all_lis[i+1]]
        print(comm)
        if len(comm) != 0:
            local_max = local_max+1
            all_lis[i+1] = comm
        else:
            if local_max > maxi:
                maxi = local_max
            local_max = 1

    print(max(maxi,local_max))
            

            

