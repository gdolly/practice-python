import threading


class ConsistentHashLoadBalancer():
    def __init__(self):
        self.server_space = 20
        self.servers = dict()
        self.sorted_server_keys = []
        self.stats = dict()
        self.lock = threading.Lock()

    def hash(self, value):
        return value * value

    def add_server(self, server_id):
        with self.lock:
            server_key = self.hash(server_id)
            self.servers[server_key] = server_id
            self.sorted_server_keys.append(server_key)
        self.sorted_server_keys.sort()

    def get_server_for_request(self, request_id):
        request_key = self.hash(request_id) % self.server_space
        with self.lock:
            for server_key in self.sorted_server_keys:
                if request_key <= server_key:
                    server_id = self.servers[server_key]
                    current_requests = self.stats[server_id] if server_id in self.stats else 0
                    self.stats[server_id] = current_requests + 1
                    return server_id
            server_id = self.servers[0]
            current_requests = self.stats[server_id] if server_id in self.stats else 0
            self.stats[server_id] = current_requests + 1
            return server_id


if __name__ == '__main__':
    def simulate_request(lb, request_id):
        print(f"Request {request_id} assigned to {lb.get_server_for_request(request_id)}")


    balancer = ConsistentHashLoadBalancer()
    for server in range(0, 4):
        balancer.add_server(server)

    print(balancer.servers)
    print(balancer.sorted_server_keys)
    threads = []
    for request in range(0, 1000):
        thread = threading.Thread(target=simulate_request, args=(balancer, request))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(balancer.stats)
