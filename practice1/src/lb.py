import hashlib
from collections import defaultdict


class ConsistentHashing:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas
        self.ring = dict()
        self.sorted_keys = []
        self.load_distribution = defaultdict(int)  # To track load distribution

    def _hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_server(self, server):
        for i in range(self.num_replicas):
            key = self._hash(f'{server}:{i}')
            self.ring[key] = server
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def remove_server(self, server):
        for i in range(self.num_replicas):
            key = self._hash(f'{server}:{i}')
            del self.ring[key]
            self.sorted_keys.remove(key)

    def get_server(self, key):
        if not self.ring:
            return None

        hashed_key = self._hash(key)

        # Linear search to find the correct position
        for i in range(len(self.sorted_keys)):
            if hashed_key <= self.sorted_keys[i]:
                server = self.ring[self.sorted_keys[i]]
                self.load_distribution[server] += 1
                return server

        # If no key is greater, wrap around to the first key
        server = self.ring[self.sorted_keys[0]]
        self.load_distribution[server] += 1
        return server

    def print_load_distribution(self):
        print("Load Distribution:")
        for server, load in self.load_distribution.items():
            print(f"{server} served {load} requests")


# Example usage
lb = ConsistentHashing()

# Adding servers
for server_id in range(100):
    lb.add_server('server'+str(server_id))

# Getting server for a specific key
for request_id in range(10000):
    print(f'my_request_{request_id} => {lb.get_server("my_request_"+str(request_id))}')

# Print load distribution before removal
lb.print_load_distribution()

# Removing a server
lb.remove_server('server2')

# Getting server for a specific key after removal
print("my_request_1 => ", lb.get_server('my_request_1'))

# Print load distribution after removal
lb.print_load_distribution()
