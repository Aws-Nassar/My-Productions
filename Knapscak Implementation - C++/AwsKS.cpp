//Aws Nassar
//12027708
#include<iostream>
using namespace std;

int max(int x, int y) 
{
	if (x > y)
		return x;
	else
		return y;
}

void Knapsack(int* list, int* sackCapacity, int size, int maxWeight)
{
	int i = 0, j = 0, maxValue = 0;

	int** Matrix = new int* [size + 1];
	for (int i = 0; i < size + 1; i++)
	{
		Matrix[i] = new int[maxWeight + 1];
	}

	if (maxWeight <= 0)
	{
		return;
	}
	if (size <= 0)
	{
		return;
	}

	for (i = 0; i <= size; i++)
	{
		for (j = 0; j <= maxWeight; j++)
		{
			if (i == 0 || j == 0)
			{
				Matrix[i][j] = 0;
			}

			else if (sackCapacity[i - 1] <= j)
			{
				Matrix[i][j] = max((list[i - 1] + Matrix[i - 1][j - sackCapacity[i - 1]]), Matrix[i - 1][j]);
			}

			else
				Matrix[i][j] = Matrix[i - 1][j];
		}
	}

	maxValue = Matrix[size][maxWeight];
	cout << "\n--------------------------------------------------------\n\n";
	cout << "The maximum value = " << maxValue << endl;
	cout << "\n--------------------------------------------------------\n\n";
	cout << "The whole matrix used to compute the maximum value: \n";

	for (i = 0; i <= size; i++)
	{
		for (j = 0; j <= maxWeight; j++)
		{
			cout << Matrix[i][j] << " || ";
		}
		cout << endl;
	}
	cout << "\n--------------------------------------------------------\n\n";
	cout << " The list of selected items is: \n";

	j = maxWeight;

	for (i = size; i > 0 && maxValue > 0; i--)
	{
		if (maxValue == Matrix[i - 1][j])
		{
			continue;
		}

		else
		{
			cout << sackCapacity[i - 1] << '\t';

			maxValue = maxValue - list[i - 1];
			j = j - sackCapacity[i - 1];
		}
	}
}

int main()
{
	int size = 0, i = 0, j = 0, maxWeight = 0;
	cout << "Enter the number of list: ";
	cin >> size;
	cout << endl;
	int* list = new int[size];
	int* sackCapacity = new int[size];

	for (i; i < size; i++)
	{
		cout << "Enter value " << i + 1 << " = ";
		cin >> list[i];
	}

	cout << endl;

	for (i = 0; i < size; i++)
	{
		cout << "Enter weight " << i + 1 << " = ";
		cin >> sackCapacity[i];
	}
	cout << endl;
	
	cout << "Enter the max weight = ";
	cin >> maxWeight;

	Knapsack(list, sackCapacity, size, maxWeight);
	
	return 0;
}