#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints basic info of python lists
 *
 * @p: is a pyobject list
 *
 * Return: nothing
*/

void print_python_list_info(PyObject *p)
{
        const int siz = Py_SIZE(p);
        const int aloc = ((PyListobject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", siz, aloc);

        for (int n = 0; n < siz; n++)
        {
                printf("Element %d: ", n);

                PyObject *const ob = PyList_GetItem(p, n);
                printf("%s\n", Py_TYPE(ob)->tp_name);
        }
}
