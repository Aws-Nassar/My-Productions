//Aws Ahmad Nassar
//12027708
#include<iostream>
#include<fstream>
#include<string>
#include <sys/time.h>
using namespace std;

double GetWallTime();
void applyMask(double** Img, double** newImg, double kernel[][3], long row, long col);

int main(int argc, char *argv[])
{
    long rowCount;
    long colCount;

    double **originalImgMatrix;
    double **newImgMatrix;
    double kernel[3][3];

	long i = 0,j = 0;
	// I need to check if the user enter 3 parameters from cmd
	if(argc < 4)
	{
		cout << "you need to enter 3 text files name from the cmd" << endl;
		return 1;
	}
	
	string originalImage = argv[1];
	string mask = argv[2];
	string newImage = argv[3];
	
	// First we need to read the matrix values from the original image file 
	
	// Check if the file open correctly or not
	ifstream inputImg(originalImage);
	if(!inputImg.is_open())
	{
        cout << "Error opening the file" << endl;
        return 1;
    }
    
    // First thing we need to read rows and cloumns count from the file first line
    inputImg >> rowCount;
    inputImg >> colCount;
    
    originalImgMatrix = new double*[rowCount];
    for(i = 0; i < rowCount; i++) 
    {
        originalImgMatrix[i] = new double[colCount];
    }
    
    for(i = 0; i < rowCount; i++) 
    {
		for(j = 0; j < colCount; j++)
		{
			inputImg >> originalImgMatrix[i][j];
		}
    }
    
    inputImg.close();
    
    // Declare the output matrix
    newImgMatrix = new double*[rowCount];
    for(i = 0; i < rowCount; i++) 
    {
        newImgMatrix[i] = new double[colCount];
    }
    
    // Then we need to read the mask values from the make file 
	ifstream maskInput(mask);
	
	// Check if the file open correctly or not
	if(!maskInput.is_open())
	{
        cout << "Error opening the file" << endl;
        return 1;
    }
    
    // Applied Kernel Matrix
    for(i = 0; i < 3; i++) 
    {
		for(j = 0; j < 3; j++)
		{
			maskInput >> kernel[i][j];
		}
    }
    
    maskInput.close();
    
    double start = GetWallTime();
    
    applyMask(originalImgMatrix,newImgMatrix,kernel,rowCount,colCount);
    
    double finish = GetWallTime();
    cout << "---------->Serial code elapsed time = " << finish - start << endl << endl;
    
    // Write the new image matrix on the output file
    ofstream outputImg(newImage);
    
    outputImg << rowCount << " " << colCount << "\n"; // To keep the form of the input file as mentioned in the assignment
    
    for(i = 0; i < rowCount; i++) 
    {
		for(j = 0; j < colCount; j++) 
		{
			outputImg << newImgMatrix[i][j] << " "; 
		}
		outputImg << "\n";
	}
    
    return 0;	  	 
}

void applyMask(double** Img, double** newImg, double kernel[][3], long row, long col)
{
	long i, j, x, y;
	double sum;
	for(i = 0; i < row; i++) 
	{
		for(j = 0; j < col; j++) 
		{
			sum = 0.0;
			for(x = -1; x <= 1; x++)
			{
				for(y = -1; y <= 1; y++)
				{
					if(((i + x) >= 0) && ((i + x) < row) && ((j + y) >= 0) && ((j + y) < col)) // check if the pixel inside the boundery of the matrix
                    {
                        sum += Img[i + x][j + y] * kernel[x + 1][y + 1];
                    }
				}
			}
			//keep the gray scale boundary
			if(sum > 255)
				sum = 255;
				
			else if(sum < 0)
				sum = 0;
				
			newImg[i][j] = sum;
		}
	}
}

double GetWallTime() 
{
    struct timeval tp;
    int rtn = gettimeofday(&tp, NULL);
    return ((double) tp.tv_sec + (1.e-6)*tp.tv_usec);
}
