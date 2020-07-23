from collections import defaultdict

def slidingWindow(word):
    dist_count=len(set(word))
    dict=defaultdict(int)
    start,end=0,0
    min_len=len(word)
    count=0
    for i in range(0,len(word)):
        dict[word[i]]+=1
        if(dict[word[i]]==1):
            count+=1
        if(dist_count==count):
            while(dict[word[start]]>1):
                dict[word[start]]-=1
                start+=1
            end=i
            len_window=s=end-start+1
            min_len=min(min_len,len_window)
    return min_len

t=int(input())
for i in range(0,t):
    word=input()
    print(slidingWindow(word))
