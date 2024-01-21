#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	size_t y, x = 0;
	PyObject *obj;

	y = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", y);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	while (x < y)
	{
		obj = PyList_GET_ITEM(p, x);
		printf("Element %zu: %s\n", x, Py_TYPE(obj)->tp_name);
		x++;
	}
}

