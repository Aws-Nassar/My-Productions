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

//--------------------------------

void printTree(node* n, string s, code* h[]);

void main(void)
{
	const int index = 5;
	int size = index;
	int i = 0, j = 0;
	char Arr[index] = { 'a','b','c','d','e' };
	int freq[index] = { 0 };

	string s;
	cout << "Enter a paragraph:" << endl;
	getline(cin, s);

	cout << endl;

	for (i = 0; i < s.length(); i++)
	{
		for (j = 0; j < index; j++)
		{
			if (s[i] == ' ')
			{
				break;
			}
			else if (s[i] == Arr[j])
			{
				freq[j]++;
				break;
			}
		}
	}

	cout << "characters and there frequancy: \n";
	for (i = 0; i < index; i++)
	{
		cout << Arr[i] << "->" << freq[i] << '\n';
	}

	node* arrNode[index];

	for (i = 0; i < index; i++)
	{
		arrNode[i] = new node(Arr[i], freq[i]);
	}
	for (i = 0; i < index; i++) {
		for (j = 0; j < index - 1; j++) {
			if (arrNode[j]->getFreq() > arrNode[j + 1]->getFreq())
			{
				node* temp = arrNode[j];
				arrNode[j] = arrNode[j + 1];
				arrNode[j + 1] = temp;
			}
		}
	}

	int Min1 = 0;
	int Min2 = 0;

	while (size > 1)
	{
		Min1 = 0;
		Min2 = 1;
		node* z = new node('?', 0);
		z->setLeft(arrNode[Min1]);
		z->setRight(arrNode[Min2]);
		z->setFreq(arrNode[Min1]->getFreq() + arrNode[Min2]->getFreq());
		z->setVisited(true);
		for (i = 0; i < size - 2; i++) {
			arrNode[i] = arrNode[i + 2];
		}
		arrNode[i] = z;
		size--;
		for (i = 0; i < size; i++) {
			for (j = 0; j < size - 1; j++) {
				if (arrNode[j]->getFreq() > arrNode[j + 1]->getFreq())
				{
					node* temp = arrNode[j];
					arrNode[j] = arrNode[j + 1];
					arrNode[j + 1] = temp;
				}
			}
		}
	}
	cout << "_____________________________________________" << endl;
	cout << "huffman code is: \n\n";
	code* huffman[index];
	printTree(arrNode[0], "", huffman);
	for (i = 0; i < index; i++) {
		cout << huffman[i]->c << " -- " << huffman[i]->bit << endl;
	}

	cout << "_____________________________________________" << endl;
	cout << "The binary code of this string is: \n\n";

	int sumBit = 0;
	for (i = 0; i < s.length(); i++)
	{
		for (j = 0; j < index; j++)
		{
			if (s[i] == ' ')
			{
				cout << ' ';
				break;
			}
			else if (s[i] == huffman[j]->c)
			{
				cout << huffman[j]->bit;
				sumBit += huffman[j]->bit.length();
			}
		}
	}
	cout << endl;
	cout << " number of bits needed to encode this paragraph = " << sumBit;
	cout << endl;
	string bc;

	cout << "_____________________________________________" << endl;
	cout << "Enter a binary code to be converted to string: \n\n";
	getline(cin, bc);
	node* temp = arrNode[0];
	cout << endl;
	cout << "The string is: \n";
	for (i = 0; i < bc.length(); i++)
	{
		if (bc[i] == ' ' || bc[i] < '0' || bc[i] > '1')
		{
			i++;
		}
		else
		{
			if (bc[i] == '0')
			{
				temp = temp->getLeft();
			}
			else if (bc[i] == '1')
			{
				temp = temp->getRight();
			}
			if (temp->getRight() == NULL && temp->getLeft() == NULL)
			{
				cout << temp->getCharacter();
				temp = arrNode[0];
			}
		}
	}

	return;

}
void printTree(node* n, string s, code* h[]) {
	static int index = 0;
	if (n != NULL) {
		if (n->getVisited() == false) {
			h[index] = new code;
			h[index]->c = n->getCharacter();
			h[index]->bit = s;
			index++;
		}
		else {
			printTree(n->getLeft(), s + "0", h);

			printTree(n->getRight(), s + "1", h);

		}

	}

}