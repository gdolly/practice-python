from load_balancer import LoadBalancer


def main():
    balancer = LoadBalancer(44, 5000)
    for request_id in range(0, 1000):
        print(f'Request={request_id} => Server={balancer.get_server(request_id)}')
    print(balancer.get_server_stats())


if __name__ == "__main__":
    main()
