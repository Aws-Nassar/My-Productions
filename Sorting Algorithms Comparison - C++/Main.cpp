#include<iostream>
#include<chrono>
#include <time.h>
using namespace std;

void merge(int*, int, int, int);

void mergeSortSol(int*, int, int);

double mergeSort(int*, int);

int Partition(int*, int, int);

void quickSortSol(int*, int, int);

double quickSort(int*, int);

double insertionSort(int*, int);

double bubbleSort(int*, int);


void main(void)
{
	const int size = 100;
	int i = 0, j = 0;
	int Array[size] = {0}; // the values that we need to sort 
	double time[4] = {0};// this array will contain the time complexity

	//Set Random values for the Array

	for (i; i < size; i++)
	{
		Array[i] = rand() % 100;
	}
	/*
	for (i = 0; i < size; i++)
	{
		cout << Array[i] << '\t';
	}
	cout << endl << endl;
	*/
	string SortingAlgo[4] = { "Merge Sort", "Quick Sort", "Insertion Sort", "Bubble Sort" };

	time[0] = mergeSort(Array, size);
	time[1] = quickSort(Array, size);
	time[2] = insertionSort(Array, size);
	time[3] = bubbleSort(Array, size);
	
	string TEMP;
	double temp = 0.0;

	cout << endl << endl;
	for (i = 0; i < 4; i++)
	{
		for (j =  i + 1; j < 4; j++)
		{
			if (time[i] > time[j])
			{
				TEMP = SortingAlgo[i];
				temp = time[i];
				SortingAlgo[i] = SortingAlgo[j];
				time[i] = time[j];
				SortingAlgo[j] = TEMP;
				time[j] = temp;
			}
		}
	}

	for (i = 0; i < 4; i++)
	{
		cout << "The time needed to sort this array with " << SortingAlgo[i] << " = " << time[i] << " nano-second" << endl << endl;
	}

	
	return;
}


//--------------------------------------------------------\\
//***********************Merge Sort***********************\\

void merge(int* Arr, int p, int mid, int q)
{
	int* B = new int[q];
	int i = 0, j = 0, k = 0;
	i = p;
	j = mid + 1;
	k = i;

	while (i <= mid && j <= q)
	{
		if (Arr[i] <= Arr[j])
		{
			B[k] = Arr[i];
			i++;
			k++;
		}

		else if (Arr[i] > Arr[j])
		{
			B[k] = Arr[j];
			k++;
			j++;
		}
	}
	while (i <= mid)
	{
		B[k] = Arr[i];
		i++;
		k++;
	}

	while (j <= q)
	{
		B[k] = Arr[j];
		k++;
		j++;
	}
	for (k = p; k <= q; k++)
	{
		Arr[k] = B[k];
	}
	return;
}

void mergeSortSol(int* Arr, int left, int right)
{
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSortSol(Arr, left, mid);
		mergeSortSol(Arr, mid + 1, right);
		merge(Arr, left, mid, right);
	}
	return;
}

double mergeSort(int* Arr, int size)
{
	int left = 0, right = (size - 1);
	auto start = std::chrono::steady_clock::now();

	mergeSortSol(Arr, left, right);

	auto stop = std::chrono::steady_clock::now();
	double time = double(std::chrono::duration_cast <std::chrono::nanoseconds>(stop - start).count());

	/*
	cout << "The array after Merge Sort it with quick sort: \n";
	for (int i = 0; i < size; i++)
	{
		cout << Arr[i] << '\t';
	}
	cout << endl;
	*/
	return time;
}


//--------------------------------------------------------\\
//***********************Quick Sort***********************\\ 

int Partition(int* Arr, int Left, int Right)
{
	int first = Arr[Left], i = (Left + 1), j = Right, temp = 0;
	bool flag = false;

	while (!flag)
	{
		while ((Arr[i] <= first) && (i < Right))
		{
			++i;
		}

		while (Arr[j] >= first && j > Left)
		{
			--j;
		}

		if (i >= j)
		{
			temp = Arr[j];
			Arr[j] = Arr[Left];
			Arr[Left] = temp;
			return j;
		}
		else
		{
			temp = Arr[i];
			Arr[i] = Arr[j];
			Arr[j] = temp;
		}
	}

}

void quickSortSol(int* Arr, int Left, int Right)
{
	static int index = 0;
	if (Left < Right)
	{
		index = Partition(Arr, Left, Right);
		quickSortSol(Arr, Left, (index - 1));
		quickSortSol(Arr, (index + 1), Right);
	}
}

double quickSort(int* Arr, int size)
{
	int left = 0, right = (size - 1);
	auto start = std::chrono::steady_clock::now();

	quickSortSol(Arr, left, right);

	auto stop = std::chrono::steady_clock::now();
	double time = double(std::chrono::duration_cast <std::chrono::nanoseconds>(stop - start).count());

	/*
	cout << "The array after sort it with Quick sort: \n";
	for (int i = 0; i < size; i++)
	{
		cout << Arr[i] << '\t';
	}
	cout << endl;
	*/
	return time;
}


//--------------------------------------------------------\\
//***********************Insertion Sort***********************\\

double insertionSort(int* Arr, int size)
{
	int i, key, j;
	auto start = std::chrono::steady_clock::now();
    for (i = 1; i < size; i++)
    {
        key = Arr[i];
        j = i - 1;

        while (j >= 0 && Arr[j] > key)
        {
            Arr[j + 1] = Arr[j];
            j = j - 1;
        }
        Arr[j + 1] = key;
    }

	auto stop = std::chrono::steady_clock::now();
	double time = double(std::chrono::duration_cast <std::chrono::nanoseconds>(stop - start).count());
	/*
	cout << "The array after sort it with insertion sort: \n";
	for (i = 0; i < size; i++)
	{
		cout << Arr[i] << '\t';
	}
	cout << endl;
	*/
	return time;

}


//***********************Bubble Sort***********************\\ 
double bubbleSort(int* Arr, int size)
{
	int i = 0, j = 0, temp = 0;
	auto start = std::chrono::steady_clock::now();
	for (i; i < size; i++)
	{
		for (j = i + 1; j < size; j++)
		{
			if (Arr[i] > Arr[j])
			{
				temp = Arr[i];
				Arr[i] = Arr[j];
				Arr[j] = temp;
			}
		}
	}
	auto stop = std::chrono::steady_clock::now();
	double time = double(std::chrono::duration_cast <std::chrono::nanoseconds>(stop - start).count());

	/*
	cout << "The array after sort it with bubble sort: \n";
	for (i = 0; i < size; i++)
	{
		cout << Arr[i] << '\t';
	}
	cout << endl;
	*/
	
	return time;
}

