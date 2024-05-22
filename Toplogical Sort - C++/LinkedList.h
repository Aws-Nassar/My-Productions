#pragma once
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