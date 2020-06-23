#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <ctype.h>
#include <unistd.h>
#include <ctype.h>
#include <stdlib.h>

#define FILENAME_LENGTH 30
#define LINE_LENGHT  30

typedef	struct	s_table
{
	char	symbol[30];
	char	value[15];
}		t_table;


t_table	 address_symb[30];


/*____FT_ATOI____*/

int             ft_sizeof(char *str)
{
        int i;
        int j;

        i = 0;
        while (str[i] != 0)
        {
                j = i;
                while (str[++j] != 0)
                        if (str[i] == str[j])
                                return (0);
                if (str[i] == '+' || str[i] == '-')
                        return (0);
                i++;
        }
        if (i == 1)
                return (0);
        return (i);
}

void    ft_putnbr_base(int nb, char *base);

int             excepcion(int nb, int b, char *base)
{
        if (nb != -2147483648)
                return (0);
        ft_putnbr_base(nb / b, base);
        write(1, &base[-1 * (nb % b)], 1);
        return (1);
}

void    ft_putnbr_base(int nb, char *base)
{
        int div;
        int b;

        b = ft_sizeof(base);
        if (b)
        {
                if (!excepcion(nb, b, base))
                {
                        if (nb < 0)
                        {
                                nb *= -1;
                                write(1, "-", 1);
                        }
                        div = 1;
                        while ((nb / div) / b)
                                div *= b;
                        while (div)
                        {
                                write(1, &base[nb / div], 1);
                                nb %= div;
                                div /= b;
                        }
                }
        }
}
/*____UTILS____*/

void 	fill_zero(char str[LINE_LENGHT], int len)
{
	int i = 0;

	while(i < len)
		str[i++] = 0;
}
/*____PARSER____*/

int	get_line(int id, char str[30])
{
	char c;
	int i;
	int err;
	fill_zero(str, LINE_LENGHT);
	/*	
		i = 0;
		err = read(id, &c, 1);
		while(c != 10)
		{
		printf("%i", c);
		while(isspace(c) && c != 10)
		err = read(id, &c, 1);
		if (c = '/')
		str[i++] = 0;
		if (err == 0)
		return (0);
		str[i++] = c;
		if (c != 10)
		err = read(id, &c, 1);
		}	
		str[i] = 0;
		return (1);*/
	i = 0;
	str[i] = 0;
	err = read(id, &c, 1);
	while (c != 13 && c != 10)
	{
		while (isspace(c))
			err = read(id, &c, 1);
		if (err == 0)
			break;
		if (c == '/')
			str[i++] = 0;
		str[i++] = c;
		err = read(id, &c, 1);
	}
	return (err);
}

char	type_detect(char line[LINE_LENGHT])
{
	if(line[0] == '@')
		return ('a');
	else if(line[0] == '(')
		return ('l');
	else if(line[0] == 0)
		return ('s');
	else
		return ('c');
}

void	aparser(char line[LINE_LENGHT])
{
	int	number;
	int	i;
	int	num2;

	num2 = 1;
	i = 0;
	if (isdigit(line[1]))
	{
		number = atoi(line + 1);
		while(num2 < number)
		{
			i += 1; 
			num2 *= 2;
		}
		while(15 - i++)
			//printf("0");
			write(1, "0",1);
		ft_putnbr_base(number, "01");
	}
	else 
	{	while (strcmp(address_symb[i++].symbol, line + 1))
			;
		i--;
		write(1, address_symb[i].value, 15);
	}
}

void	parser(char line[LINE_LENGHT])
{
	char	type;

	type = type_detect(line); //a, c, l
	if (type == 'a')
		aparser(line);	
//	else if (type == 'c')
//		cparser(line);
//	printf("    %c", type);
}

/*___MAIN_____*/

int	main(int argn, char **argv)
{
	char	filenameasm[FILENAME_LENGTH];
	char	filenamebin[FILENAME_LENGTH];
	int	asm_id;
	int	bin_id;

	strcpy(address_symb[0].symbol, "R0");
	strcpy(address_symb[0].value, "00000000000000");
	strcpy(address_symb[1].symbol, "R1");
	strcpy(address_symb[1].value, "00000000000001");
	strcpy(address_symb[2].symbol, "R2");
	strcpy(address_symb[2].value, "00000000000010");
	strcpy(address_symb[3].symbol, "R3");
	strcpy(address_symb[3].value, "00000000000011");
	strcpy(address_symb[4].symbol, "R4");
	strcpy(address_symb[4].value, "00000000000100");

	strcpy(filenameasm, argv[1]);
	strcpy(filenamebin, argv[1]);
	//printf("%s\n", filename);
	asm_id = open(strcat(filenameasm, ".asm"), O_RDONLY);
	//printf("%i\n", asm_id);
	bin_id = open(strcat(filenamebin, ".hack"), O_CREAT);
	char line[30];
	while(get_line(asm_id, line))
	{
		//get_line(asm_id, line);
		parser(line);
		printf("%s\n", line);
	}
	//	return(0);
}
