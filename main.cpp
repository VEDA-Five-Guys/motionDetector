#include <iostream>
#include <thread>
#include <string>
#include <regex>
#include <stdexcept>

#include "message_queue.h"
#include "websocket_client.h"
#include "python_module.h"

bool is_valid_ip(const std::string& ip) {
    const std::regex ip_pattern(
        R"((\d{1,3}\.){3}\d{1,3})");
    return std::regex_match(ip, ip_pattern);
}

bool is_valid_port(const std::string& port) {
    const std::regex port_pattern(R"(\d{1,5})");
    int port_num = std::stoi(port);
    return std::regex_match(port, port_pattern) && port_num >= 1 && port_num <= 65535;
}

int main() {
    MessageQueue message_queue;

    PythonModule python_module(message_queue);
    python_module.initialize();

    std::string host;
    std::string port;

    try {
	std::cout << "Enter server IP address: ";
        std::cin >> host;

        if (!is_valid_ip(host)) {
            throw std::invalid_argument("Invalid IP address format.");
        }

        std::cout << "Enter server port: ";
        std::cin >> port;

        if (!is_valid_port(port)) {
            throw std::invalid_argument("Invalid port number. Must be between 1 and 65535.");
        }

        WebSocketClient websocket_client(host, port, message_queue);

        std::thread websocket_thread(&WebSocketClient::run, &websocket_client);

        python_module.run_script("motion_detection");

        websocket_thread.join();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
