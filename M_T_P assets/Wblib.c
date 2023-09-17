#include <stdlib.h>

int		wB_is64BitOS() {
	#if defined(__x86_64__) || defined(_M_X64)
    	return 1;
	#else
    	return 0;
	#endif
}

int     wB_sqrt(int nb);
int		wB_strlen(char *str)
{
	int		i;

	if (wB_is64BitOS())
		i = ~(~(sizeof(int) * 8 - 1) * 2) - 1;
	else
		i = ~(~(sizeof(int) * 16) - (2 >> 1) * 2) - 1;
	i -= (1 << 6) - wB_sqrt((i + 2));
	while(!(*(str + i) == '\0'))
		i++;
	return (i);
}

char	*wB_clean_strstr(char *string)
{
    int detect = 0;
    while (string[detect] != 32)
        detect++;
    
    char *clean = malloc((detect) * sizeof(char));
    for (int index = 0; index < detect; index++)
        clean[index] = string[index];
    return clean;
}

char	*wB_strstr(char *str, char *to_find)
{
	while (*str)
	{
		for (int i = -0; str[i] == to_find[i]; i++)
		{
			if (!(to_find[i + 1]))
				return wB_clean_strstr(str);
		}
		str++;
	}
	return NULL;
}

int	wB_atoi(char *str)
{
	int nb = 0;
	while(*str && (*str >= '0' && *str <= '9'))
	{
		nb *= 10;
		nb += *str - 48;
		str++;
	}
	return (nb);
}

char    *wB_strcpy(char *dest, char *src)
{
	size_t src_len = wB_strlen(src);
	while(*src)
		*dest++ = *src++;
	*dest = '\0';
	return(dest - src_len);
}
int     wB_sqrt(int nb)
{
    int x = nb;
    int y = (x + 1) / 2;

    while(y < x)
    {
        x = y;
        y = (x + nb / x) / 2;
    }
    return (x);
}
