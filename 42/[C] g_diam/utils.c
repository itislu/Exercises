#include "g_diam.h"
#include <stdlib.h>
#include <unistd.h>

bool	append_link(t_link **head, int n, int m)
{
	t_link	*new_link;
	t_link	*current;

	new_link = (t_link *)malloc(sizeof(t_link));
	if (new_link == NULL)
		return false;
	new_link->n.nbr = n;
	new_link->m.nbr = m;
	new_link->n.index = -1;
	new_link->m.index = -1;
	new_link->next = NULL;

	if(*head == NULL)
		*head = new_link;
	else
	{
		current = *head;
		while(current->next != NULL)
			current = current->next;
		current->next = new_link;
	}
	return true;
}

void	free_links(t_link **head)
{
	t_link	*next;

	while (*head)
	{
		next = (*head)->next;
		free(*head);
		*head = next;
	}
}

void	free_matrix(bool **matrix, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		free(matrix[i]);
		i++;
	}
	free(matrix);
}

int	ft_atoi(char *str)
{
	int	n;
	int	i;
	int	sign;

	n = 0;
	i = 0;
	sign = 1;
	if (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (ft_isdigit(str[i]))
	{
		n = n * 10 + (str[i] - '0');
		i++;
	}
	return (n * sign);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	void			*new;
	unsigned char	*ptr;
	size_t	i;
	size_t	j;

	new = malloc(nmemb * size);
	if (!new)
		return (NULL);
	i = 0;
	while (i < nmemb)
	{
		ptr = &new[i];
		j = 0;
		while (j < size)
			ptr[j++] = (unsigned char)0;
		i++;
	}
	return (new);
}

bool	ft_isdigit(char c)
{
	return (c >= '0' && c <= '9');
}

void	ft_putnbr(int n)
{
	char	c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

void	goto_next_nbr(char *str, int *i)
{
	bool	is_past_separator;

	if (str[*i] == '+' || str[*i] == '-')
		(*i)++;
	while (ft_isdigit(str[*i]))
		(*i)++;
	is_past_separator = false;
	while (str[*i] && !ft_isdigit(str[*i]))
	{
		if (str[*i] == '-' || str[*i] == ' ')
		{
			if (is_past_separator && str[*i] == '-' && ft_isdigit(str[*i + 1]))
				break ;
			else
			 	is_past_separator ^= true;
		}
		(*i)++;
	}
}
