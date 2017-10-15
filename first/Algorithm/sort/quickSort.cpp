#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;

/*定义写法*/
int partition(int a[], int low, int high)
{
	int pivot = a[high];
	int i = low - 1;
	for (int j = low; j <= high - 1; j++)
	{
		if(a[j] < pivot)
		{
			i ++;
			if (i < j)
			{
				swap(a[i], a[j]);
			}
		}
	}
	if (a[high] < a[i + 1])
	{
		swap(a[i + 1], a[high]);
	}
	return i + 1;
}

void quickSort(int a[], int low, int high)
{
	if(low < high)
	{
		int p = partition(a, low, high);
		quickSort(a, low, p - 1);
		quickSort(a, p + 1, high);
	}
}

/*快排模板*/
void qsort(int a[], int l,int r)
{

    if(l >= r)
        return;

    int i = l;
    int j = r;
    int standard = a[l];

    while(i < j)
    {
        while( i < j && a[i] < standard) ++i;
        while( i < j && a[j] > standard) --j;

        swap(a[i],a[j]);
    }
    // i == j where the standard should be

    qsort(a, l, i - 1);
    qsort(a, i + 1, r);
}


/*求第k小数*/
void ksort(int a[], int l, int r, int k)
{
    int i = l;
    int j = r;
    int mid = a[(l + r) / 2];
    do
    {
        while(a[i] < mid) ++i;
        while(a[j] > mid) --j;
        if(i <= j)
        {
            swap(a[i], a[j]);
            ++i;
            --j;
        }
    }
    while(i <= j);

    if(l <= j && k <= j - l + 1) ksort(a, l, j, k);
    if(i <= r && k >= i - l + 1) ksort(a, i, r, k - (i - 1));
}



int main()
{
	int A[] = {2, 3,4,2,4,5,2,5};
	quickSort(A, 0, 7);
	for (int i = 0; i < 8; i++)
	{
		cout<<A[i]<<" ";
	}cout<<endl;
	return 0;
}
