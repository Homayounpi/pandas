x='assa assa'
palindi_li=[]
start=0
end=2
all=[]
for i in range(len(x)-1):
    v_start = 0
    v_end =i+2
    for j in range((len(x)-end)+1):
        val=x[v_start:v_end]
        all.append(val)

        if val==val[::-1]:
            palindi_li.append(val)
        v_start=v_start+1
        v_end=v_end+1
    end+=1
print(set(palindi_li))









