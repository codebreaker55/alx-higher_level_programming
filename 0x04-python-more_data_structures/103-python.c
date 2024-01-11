#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list_info - function that prints basic info of python lists
 *
 * @p: is a pyobject list
 *
 * Return: nothing
*/

void print_python_list_info(PyObject *p)
{
	int siz, aloc, n;
	const char *type;
	PyListObject *lis = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	siz = var->ob_size;
	aloc = lis->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", siz);
	printf("[*] Allocated = %d\n", aloc);

	for (n = 0; n < siz; n++)
	{
		type = lis->ob_item[n]->ob_type->tp_name;
		printf("Element %d: %s\n", n, type);

		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(lis->ob_item[n]);
		}
	}
}

/**
 * print_python_bytes - function that prints basic info of python objects
 *
 * @p: is a pyobject list
 *
 * Return: void
*/

void print_python_bytes(PyObject *p)
{
	unsigned char n, size;
	PyBytesObject *byts = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byts->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		siz = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %d bytes: ", siz);

	for (n = 0; n < siz; n++)
	{
		printf("%02hhx", byts->ob_sval[n]);
		if (n == siz - 1)
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
