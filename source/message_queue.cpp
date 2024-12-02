#include "message_queue.h"

void MessageQueue::push(const std::string& message) {
	std::lock_guard<std::mutex> lock(mutex_);
	queue_.push(message);
}

bool MessageQueue::pop(std::string& message) {
	std::lock_guard<std::mutex> lock(mutex_);
	if (queue_.empty()) return false;

	message = queue_.front();
	queue_.pop();
	return true;
}
