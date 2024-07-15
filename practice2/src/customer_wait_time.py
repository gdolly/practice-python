class CustomerWaitTime:
    def __init__(self, wait_times):
        self.wait_times = wait_times

    def calculate_avg_wait_time(self):
        time_till_last_order = 0
        wait_time = 0
        customer_count = 0
        for customer in self.wait_times:
            in_time = customer[0]
            order_prep_time = customer[1]
            idle_time = time_till_last_order - in_time if time_till_last_order >= in_time else 0
            wait_time = wait_time + order_prep_time + idle_time
            customer_count += 1
            time_till_last_order = in_time + idle_time + order_prep_time
            print(wait_time)
        return wait_time/customer_count



if __name__ == '__main__':
    print(CustomerWaitTime([[1,2], [2, 5], [4, 3]]).calculate_avg_wait_time())
    print(CustomerWaitTime([[5,2], [5,4], [10,3], [20,1 ]]).calculate_avg_wait_time())