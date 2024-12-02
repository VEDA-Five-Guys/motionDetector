#ifndef MESSAGE_QUEUE_H
#define MESSAGE_QUEUE_H

#include <queue>
#include <mutex>
#include <string>

class MessageQueue {
	std::queue<std::string> queue_;
	std::mutex mutex_;

public:
	void push(const std::string& message);
	bool pop(std::string& message);
};

#endif // MESSAGE_QUEUE_H
