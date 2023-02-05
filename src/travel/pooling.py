import numpy as np
from sys import maxsize
from itertools import permutations
from location_management import Location
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
from time import perf_counter


def time_wrapper(func, *args, **kwargs):
    time_start = perf_counter()
    ret = func(*args, **kwargs)
    time_end = perf_counter()
    print(f'The time taken for the function {func.__name__} was {time_end - time_start}')
    return ret


def travellingSalesmanProblem(graph, s, V):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        point_path = [s]
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
            point_path.append(j)
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path, point_path


class CarPooling:

    def __init__(self, host_address: str, attendee_addresses: list[str], carshare_address: str = None):

        self.host_addr = [Location(host_address)]
        self.attendee_addrs = []
        for addr in attendee_addresses:
            self.attendee_addrs.append(Location(addr))
        if carshare_address:
            self.carshare_address = carshare_address
            self.carshare_address_idx = attendee_addresses.index(carshare_address) + 1

    def location_time_matrix(self):
        """
        returns a timing matrix that has each row as the time to get from address of the
        row -> address of the column
        :return:
        :rtype:
        """
        self.distance_matrix = np.zeros((len(self.attendee_addrs) + 1, len(self.attendee_addrs) + 1))
        for idx, addr1 in enumerate(self.host_addr + self.attendee_addrs):
            for jdx, addr2 in enumerate(self.host_addr + self.attendee_addrs):
                if addr1 != addr2:
                    self.distance_matrix[idx, jdx] = addr1.time_to_location(addr2.address)
        return self

    def location_distance_matrix(self):
        """
        returns a timing matrix that has each row as the time to get from address of the
        row -> address of the column
        :return:
        :rtype:
        """
        self.distance_matrix = np.zeros((len(self.attendee_addrs) + 1, len(self.attendee_addrs) + 1))

        for idx, addr1 in enumerate(self.host_addr + self.attendee_addrs):
            for jdx, addr2 in enumerate(self.host_addr + self.attendee_addrs):
                if addr1 != addr2:
                    self.distance_matrix[idx, jdx] = addr1.dist_to_location(addr2.address)
        return self

    def tsp_uber(self, timing_not_dist: bool = True) -> float:
        data = {}
        if timing_not_dist:
            self.location_time_matrix()
        else:
            self.location_distance_matrix()
        data['distance_matrix'] = self.distance_matrix
        data['num_vehicles'] = 1
        data['depot'] = 0

        data['distance_matrix'][0, :] = 0

        print(f'data=\n{data["distance_matrix"]}')

        def distance_callback(from_idx, to_idx) -> float:
            """Returns the distance/time between two nodes"""
            from_node = manager.IndexToNode(from_idx)
            to_node = manager.IndexToNode(to_idx)
            if from_node == 0:
                weighting = 0
            else:
                weighting = data['distance_matrix'][from_node][to_node]
            return weighting

        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
        routing = pywrapcp.RoutingModel(manager)

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        solution = routing.SolveWithParameters(search_parameters)
        index = routing.Start(0)
        plan_output = 'Route for vehicle 0:\n'
        route_distance = 0
        # print([f'{idx} : {loc}' for idx, loc in enumerate(self.attendee_addrs)])
        route_numbers = []
        while not routing.IsEnd(index):
            route_numbers.append(index)
            if index != 0:  # This ignores starting at the hosts location
                plan_output += f' {(self.host_addr + self.attendee_addrs)[manager.IndexToNode(index)]} ->'
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

        # Calculate route_distance
        route_distance = 0
        for idx, number in enumerate(route_numbers[1:-1]):
            route_distance += data['distance_matrix'][number, route_numbers[idx + 1]]

        route_distance = int(route_distance)
        if timing_not_dist:
            interval = 'seconds'
        else:
            interval = 'meters'
        plan_output += f' {self.host_addr[0]}\n'
        plan_output += f'Route distance: {route_distance}{interval}\n'
        print(plan_output)
        self.route_numbers = route_numbers
        return route_distance

    def tsp_carshare(self, timing_not_dist: bool = True) -> float:
        data = {}
        if timing_not_dist:
            self.location_time_matrix()
        else:
            self.location_distance_matrix()
        data['distance_matrix'] = self.distance_matrix
        data['num_vehicles'] = 1
        data['depot'] = 0

        # data['distance_matrix'][0, 1:] =
        data['distance_matrix'][0, self.carshare_address_idx] = 0

        print(f'data=\n{data["distance_matrix"]}')

        for idx, name in enumerate(self.host_addr + self.attendee_addrs):
            print(f'{idx} \t:{name}')

        def distance_callback(from_idx, to_idx) -> float:
            """Returns the distance/time between two nodes"""
            from_node = manager.IndexToNode(from_idx)
            to_node = manager.IndexToNode(to_idx)
            if from_node == 0 and to_node == self.carshare_address_idx:
                weighting = 0
            else:
                weighting = data['distance_matrix'][from_node][to_node]
            return weighting

        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
        routing = pywrapcp.RoutingModel(manager)

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        solution = routing.SolveWithParameters(search_parameters)
        index = routing.Start(0)
        plan_output = 'Route for vehicle 0:\n'
        route_distance = 0
        # print([f'{idx} : {loc}' for idx, loc in enumerate(self.attendee_addrs)])
        route_numbers = []
        while not routing.IsEnd(index):
            route_numbers.append(index)
            if index != -1:  # This ignores starting at the hosts location
                plan_output += f' {(self.host_addr + self.attendee_addrs)[manager.IndexToNode(index)]} ->'
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

        # Calculate route_distance
        route_distance = 0
        for idx, number in enumerate(route_numbers[:-1]):
            print(data['distance_matrix'][number, route_numbers[idx + 1]])
            route_distance += data['distance_matrix'][number, route_numbers[idx + 1]]

        route_distance = int(route_distance)
        if timing_not_dist:
            interval = 'seconds'
        else:
            interval = 'meters'
        plan_output += f' {self.host_addr[0]}\n'
        plan_output += f'Route distance: {route_distance}{interval}\n'
        print(plan_output)
        self.route_numbers = route_numbers

        return route_distance

    def get_max_amount(self) -> float:
        """
        Returns the maximum distance or time taken for the most inefficient routes.
        These routes are defined by each person getting their own car.
        :return:
        :rtype:
        """
        return np.sum(self.distance_matrix[1:, 0])

    def get_locations(self) -> list[dict]:
        """
        Gets a list of the latitude and longitudes of each user_id.
        Ordered in the optimized path.
        """
        addresses = self.host_addr + self.attendee_addrs
        lat_longs = []
        for idx in np.roll(self.route_numbers, -1):
            # print(f'{addresses[idx]} and {addresses[idx].location}\n')
            lat_longs.append(addresses[idx].location)
        # print(lat_longs)
        return lat_longs


def query_db_for_address(user_id) -> list[str]:
    addr1 = 'South Kensington Station, London'
    addr2 = 'Acton Town Station, London'
    addr3 = 'Earls Court Station, London'
    addr4 = 'Baron\'s Court Station, London'
    addr = 'London Heathrow'
    addr5 = 'Hammersmith Tube Station, London'
    return [addr2, addr3, 'Slough, England', addr1, addr]
    return [addr1, addr2, addr3, addr4, addr5]


def query_db_for_host_address(event_id) -> list[str]:
    host_add = ['Blackett Laboratory, Imperial College London, London']
    return host_add


def carpooling_handler(event, context):
    # event["user_ids"] -> Query db for location of user id,
    user_ids = event["user_ids"]
    carshare_id = event['carshare_id']
    event_id = event['event_id']
    event_address = query_db_for_host_address(event_id)[0]
    addresses = query_db_for_address(user_ids)
    if event['carshare_id'] != 1:
        carshare_address = query_db_for_address(carshare_id)[0]
    else:
        carshare_address = 'London Heathrow'

    pool = CarPooling(event_address, addresses, carshare_address)
    pool.location_time_matrix()
    tot_time = pool.tsp_carshare(timing_not_dist=False)  # Set True for timings, False for distance
    location_list = pool.get_locations()
    max_time = pool.get_max_amount()
    carpool_data = {
            "markers"   : location_list,
            "total_time": tot_time,
            "CO2"       : tot_time / max_time
    }
    return carpool_data


def uberpooling_handler(event, context):
    # event["user_ids"] -> Query db for location of user id,
    user_ids = event["user_ids"]
    event_id = event['event_id']
    event_address = query_db_for_host_address(event_id)[0]
    addresses = query_db_for_address(user_ids)

    pool = CarPooling(event_address, addresses)
    pool.location_time_matrix()
    tot_time = pool.tsp_uber(timing_not_dist=False)  # Set True for timings, False for distance
    location_list = pool.get_locations()
    max_time = pool.get_max_amount()

    carpool_data = {
            "markers"   : location_list,
            "total_time": tot_time,
            "CO2"       : tot_time / max_time
    }
    return carpool_data
