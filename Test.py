t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    min=max=1
    diff_not_two=0
    for i in range(n-1):
        diff_two=0
        if(arr[i+1]-arr[i]<=2):
            diff_two+=1
        elif(arr[i+1]-arr[i]>2):
            diff_not_two+=1
            break
    print(min+diff_not_two)
    print(max+diff_two)       