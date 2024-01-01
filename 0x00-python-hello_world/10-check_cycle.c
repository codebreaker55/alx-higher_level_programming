#include "lists.h"
#include <stdio..h>
#include <stdlib.h>

/**
 * check_cycle - a function that checks if a linked list has cycle
 *
 * @listint: is a pointer to the list that will be checked
 *
 * Return: if there is a cycle return 1, otherwise return 0
*/

int check_cycle(listint_t *listint)
{
	listint_t *x = listint, *y = listint;

	while (x != NULL && x->next)
	{
		y = y->next;
		x = x->next->next;
		if (y == x)
		{
			return (1);
		}
	}
	return (0);
}
