#ifndef PYTHON_MODULE_H
#define PYTHON_MODULE_H

#include <Python.h>
#include <string>

#include "message_queue.h"

class PythonModule{
	MessageQueue& message_queue_;
public:
	PythonModule(MessageQueue&);
	~PythonModule();
	void initialize();
	void run_script(const std::string&);
};

#endif // PYTHON_MODULE_H
