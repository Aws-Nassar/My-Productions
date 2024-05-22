#include<iostream>
using namespace std;
class node
{
private:
	int Info;
	node* next;
public:
	node(int AWS = 0) : next(NULL)
	{
		setInfo(AWS);
	}
	~node()
	{
		setNext(NULL);
	}
	inline void setInfo(int T = 0)
	{
		Info = T;
	}
	inline void setNext(node* S)
	{
		next = S;
	}
	inline int getInfo()const
	{
		return Info;
	}
	inline node* getNext()const
	{
		return next;
	}
};
class Linked
{
private:
	node* Root;
public:
	Linked(node* A = NULL)
	{
		setRoot(A);
	}
	inline void setRoot(node* a)
	{
		Root = a;
	}
	inline node* getRoot()const
	{
		return Root;
	}
	void inseartAtHead(int v = 0)
	{
		node* q = new node(v);
		q->setNext(Root);
		setRoot(q);
	}
	void insertAtTail(int a = 0)
	{
		node* A = new node(a);
		if (getRoot() == NULL)
			setRoot(A);
		else
		{
			node* B = getRoot();
			while (B->getNext() != NULL)
				B = B->getNext();
			B->setNext(A);
		}
	}
	int deleteAtHead()
	{
		int R = -999;
		if (Root)
		{
			node* A = Root;
			setRoot(getRoot()->getNext());
			R = A->getInfo();
			delete A;
		}
		return R;
	}
	int deleteAtTail()
	{
		int R = -999;
		if (getRoot() && getRoot()->getNext() == NULL)
		{
			R = getRoot()->getInfo();
			delete Root;
			setRoot(NULL);
		}
		else if (getRoot())
		{
			node* curr = getRoot();
			node* prev = getRoot();
			while (curr->getNext())
			{
				prev = curr;
				curr = curr->getNext();
			}
			R = curr->getInfo();
			prev->setNext(NULL);
			delete curr;
			curr = NULL;
		}
		return R;
	}
	void print() const
	{
		node* curr;
		if (getRoot() == NULL)
		{
			cout << " Not linked with anything." << endl;
			return;
		}
		curr = getRoot();
		while (curr != NULL)
		{
			cout << curr->getInfo();
			if(curr->getNext())
				cout << " -> ";
			curr = curr->getNext();
		}
		cout << endl;
	}
};

//-----------------------------------------------------

class Stack
{
private:
	Linked L;
public:
	Stack() : L()
	{

	}
	int isEmpty()const
	{
		return (L.getRoot() == NULL);
	}
	int full()const
	{
		return false;
	}
	void push(int A = 0)
	{
		if (!full())
			L.inseartAtHead(A);
	}
	int pop()
	{
		int A = -999;
		if (!isEmpty())
			A = L.deleteAtHead();
		return A;
	}
	int getTop()
	{
		int a = L.getRoot()->getInfo();
		return a;
	}
};
class Queue
{
private:
	Linked L;
public:
	Queue() : L()
	{

	}
	~Queue()
	{

	}
	int isEmpty()const
	{
		return L.getRoot() == NULL;
	}
	int full()const
	{
		return false;
	}
	void addQueue(int A = 0)
	{
		if (!full())
			L.insertAtTail(A);
	}
	int deleteQueue()
	{
		int A = -999;
		if (!isEmpty())
			A = L.deleteAtHead();
		return A;
	}
	int qfront()
	{
		int a = L.getRoot()->getInfo();
		return a;
	}
};

//-----------------------------------------------------

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