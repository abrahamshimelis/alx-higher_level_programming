#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a singly linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node = list;
	listint_t *next_node;
	
	if (!current_node)
		return (0);

	while(current_node->next)
	{
		next_node = current_node->next;
		if (current_node == next_node)
			return (1);
		else
			current_node = next_node;
	}

	return (0);

}
