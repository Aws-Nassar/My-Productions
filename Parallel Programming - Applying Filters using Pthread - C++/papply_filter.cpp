//Aws Ahmad Nassar
//12027708
#include<iostream>
#include<fstream>
#include<string>
#include<pthread.h>
#include <sys/time.h>
using namespace std;

double GetWallTime();
void *applyMask(void *rank);

long rowCount;
long colCount;
double **originalImgMatrix;
double **newImgMatrix;
double kernel[3][3];
int threadNum; 
  
int main(int argc, char *argv[])
{
	long i = 0,j = 0;
	pthread_t * threads; 
	
	// I need to check if the user enter 3 parameters from cmd
	if(argc < 5)
	{
		cout << "you need to enter 3 text files name from the cmd" << endl;
		return 1;
	}
	
	string originalImage = argv[1];
	string mask = argv[2];
	string newImage = argv[3];
	threadNum = strtol(argv[4], NULL, 10);
	
	threads = (pthread_t*)malloc(threadNum * sizeof(pthread_t));
	
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
    // Thread Creation
    for(i = 0; i < threadNum; i++)
    {
        pthread_create(&threads[i],NULL, applyMask, (void*)i);
    }
    
    for(i = 0; i < threadNum; i++)
    {
        pthread_join(threads[i],NULL);
    }
    
    double finish = GetWallTime();
    cout << "---------->Parallel code with " << threadNum << " thread/s elapsed time = " << finish - start << endl << endl;
    
    free(threads);
    
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

void *applyMask(void *rank)
{
	long i, j, x, y;
	double sum;
	long my_rank = (long)rank;
	long local_row = rowCount / threadNum;
    long my_first_row = my_rank * local_row;
    long my_last_row = (my_rank + 1) * local_row - 1;
    
    if (my_rank == threadNum - 1)
	{
		my_last_row = rowCount - 1;
	}
	
	// to be sure that we take the whole image (solve divide odd / even problem)
	
	for(i = my_first_row; i <= my_last_row; i++) 
	{
		for(j = 0; j < colCount; j++) 
		{
			sum = 0.0;
			for(x = -1; x <= 1; x++)
			{
				for(y = -1; y <= 1; y++)
				{
					if(((i + x) >= 0) && ((i + x) < rowCount) && ((j + y) >= 0) && ((j + y) < colCount)) // check if the pixel inside the boundery of the matrix
                    {
                        sum += originalImgMatrix[i + x][j + y] * kernel[x + 1][y + 1];
                    }
				}
			}
			//keep the gray scale boundary
			if(sum > 255)
				sum = 255;
				
			else if(sum < 0)
				sum = 0;
				
			newImgMatrix[i][j] = sum;
		}
	}
	return nullptr;
}

double GetWallTime() 
{
    struct timeval tp;
    int rtn = gettimeofday(&tp, NULL);
    return ((double) tp.tv_sec + (1.e-6)*tp.tv_usec);
}
