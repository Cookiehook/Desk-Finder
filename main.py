from desk_objects import DeskObject
import queue as Q

list_of_desks = []

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

list_of_desks.append(door)
list_of_desks.append(a)
list_of_desks.append(b)
list_of_desks.append(c)
list_of_desks.append(d)
list_of_desks.append(e)
list_of_desks.append(f)
list_of_desks.append(g)
list_of_desks.append(h)
list_of_desks.append(i)
list_of_desks.append(j)

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

# for desk in list_of_desks:
#     for key, value in desk.relationship_map.items():
#         print("{0} is related to {1} with cost {2}".format(desk.name, key.name, value))


def find_shortest_path(start, end):

    hack_counter = 0 # Used to make sure the priority queue never tries to sort by a DeskObject. This needs to be implemented better in the future.
    priority_queue = Q.PriorityQueue()
    priority_queue.put((0, hack_counter, start))
    hack_counter += 1
    completed_desks = []

    while end not in completed_desks:
        current_entry = priority_queue.get()
        current_cost = current_entry[0]
        current_desk = current_entry[2]
        for destination, cost in current_desk.relationship_map.items():
            if destination not in completed_desks:
                priority_queue.put((current_cost + cost, hack_counter, destination))
                hack_counter += 1
        completed_desks.append(current_desk)


"""
Once we have a processed final node:
    Get the final node, put it in a path list.
    Search the processed nodes for any nodes related to final. Pick the lowest cost, add it to the path list.
    Repeat with the last entry on the path list, until start is found.
    Reverse the list, print it
"""

find_shortest_path(door, e)
print("Complete")

