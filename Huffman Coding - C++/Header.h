#pragma once
//Aws Ahmad Nassar
//12027708
#include<iostream>
#include <string>
using namespace std;

class node
{
private:
	int Freq;
	char character;
	node* right;
	node* left;
	bool visited;

public:
	node(char a = ' ', int b = -1) : right(NULL), left(NULL)
	{
		setVisited(false);
		setCharacter(a);
		setFreq(b);
	}
	~node()
	{
		setRight(NULL);
		setLeft(NULL);
	}
	inline void setFreq(int T = 0)
	{
		Freq = T;
	}
	inline void setCharacter(char T = ' ')
	{
		character = T;
	}
	inline void setRight(node* S)
	{
		right = S;
	}
	inline void setVisited(bool T = false)
	{
		visited = T;
	}
	inline void setLeft(node* S)
	{
		left = S;
	}
	inline int getFreq()const
	{
		return Freq;
	}
	inline char getCharacter()const
	{
		return character;
	}
	inline bool getVisited()const
	{
		return visited;
	}
	inline node* getRight()const
	{
		return right;
	}
	inline node* getLeft()const
	{
		return left;
	}
};

struct code
{
	char c;
	string bit;
};