#include <Python.h>
#include <listobject.h>
#include <object.h>

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
	PyObject *ob;

	siz = Py_SIZE(p);
	aloc = ((PyListobject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", siz);
	printf("[*] Allocated = %d\n", aloc);

	for (n = 0; n < siz; n++)
	{
		printf("Element %d: ", n);

		ob = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
