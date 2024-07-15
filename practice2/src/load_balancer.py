class LoadBalancer:
    SEARCH_SPACE_SIZE = 20

    def __init__(self, number_of_servers, s):
        self.SEARCH_SPACE_SIZE = s
        self.number_of_servers = number_of_servers
        self.stats = {}
        self.server_space = {}
        for server_id in range(1, number_of_servers + 1):
            self.server_space[server_id] = (self.get_server_location(server_id), None)

        for server_id in list(self.server_space.keys()):
            start = 0 if server_id == 1 else self.server_space[server_id][0]

            if server_id == self.number_of_servers:
                end = self.SEARCH_SPACE_SIZE+1
            else:
                end = self.server_space[server_id + 1][0]
            self.server_space[server_id] = (self.server_space[server_id][0], range(start, end))

        print(self.server_space)

    def get_server(self, request_id) -> int:
        request_location = self.get_hash_for(request_id) % self.SEARCH_SPACE_SIZE
        server_id = self.get_assigned_server_for(request_location)

        requests_served_by_server = self.stats[server_id] if server_id in self.stats else 0
        self.stats[server_id] = requests_served_by_server + 1
        return server_id

    def get_server_location(self, server_id) -> int:
        return self.get_hash_for(server_id) % self.SEARCH_SPACE_SIZE

    def get_hash_for(self, value):
        return value * value

    def get_server_stats(self):
        return self.stats

    def get_assigned_server_for(self, request_location):
        for server in self.server_space:
            if request_location in self.server_space[server][1]:
                return server
