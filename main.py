from desk_objects import DeskObject
import queue as Q
import logging

logging.basicConfig(level=logging.INFO)

# Creating some nodes. Eventually moved into a database read command
door = DeskObject("Door")
a = DeskObject("Desk A")
b = DeskObject("Desk B")
c = DeskObject("Desk C")
d = DeskObject("Desk D")
e = DeskObject("Desk E")
f = DeskObject("Desk F")
g = DeskObject("Desk G")
h = DeskObject("Desk H")
i = DeskObject("Desk I")
j = DeskObject("Desk J")

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


def find_shortest_path(start, end):

    visited_desks = []  # List of desks we've visited, used to check if we've reached the end
    desk_path = []  # List of desks visited, and how we got there.
    priority_queue = Q.PriorityQueue()

    hack_counter = 0 #  Used to make sure the priority queue never tries to sort by a DeskObject. This needs to be implemented better in the future.
    priority_queue.put((0, hack_counter, start, start))
    hack_counter += 1

    while end not in visited_desks:
        current_entry = priority_queue.get()
        current_cost = current_entry[0]
        current_desk = current_entry[2]
        previous_desk = current_entry[3]

        # Loop through all nodes linked to the current one. Add them to the priority queue
        # if they haven't already been processed.
        for destination, cost in current_desk.relationship_map.items():
            if destination not in visited_desks:
                priority_queue.put((current_cost + cost, hack_counter, destination, current_desk))
                logging.debug("Adding {0}, {1}, {2}, {3} to priority queue".format(
                                current_cost + cost, hack_counter, destination.name, current_desk.name))
                hack_counter += 1
        visited_desks.append(current_desk)
        desk_path.append((current_desk, previous_desk))

    for item in desk_path:
        logging.debug("{0} Processed by {1}".format(item[0].name, item[1].name))

    desk_path.reverse()
    shortest_route = []
    shortest_route.append(end)

    current_desk = end
    while current_desk is not start:
        for entry in desk_path:
            if entry[0] == current_desk:
                shortest_route.append(entry[1])
                current_desk = entry[1]
                break # Prevents start from being added twice

    shortest_route.reverse()
    return shortest_route


for node in find_shortest_path(f, d):
    logging.info(node.name)

