#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_bytes - function that prints basic info of python objects
 *
 * @p: is a pyobject list
 *
 * Return: void
*/

void print_python_bytes(PyObject *p)
{
	size_t n, siz, len;
	char *strin;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	siz = ((PyVarObject *)p)->ob_size;
	len = siz + 1 < 10 ? siz + 1 : 10;
	strin = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %lu\n", siz);
	printf("  trying string: %s\n", strin);
	printf("  first %lu bytes: ", len);

	for (n = 0; n < len; n++)
	{
		printf("%02hhx%s", strin[n], n + 1 > len ? "" : " ");
	}
	printf("\n");
}

/**
 * print_python_float - function tht priints python float info
 *
 * @p: is a PyFloat Object
 *
 * Return: void
*/

void print_python_float(PyObject *p)
{
	double f;

	setbuf(stdout, NULL);

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %s\n", PyOS_double_to_string
			(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_list - function that prints basic info of python lists
 *
 * @p: is a pyobject list
 *
 * Return: nothing
*/

void print_python_list(PyObject *p)
{
	int n;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (n = 0; n < ((PyVarObject *)p)->ob_size; n++)
	{
		printf("Element %d: %s\n", n,
				((PyListObject *)p)->ob_item[n]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[n]->ob_type->tp_name, "bytes"))
		{
			print_python_bytes(((PyListObject *)p)->ob_item[n]);
		}
		else if (!strcmp(((PyListObject *)p)->ob_item[n]->ob_type->tp_name, "float"))
		{
			print_python_float(((PyListObject *)p)->ob_item[n]);
		}
	}
}
