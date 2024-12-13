#include <thread>

#include "message_queue.h"
#include "websocket_client.h"
#include "python_module.h"

int main() {
	MessageQueue message_queue;

	PythonModule python_module(message_queue);
	python_module.initialize();

	std::string host = "192.168.0.24";
	std::string port = "8080";
	WebSocketClient websocket_client(host, port, message_queue);

	std::thread websocket_thread(&WebSocketClient::run, &websocket_client);
	
	python_module.run_script("motion_detection");
	
	websocket_thread.join();

	return 0;
}
