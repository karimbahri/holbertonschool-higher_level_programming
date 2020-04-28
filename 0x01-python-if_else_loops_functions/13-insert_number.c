#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert sorted list
 * @head: head of the list
 * @number: containing of the node
 * Return: head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp, *n;

	if (!head)
		return (NULL);

	n = *head;

	node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);

	node->n = number;

	while (n && n->next)
	{
		if (n->next->n > number)
		{
			tmp = n->next;
			n->next = node;
			node->next = tmp;
		}
		n = n->next;
	}
	return (*head);
}
