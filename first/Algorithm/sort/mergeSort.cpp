#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;

/*将a[first...mid]和a[mid+1...last]合并*/
void MergeArray(int a[], int first, int mid, int last)
{
	int *b = new int[last + 1];
	int i = first, j = mid + 1, k = first;
	while(i <= mid && j <= last)
	{
		if(a[i] < a[j])
		{
			b[k++] = a[i++];
		}
		else
			b[k++] = a[j++];
	}

	while(j <= last)
	{
		b[k++] = a[j++];
	}

	while(i <= mid)
	{
		b[k++] = a[i++];
	}

	for(i = first; i <= last; i++)
	{
		a[i] = b[i];
	}
	delete b;
}

void MergeSort(int a[], int first, int last)
{
	if(first < last)
	{
		int mid = (last + first) / 2;
		MergeSort(a, first, mid);
		MergeSort(a, mid + 1, last);
		MergeArray(a, first, mid, last);
	}
}
int main()
{
	
	int A[] = {2, 3,4,2,4,5,2,5};
	MergeSort(A, 0, 7);
	for (int i = 0; i < 8; i++)
	{
		cout<<A[i]<<" ";
	}cout<<endl;
	return 0;
}