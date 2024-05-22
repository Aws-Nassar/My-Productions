#pragma once
#include"StackQue.h"

void countIn(Linked* A, int* B, int* c, int size)
{
	int count = 0, flag = 0;
	node* curr;
	for (int i = 0; i < size; i++) // for find the count for each cell
	{
		curr = A[i].getRoot();
		while (curr != NULL)
		{
			for (int j = 0; j < size && flag != 1; j++)
			{
				if (curr->getInfo() == c[j])
				{
					B[j]++;
					flag = 1;
				}
			}
			flag = 0;
			curr = curr->getNext();
		}
	}
}

void reduceLinks(Linked* A, int* B,int* c, int size, int z)
{
	if (A[z].getRoot() == NULL)
		return;
	node* curr;
	bool flag = false;
	curr = A[z].getRoot();
	while (curr != NULL)
	{
		for (int j = 0; j < size && flag != 1; j++)
		{
			if (curr->getInfo() == c[j])
			{
				B[j]--;
				flag = 1;
			}
		}
		flag = 0;
		curr = curr->getNext();
	}
}

int main(void)
{
	const int size = 6;     // Elements counter
	int i = 0, j = 0, flag = 0, index = 0;     // loop,counter(stop case),flag(stop case),place holder
	Linked Topologic;    // to store the elements that topologicaly sorted
	int arr[size] = { 0,1,2,3,4,5 };     // The orignal array values
	int inDegree[size] = {0};     // to store the count of indegree for each node in parallel with the original array
	Linked list[size];     // the adjusant list(array contain pointers each one of them point to an linked list in parallel with the original array
	Stack S;
	Queue Q;
	list[2].inseartAtHead(3);
	list[3].inseartAtHead(1);
	list[4].inseartAtHead(1);
	list[4].insertAtTail(0);
	list[5].inseartAtHead(0);
	list[5].insertAtTail(2);

	countIn(list, inDegree, arr, size);     // find the indegree count for each node

	cout << "\n\n\tThe array is:- \n\n";
	for (i = 0; i < size; i++)
		cout << "\t" << arr[i] << "\t";

	cout << "\n\t--------------------------------------------------------------------------------------------- ";
	cout << "\n\tThe Adjacency List of these values is:\n\n";
	for (i = 0; i < size; i++)
	{
		cout << "\t" << arr[i] << " -> ";
		list[i].print();
		cout << endl;
	}

	cout << "\t--------------------------------------------------------------------------------------------- ";
	cout << "\n\tThe in Degree array is:- \n\n";
	for (i = 0; i < size; i++)
	{
		cout << "\t" << inDegree[i] << endl << endl;
	}

	cout << endl;
	//***************************Stack*************************\\ 

	while (flag != 1)
	{
		for (i = 0; i < size; i++)
		{
			if (inDegree[i] == 0)
			{
				inDegree[i] = -1;
				S.push(arr[i]);
			}		
		}

		if(!S.isEmpty())
		{
			index = S.getTop();
			for(i = 0; i < size; i++)
				if (index == arr[i])
				{
					index = i;
					break;
				}
			reduceLinks(list, inDegree, arr, size,index);
			Topologic.insertAtTail(S.pop());
			j++;
		}
		if (j == size)
		{
			flag = 1;
		}

	}
	cout << "\t--------------------------------------------------------------------------------------------- ";
	cout << "\n\tUsing Stack:- \n" << endl;
	cout << "\t";
	Topologic.print();

	//***************************Queue*************************\\ 

	Topologic.setRoot(NULL); // make the toplogical list empty

	for (i = 0; i < size; i++)
		inDegree[i] = 0;// return it to the 0 values to re count the in degree

	countIn(list, inDegree, arr, size);
	j = 0;// re find the new count
	flag = 0;

	while (flag != 1)
	{
		for (i = 0; i < size; i++)
		{
			if (inDegree[i] == 0)
			{
				inDegree[i] = -1;
				Q.addQueue(arr[i]);
			}
		}

		if (!Q.isEmpty() )
		{
			index = Q.qfront();
			for (i = 0; i < size; i++)
				if (index == arr[i])
				{
					index = i;
					break;
				}
			reduceLinks(list, inDegree, arr, size, index);
			Topologic.insertAtTail(Q.deleteQueue());
			j++;
		}
		if (j == size)
		{
			flag = 1;
		}

	}
	cout << "\t--------------------------------------------------------------------------------------------- ";
	cout << "\n\tUsing Queue:- \n" << endl;
	cout << "\t";
	Topologic.print();

	return 0;
}