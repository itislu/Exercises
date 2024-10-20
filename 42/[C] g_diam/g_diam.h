#ifndef G_DIAM_H
# define G_DIAM_H

# include <stdbool.h>
# include <stddef.h>

/**
 * @brief Data structure for saving the input.
 *
 * @param nbr       Original input number.
 * @param index     Used to index the is_linked_matrix. Default is -1
 */
typedef struct s_node
{
	int	nbr;
	int	index;
}	t_node;

typedef struct s_link t_link;
struct s_link
{
	t_node	n;
	t_node	m;
	t_link	*next;
};

// Init
bool	init(
			bool ***is_linked,
			bool **is_visited,
			int *unique_numbers,
			char *input);

// Utils
bool	append_link(t_link **head, int n, int m);
void	free_links(t_link **head);
void	free_matrix(bool **matrix, int size);
int		ft_atoi(char *str);
void	*ft_calloc(size_t nmemb, size_t size);
bool	ft_isdigit(char c);
void	ft_putnbr(int n);
void	goto_next_nbr(char *str, int *i);

#endif
