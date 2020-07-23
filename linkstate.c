#include <stdio.h>
#include <string.h>
#define INF 999

int main()
{
	int count, src, i, j, k, min, minIndex;

	int c_mat[100][100];
	int dist[100], proc[100];


	printf("Number Of Routers: ");
	scanf("%d", &count);

	printf("Cost Matrix:\n");
	for(i = 0 ; i < count ; i++)
	{
		dist[i] = INF;
		proc[i] = 0;
		for(j = 0; j < count; j++)
		{
			printf ("%d->%d:", i, j);
			scanf ("%d", &c_mat[i][j]);
			if(c_mat[i][j]<0) c_mat[i][j] = 999;
		}
	}

	printf("Source Router: ");
	scanf("%d", &src);

	for(i = 0; i <count; i++)
		dist[i] = c_mat[src][i];

	proc[src] = 1;

	for(i = 0; i < count; i++){
		minIndex=0;
		min = INF;
		for(j = 0; j < count; j++)
		{
			if(!proc[j] && dist[j] < min)
			{
				min = dist[j];
				minIndex = j;
			}
		}

		printf("min index is %d -%d ", minIndex, min);
		proc[minIndex] = 1;

		for(j = 0; j < count; j++)
		{
			if(!proc[j]  && dist[minIndex]+c_mat[minIndex][j]< dist[j])
			{
				dist[j] = dist[minIndex]+c_mat[minIndex][j];
			}
		}
	}

	for(i = 0 ; i < count ; i++)
	{
		printf ("%d-->%d: SP %d\n", src, i, dist[i]);
	}

}
