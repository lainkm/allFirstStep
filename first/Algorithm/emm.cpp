#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<map>
#include<queue>
#include <iostream>
using namespace std;
const int N=1e5+10;
int n,m;
int a[N];
/*建立一个大根堆，一个小根堆，保证大根堆的个数大于等于小根堆
*使大根堆保存较小的一部分数，小根堆保存较大的一部分数（拆分情况调整两个堆）
*这样中位数就是大根堆的堆顶元素*/
struct heap{
	int a[N];
	int num;
	bool (*op)(int,int);

	void clear(){
		num=0;	
	}
	void insert(int x){
	    a[++num]=x;
	    int t=num;
	    while(t>1 && op(a[t],a[t/2])){
	    	swap(a[t],a[t/2]);
	    	t/=2;
	    }
	}
	int getTop(){
		return a[1];
	}
	int getSize(){
		return num;
	}
	int pop(){
		int res=a[1];
		swap(a[1],a[num]);
		num--;
		int t=1;
		while(t*2<=num){
			int l=t*2;
			if(l<num && op(a[l+1],a[l])) l++;
			if(op(a[l],a[t])){
				swap(a[l],a[t]);
				t=l;
			}else break;
		}
		return res;
	}
}h1,h2;
bool max(int a,int b){
	return a>b;
}
bool min(int a,int b){
	return a<b;
}
int main() {
    //freopen("aaa","r",stdin);
	int T;
	scanf("%d",&T);
	h1.op=max;
    h2.op=min;
	while(T--){
		int id;
		scanf("%d",&id);
		scanf("%d",&n);
		printf("%d %d\n",id,(n+1)/2);
		int num=0;
		h1.clear();
		h2.clear();

		for(int i=1;i<=n;i++){
			scanf("%d",a+i);
			if(i&1){
				if(h1.getSize()==0 || a[i]<=h2.getTop()){
					h1.insert(a[i]);
				}else{
					h1.insert(h2.pop());
					h2.insert(a[i]);
				}
				num++;
				printf("%d%c",h1.getTop(),(num==10 || i==n)?'\n':' ');
				if(num==10) num=0;
			}else{
				if(a[i]<=h1.getTop()){
					h2.insert(h1.pop());
					h1.insert(a[i]);
				}else{
					h2.insert(a[i]);
				}
			}
		}

	}

	return 0;
}
