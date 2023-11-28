#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - ths function checks if list
 * is cyclical
 *
 * @list: pointer to list
 * Return: 1 if success, else 0
 */
int check_cycle(listint_t *lst)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
