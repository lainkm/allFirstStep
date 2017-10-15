#include <cstring>
#include <cstdio>
#include <iostream>
const int MAX = 10000 + 5;
const int inf = 0x3f3f3f3f;
using namespace std;

/*最小堆*/
struct minHeap{
    int a[MAX];
    int num;
    
    int Top()
    {
        return a[1];
    }
    int getSize()
    {
        return num;
    }
    void Insert(int x)
    {
        a[++num] = x;
        int i = num;
        while(i > 1 && a[i >> 1] > a[i])
        {
            swap(a[i], a[i >> 1]);
            i >>= 1;
        }
    }
    int Pop()
    {
        int res = a[1];
        swap(a[1], a[num]);
        num --;
        int i = 1;
        while (i * 2 <= num)
        {
            int left = i << 1;
            if (left < num && a[left] > a[left + 1])
                left ++;
            if (a[i] > a[left])
            {
                swap(a[left], a[i]);
                i = left;
            }
            else break;
        }
        return res;
    }
}Min;

/*最大堆*/
struct maxHeap{
    int a[MAX];
    int num;
    
    int Top()
    {
        return a[1];
    }
    int getSize()
    {
        return num;
    }
    void Insert(int x)
    {
        a[++num] = x;
        int i = num;
        while(i > 1 && a[i >> 1] < a[i])
        {
            swap(a[i], a[i >> 1]);
            i >>= 1;
        }
    }
    int Pop()
    {
        int res = a[1];
        swap(a[1], a[num]);
        num --;
        int i = 1;
        while (i * 2 <= num)
        {
            int left = i << 1;
            if (left < num && a[left] < a[left + 1])
                left ++;
            if (a[i] < a[left])
            {
                swap(a[left], a[i]);
                i = left;
            }
            else break;
        }
        return res;
    }
}Max;

/*堆，需要后面声明op是哪个函数*/
struct heap{
    int a[MAX];
    int num;
    bool (*op)(int, int);
    int Top()
    {
        return a[1];
    }
    int getSize()
    {
        return num;
    }
    void Insert(int x)
    {
        a[++num] = x;
        int i = num;
        while(i > 1 && op(a[i >> 1], a[i]))
        {
            swap(a[i >> 1], a[i]);
            i >>= 1;
        }
    }
    int Pop()
    {
        int res = a[1];
        swap(a[1], a[num]);
        num --;
        int i = 1;
        while(i << 1 <= num)
        {
            int l = i << 1;
            if (l < num && op(a[l], a[l + 1])) l++;
            if (op(a[i], a[l]))
            {
                swap(a[i], a[l]);
                i = l;
            }
            else break;
        }
        return res;
    }
}iheap,aheap;

bool max(int a, int b)
{
    return a > b;
}
bool min(int a, int b)
{
    return a < b;
}
int main()
{
    int k;
    cout<<"case 1：建立小根堆"<<endl;
    for (int i = 1; i <= 10 ; i++)
    {
        cin >> k;
        Min.Insert(k);
    }
    for (int i = 1; i <= 10; i++)
    {
        cout<<Min.Top()<<" ";
        Min.Pop();
    }cout<<endl;
    cout<<"case 2：建立大根堆"<<endl;
    for (int i = 1; i <= 10 ; i++)
    {
        cin >> k;
        Max.Insert(k);
    }
    for (int i = 1; i <= 10; i++)
    {
        cout<<Max.Top()<<" ";
        Max.Pop();
    }cout<<endl;
    
    cout<<"case 3：同时建立大根堆和小根堆"<<endl;
    iheap.op = max;
    aheap.op = min;
    for (int i = 1; i <= 10; i++)
    {
        cin>>k;
        iheap.Insert(k);
        aheap.Insert(k);
    }
    for (int i = 1; i <= 10; i++)
    {
        cout<<iheap.Top()<<" ";
        iheap.Pop();
    }cout<<endl;
    for (int i = 1; i <= 10; i++)
    {
        cout<<aheap.Top()<<" ";
        aheap.Pop();
    }cout<<endl;
    
    return 0;
}
