#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * is_palindrome - a function that recrusives palind or not
 *
 * @head: is the head of the list
 *
 * Return: if not a palindrome return 0, else return 1
*/

int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
	{
		return (1);
	}
	return (check_palind(head, *head));
}

/**
 * check_palind - a function to know if a singly linked list is a palindrome
 *
 * @head: is the head of the list
 * @end: is the end of the list
 *
 * Return: 1 if it is palindrome, 0 if it is not
*/

int check_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
	{
		return (1);
	}
	if (check_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
