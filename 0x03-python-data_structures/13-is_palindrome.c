#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_nodeint_at_index - get the nth node of linked list
 * @head: head of the list
 * @index: given index
 * Return: the nth node
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int pos = 0;

	while (head)
	{
		if (pos == index)
			return (head);

		head = head->next;
		pos++;
	}
	return (NULL);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: head of the list
 * Return: 1 if True 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	size_t list_length = 0, i = 0;
	bool palindrome_bool = TRUE;

	if (!head || !*head)
		return (1);

	node = *head;

	list_length = listint_len(*head);

	while (i != (list_length / 2) - 1)
	{
		if (node->n != get_nodeint_at_index(*head, list_length - 1 - i)->n)
			return (palindrome_bool = FALSE);

		i++;
		node = node->next;
	}
	return (palindrome_bool);
}

/**
 * listint_len - compute the size of linked list
 * @h: head of the list
 * Return: size of the list
 */
size_t listint_len(const listint_t *h)
{
	const listint_t *node = h;
	size_t size = 0;

	while (node)
	{
		node = node->next;
		size++;
	}

	return (size);
}
