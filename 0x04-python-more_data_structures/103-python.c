#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Displays information about byte objects
 *
 * @p: Python object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] Byte object information\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Byte Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  Size: %ld\n", size);
	printf("  Trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  First %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Displays information about list objects
 *
 * @p: Python object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)p)->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list information\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
