import queue as q


def find_shortest_path(start, end, nodes_lookup):
    """
    Using Djikstra's algorithm, finds the shortest path from one node to another.
    When searching for linked nodes, it will first look through that node's children, then any nodes that
    are a parent of the current node.
    :param start: Node to start from
    :param end: Node to find a path to
    :param nodes_lookup: List of all nodes and their IDs. Needed to relate node_it with NodeObject instances.
    :return: List of nodes comprising the shortest path
    """
    visited_nodes = []
    node_path = []
    priority_queue = q.PriorityQueue()

    counter = 0  # Used to make sure the priority queue never tries to sort by a NodeOject.
    priority_queue.put((0, counter, start, start))
    counter += 1

    while end not in visited_nodes:
        current_entry = priority_queue.get()
        current_cost = current_entry[0]
        current_node = current_entry[2]
        previous_node = current_entry[3]

        # Loop through all child relationships first
        for relationship in current_node.child_relationship:
            # Find the node object related to the PK in the node_path table.
            for node in nodes_lookup:
                if getattr(node, "node_id") == getattr(relationship, "parent_node_id"):
                    related_node = node
                    break
            if related_node not in visited_nodes:
                priority_queue.put((current_cost + getattr(relationship, "cost"), counter, related_node, current_node))
                counter += 1

        # Loop through all parent relationships next.
        for relationship in current_node.parent_relationship:
            # Find the node object related to the PK in the node_path table.
            for node in nodes_lookup:
                if getattr(node, "node_id") == getattr(relationship, "child_node_id"):
                    related_node = node
                    break
            if related_node not in visited_nodes:
                priority_queue.put((current_cost + getattr(relationship, "cost"), counter, related_node, current_node))
                counter += 1

        visited_nodes.append(current_node)
        node_path.append((current_node, previous_node))

    node_path.reverse()
    shortest_route = []
    shortest_route.append(end)

    # Back track through history to find the shortest path
    current_node = end
    while current_node is not start:
        for entry in node_path:
            if entry[0] == current_node:
                shortest_route.append(entry[1])
                current_node = entry[1]
                break  # Prevents start from being added twice
    shortest_route.reverse()
    return shortest_route


def get_cost_of_route(route, relationship_lookup):
    """
    Given a list of nodes, calculates the total cost of the path
    :param route: List of nodes to calculate the cost between
    :param relationship_lookup: List of all relationships
    :return: Integer value for the total cost of that journey
    """
    current_cost = 0

    while len(route) > 1:

        current_node = route[0]
        for relation in relationship_lookup:
            parent_node_id = getattr(relation, "parent_node_id")
            child_node_id = getattr(relation, "child_node_id")
            if (parent_node_id == current_node.node_id and child_node_id == route[1].node_id) or \
                (child_node_id == current_node.node_id and parent_node_id == route[1].node_id):
                new_cost = getattr(relation, "cost")
                break
        current_cost += new_cost
        route.remove(route[0])

    return current_cost
