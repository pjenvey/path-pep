/*
    Return the file system path of the object.

    If the object is str or bytes, then allow it to pass through with
    an incremented refcount. If the object defines __fspath__(), then
    return the result of that method. All other types raise a TypeError.
*/
PyObject *
PyOS_FSPath(PyObject *path)
{
    if (PyUnicode_Check(path) || PyBytes_Check(path)) {
        Py_INCREF(path);
        return path;
    }

    if (PyObject_HasAttrString(path->ob_type, "__fspath__")) {
        return PyObject_CallMethodObjArgs(path->ob_type, "__fspath__", path,
                                          NULL);
    }

    return PyErr_Format(PyExc_TypeError,
                        "expected a str, bytes, or path object, not %S",
                        path->ob_type);
}
