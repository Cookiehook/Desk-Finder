import queue as q
import logging


def find_shortest_path(start, end, nodes_lookup):
    visited_nodes = []  # List of nodes we've visited, used to check if we've reached the end
    node_path = []  # List of nodes visited, and how we got there.
    priority_queue = q.PriorityQueue()

    hack_counter = 0  # Used to make sure the priority queue never tries to sort by a NodeOject.
    priority_queue.put((0, hack_counter, start, start))
    hack_counter += 1

    while end not in visited_nodes:
        current_entry = priority_queue.get()
        current_cost = current_entry[0]
        current_node = current_entry[2]
        previous_node = current_entry[3]

        # Loop through all nodes linked to the current one. Add them to the priority queue
        # if they haven't already been processed.
        for relationship in current_node.child_relationship:
            # Find the node object related to the PK in the node_path table.
            for node in nodes_lookup:
                if getattr(node, "node_id") == getattr(relationship, "parent_node"):
                    child_node = node
                    break
            if child_node not in visited_nodes:
                priority_queue.put((current_cost + getattr(relationship, "cost"),
                                    hack_counter, child_node, current_node))
                hack_counter += 1
        visited_nodes.append(current_node)
        node_path.append((current_node, previous_node))

    for item in node_path:
        logging.debug("{0} Processed by {1}".format(item[0].description, item[1].description))

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
    current_cost = 0

    while len(route) > 1:

        current_node = route[0]
        for relation in relationship_lookup:
            if getattr(relation, "parent_node") == current_node.node_id and \
                    getattr(relation, "child_node") == route[1].node_id:
                new_cost = getattr(relation, "cost")
                break
        current_cost += new_cost
        route.remove(route[0])

    return current_cost
