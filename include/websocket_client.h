#ifndef WEBSOCKET_CLIENT_H
#define WEBSOCKET_CLIENT_H

#include <string>
#include <boost/beast/core.hpp>
#include <boost/beast/websocket.hpp>
#include <boost/asio.hpp>

#include "message_queue.h"

namespace beast = boost::beast;
namespace websocket = beast::websocket;
namespace net = boost::asio;
using tcp = net::ip::tcp;

class WebSocketClient {
	std::string host_;
	std::string port_;
	MessageQueue& message_queue_;

public:
	WebSocketClient(const std::string& host, const std::string& port, MessageQueue& message_queue);
	void run();
};

#endif // WEBSOCKET_CLIENT_H
