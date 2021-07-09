#include "menger.h"
/**
 * character - # or blank space
 * @row: row.
 * @col: col.
 * Return: # or blank space
 */
char character(int row, int col)
{
	while (row || col)
	{
		if (row % 3 == 1 && col % 3 == 1)
			return (' ');
		row = row / 3;
		col = col / 3;
	}
	return ('#');
}

/**
 * menger - an awesome menger sponge in 2D
 * @level: draw level
 */
void menger(int level)
{
	int size, row, col;
	char character;

	size = pow(3, level);

	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
		{
			character = character(row, col);
			printf("%c", character);
		}
		printf("\n");
	}
}

