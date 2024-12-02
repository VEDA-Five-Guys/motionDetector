#include <iostream>

#include "python_module.h"

static MessageQueue* global_message_queue = nullptr;

static PyObject* send_message(PyObject* self, PyObject* args) {
	const char* message;
	if (!PyArg_ParseTuple(args, "s", &message)) return nullptr;

	std::cout << "send_message called with : " << message << '\n';

	if (global_message_queue) {
		global_message_queue->push(message);
	}

	Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
	{ "send_message", send_message, METH_VARARGS, "Send message to server via WebSocket"},
	{ nullptr, nullptr, 0, nullptr }
};

static struct PyModuleDef custom_module = {
	PyModuleDef_HEAD_INIT,
	"custom_module",
	nullptr,
	-1,
	methods
};

PyMODINIT_FUNC PyInit_custom_module(void) {
	return PyModule_Create(&custom_module);
}

PythonModule::PythonModule(MessageQueue& message_queue)
	: message_queue_(message_queue) {
	global_message_queue = &message_queue;
}

PythonModule::~PythonModule() {
	Py_Finalize();
}

void PythonModule::initialize() {
	PyImport_AppendInittab("custom_module", &PyInit_custom_module);
	Py_Initialize();
}

void PythonModule::run_script(const std::string& script_name) {
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('.')");
	std::string import_command = "import " + script_name;
	PyRun_SimpleString(import_command.c_str());
}
