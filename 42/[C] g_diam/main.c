#include "g_diam.h"
#include <stdlib.h>
#include <unistd.h>

static int	find_longest_chain(
				bool **is_linked, bool *is_visited, int unique_numbers);
static void	follow_all_links(
				bool **is_linked,
				bool *is_visited,
				int i,
				int *longest_chain,
				int unique_numbers);

int	main(int argc, char *argv[])
{
	bool	**is_linked;
	bool	*is_visited;
	int		unique_numbers;
	int		longest_chain;

	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	if (!init(&is_linked, &is_visited, &unique_numbers, argv[1]))
		return (1);

	longest_chain = find_longest_chain(is_linked, is_visited, unique_numbers);
	ft_putnbr(longest_chain);
	write(1, "\n", 1);

	free_matrix(is_linked, unique_numbers);
	free(is_visited);
	return (0);
}

static int	find_longest_chain(
				bool **is_linked, bool *is_visited, int unique_numbers)
{
	int	longest_chain;
	int	tmp;
	int	i;

	longest_chain = 0;
	i = 0;
	while (i < unique_numbers)
	{
		tmp = 0;
		follow_all_links(is_linked, is_visited, i, &tmp, unique_numbers);
		if (tmp > longest_chain)
			longest_chain = tmp;
		i++;
	}
	return (longest_chain);
}

static void	follow_all_links(
				bool **is_linked,
				bool *is_visited,
				int i,
				int *longest_chain,
				int unique_numbers)
{
	int starting_point;
	int	tmp;
	int	j;

	is_visited[i] = true;
	(*longest_chain)++;
	starting_point = *longest_chain;

	j = 0;
	while (j < unique_numbers)
	{
		if (!is_visited[j] && is_linked[i][j])
		{
			tmp = starting_point;
			follow_all_links(is_linked, is_visited, j, &tmp, unique_numbers);
			if (tmp > *longest_chain)
				*longest_chain = tmp;
		}
		j++;
	}
	is_visited[i] = false;
}
