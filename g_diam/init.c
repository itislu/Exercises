#include "g_diam.h"
#include <stdlib.h>

static void		set_duplicates(t_link *links, int number, int index);
static t_link	*parse_links(char *str);
static int		set_indeces(t_link *links);
static bool		*init_is_visited_array(int unique_numbers);
static bool		**init_is_linked_matrix(int unique_numbers);
static void		fill_is_linked_matrix(bool **is_linked, t_link *links);

bool	init(
			bool ***is_linked,
			bool **is_visited,
			int *unique_numbers,
			char *input)
{
	t_link	*links;

	links = parse_links(input);
	if (!links)
		return (false);
	*unique_numbers = set_indeces(links);

	*is_visited = init_is_visited_array(*unique_numbers);
	if (*is_visited == NULL)
	{
		free_links(&links);
		return (false);
	}
	*is_linked = init_is_linked_matrix(*unique_numbers);
	if (*is_linked == NULL)
	{
		free(*is_visited);
		free_links(&links);
		return (false);
	}
	fill_is_linked_matrix(*is_linked, links);
	free_links(&links);
	return (true);
}

static t_link	*parse_links(char *str)
{
	t_link	*links;
	int 	n;
	int 	m;
	int		i;

	links = NULL;
	i = 0;
	while (str[i])
	{
		n = ft_atoi(&str[i]);
		goto_next_nbr(str, &i);
		m = ft_atoi(&str[i]);
		goto_next_nbr(str, &i);
		if (!append_link(&links, n, m))
		{
			free_links(&links);
			return (NULL);
		}
	}
	return (links);
}

static int	set_indeces(t_link *links)
{
	int		index;
	t_link	*cur;

	index = 0;
	cur = links;
	while (cur)
	{
		if (cur->n.index == -1)
		{
			set_duplicates(links, cur->n.nbr, index);
			index++;
		}
		cur = cur->next;
	}
	cur = links;
	while (cur)
	{
		if (cur->m.index == -1)
		{
			set_duplicates(links, cur->m.nbr, index);
			index++;
		}
		cur = cur->next;
	}
	return (index + 1);
}

static void	set_duplicates(t_link *links, int number, int index)
{
	while (links)
	{
		if(links->n.nbr == number)
			links->n.index = index;
		if(links->m.nbr == number)
			links->m.index = index;
		links = links->next;
	}
}

static bool	*init_is_visited_array(int unique_numbers)
{
	bool	*is_visited;

	is_visited = ft_calloc(unique_numbers, sizeof(bool));
	if (!is_visited)
		return (NULL);
	return (is_visited);
}

static bool	**init_is_linked_matrix(int unique_numbers)
{
	bool	**is_linked;
	int		i;

	is_linked = (bool**)ft_calloc(unique_numbers, sizeof(bool*));
	if(is_linked == NULL)
		return (NULL);
	i = 0;
	while(i < unique_numbers)
	{
		is_linked[i] = (bool*)ft_calloc(unique_numbers, sizeof(bool));
		if(is_linked[i] == NULL)
		{
			free_matrix(is_linked, i);
			return (NULL);
		}
		i++;
	}
	return (is_linked);
}

static void	fill_is_linked_matrix(bool **is_linked, t_link *links)
{
	while (links)
	{
		is_linked[links->n.index][links->m.index] = true;
		is_linked[links->m.index][links->n.index] = true;
		links = links->next;
	}
}
