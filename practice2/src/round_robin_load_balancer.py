import threading


class RoundRobinLoadBalancer:
    def __init__(self):
        self.servers = []
        self.stats = dict()
        self.lock = threading.Lock()

    def add_server(self, server_id):
        with self.lock:
            self.servers.append(server_id)

    def get_server_for_request(self, request_id):
        with self.lock:
            server_id = request_id % len(self.servers)
            current_requests = self.stats[server_id] if server_id in self.stats else 0
            self.stats[server_id] = current_requests + 1
            return server_id


if __name__ == '__main__':
    def simulate_request(lb, request_id):
        print(f"Request {request_id} assigned to {lb.get_server_for_request(request_id)}")

    balancer = RoundRobinLoadBalancer()
    for server in range(0, 4):
        balancer.add_server(server)

    threads = []
    for request in range(0, 40000):
        thread = threading.Thread(target=simulate_request, args=(balancer, request))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(balancer.stats)
