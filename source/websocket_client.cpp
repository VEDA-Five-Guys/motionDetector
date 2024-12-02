#include <iostream>
#include <thread>
#include <chrono>

#include "websocket_client.h"

WebSocketClient::WebSocketClient(const std::string& host, const std::string& port, MessageQueue& message_queue) 
	: host_(host), port_(port), message_queue_(message_queue) {}

void WebSocketClient::run() {
	try {
		net::io_context ioc;
		tcp::resolver resolver(ioc);
		websocket::stream<tcp::socket> ws(ioc);

		auto const results = resolver.resolve(host_, port_);
		net::connect(ws.next_layer(), results.begin(), results.end());
		ws.handshake(host_, "/");

		std::cout << "Connected to WebSocket server!\n";

		while (true) {
			std::string message;
			if (message_queue_.pop(message)) {
				try {
					ws.write(net::buffer(message));
					std::cout << "Sent message : " << message << '\n';
				} catch (const std::exception& e) {
					std::cerr << "WebSocket send error : " << e.what() << '\n';
				}
			}
			std::this_thread::sleep_for(std::chrono::milliseconds(10));
		}

		ws.close(websocket::close_code::normal);
	} catch (const std::exception& e) {
		std::cerr << "WebSocket client error : " << e.what() << '\n';
	}
}
