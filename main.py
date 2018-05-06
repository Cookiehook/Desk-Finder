from node_objects import NodeObject
import queue as q
import logging

logging.basicConfig(level=logging.INFO)


def find_shortest_path(start, end):

    visited_nodes = []  # List of nodes we've visited, used to check if we've reached the end
    node_path = []  # List of nodes visited, and how we got there.
    priority_queue = q.PriorityQueue()

    hack_counter = 0 #  Used to make sure the priority queue never tries to sort by a NodeOject. This needs to be implemented better in the future.
    priority_queue.put((0, hack_counter, start, start))
    hack_counter += 1

    while end not in visited_nodes:
        current_entry = priority_queue.get()
        current_cost = current_entry[0]
        current_node = current_entry[2]
        previous_node = current_entry[3]

        # Loop through all nodes linked to the current one. Add them to the priority queue
        # if they haven't already been processed.
        for destination, cost in current_node.relationship_map.items():
            if destination not in visited_nodes:
                priority_queue.put((current_cost + cost, hack_counter, destination, current_node))
                logging.debug("Adding {0}, {1}, {2}, {3} to priority queue".format(
                                current_cost + cost, hack_counter, destination.name, current_node.name))
                hack_counter += 1
        visited_nodes.append(current_node)
        node_path.append((current_node, previous_node))

    for item in node_path:
        logging.debug("{0} Processed by {1}".format(item[0].name, item[1].name))

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


def get_cost_of_route(route):
    current_cost = 0

    while len(route) > 1:
        current_cost += route[0].get_cost_to_node(route[1])
        route.remove(route[0])

    return current_cost


if __name__ == "__main__":

    # Creating some nodes. Eventually moved into a database read command
    door = NodeObject("Door")
    a = NodeObject("Desk A")
    b = NodeObject("Desk B")
    c = NodeObject("Desk C")
    d = NodeObject("Desk D")
    e = NodeObject("Desk E")
    f = NodeObject("Desk F")
    g = NodeObject("Desk G")
    h = NodeObject("Desk H")
    i = NodeObject("Desk I")
    j = NodeObject("Desk J")

    # Adding node relations. Eventually moved into a database read command
    door.add_relationships((a, 4))
    a.add_relationships((door, 4), (b, 1), (g, 2))
    b.add_relationships((c, 1), (a, 1))
    c.add_relationships((b, 1))
    d.add_relationships((g, 5), (j, 1))
    e.add_relationships((g, 2), (f, 1), (h, 1))
    f.add_relationships((g, 15), (e, 1))
    g.add_relationships((a, 2), (d, 5), (e, 2), (f, 15))
    h.add_relationships((e, 1), (i, 2))
    i.add_relationships((h, 2), (j, 2))
    j.add_relationships((d, 1), (i, 3))

    path = find_shortest_path(door, i)
    cost = get_cost_of_route(path)
    for node in path:
        logging.info(node.name)

    logging.info("Total cost is: %s " % cost)
