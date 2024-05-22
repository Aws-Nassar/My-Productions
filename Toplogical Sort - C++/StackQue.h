#pragma once
#include"LinkedList.h"
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