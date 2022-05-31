#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: listint_t type, list to be checked
 *
 * Return: 1 if there is a cycle or 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;

	while (current != NULL)
	{
		for (temp = current->next; temp != NULL; temp=temp->next)
		{
			if (temp->next == NULL && current->next == NULL)
				return (0);
			if (temp == current)
				return (1);
		}
		current = current->next;
	}
	return (0);
}

