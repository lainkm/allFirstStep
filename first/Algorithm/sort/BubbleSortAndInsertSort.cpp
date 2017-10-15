#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;

void BubbleSort(int a[], int n)
{
	for (int i = n - 1; i >= 1; i--)
	{
		bool Swap = false;
		for (int j = 0; j <= i - 1; j++)
		{
			if (a[j] > a[j + 1])
			{
				swap(a[j], a[j + 1]);
				Swap = true;
			}
		}
		if (!Swap) break;
	}
}

void InsertSort(int a[], int n)
{
	int x, j;
	for (int i = 1; i < n; i++)
	{
		x = a[i];
		j = i - 1;
		while(j > 0 && a[j] > x)
		{
			a[j + 1] = a[j];
			j--;
		}
		a[j + 1] = x;
	}
}

int main()
{
	int A[] = {2, 3,4,2,4,5,2,5};
	BubbleSort(A, 7);
	for (int i = 0; i < 8; i++)
	{
		cout<<A[i]<<" ";
	}cout<<endl;

	int B[] = {2, 3,4,2,4,5,2,5};
	InsertSort(B, 7);
	for (int i = 0; i < 8; i++)
	{
		cout<<B[i]<<" ";
	}cout<<endl;

	return 0;
}