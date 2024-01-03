#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - is a function that inserts a number
 *	into a sorted singly linked list
 *
 * @head: is the address of the head pointer
 * @number: is the number that will be inserted
 *
 * Return: the node after it get inserted
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *n_node = malloc(sizeof(listint_t));

	if (n_node == NULL)
	{
		return (NULL);
	}
	n_node->n = number;
	n_node->next = NULL;

	if (node == NULL || n_node->n < node->n)
	{
		n_node->next = node;
		return (*head = n_node);
	}
	while (node != NULL)
	{
		if (n_node->n < node->next->n || node->next == NULL)
		{
			n_node->next = node->next;
			node->next = n_node;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
