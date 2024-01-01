#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a function that checks if a linked list has cycle
 *
 * @l_list: is a pointer to the list that will be checked
 *
 * Return: if there is a cycle return 1, otherwise return 0
*/

int check_cycle(listint_t *l_list)
{
	listint_t *x = l_list, *y = l_list;

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
