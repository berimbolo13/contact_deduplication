import typing

from contact_model import Contact


def get_contact_groups(contacts: typing.List[Contact]):
    reverse_index = _create_reverse_index(contacts)
    graph = _create_graph_from_reverse_index(reverse_index)
    return _get_groups(graph)


def _get_groups(graph):
    visited = set()
    groups = []
    for contact in graph:
        if contact not in visited:
            group = _bfs(graph, contact)
            groups.append(group)
            visited.update(group)
    return groups


def _bfs(graph, start_contact):
    visited = set()
    queue = [start_contact]
    visited.add(start_contact)
    group = []

    while queue:
        contact = queue.pop(0)
        group.append(contact)
        for neighbor in graph[contact]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return group


def _create_reverse_index(contacts: typing.List[Contact]):
    reverse_index: dict = dict()
    for contact in contacts:
        for email in contact.emails:
            if email in reverse_index:
                reverse_index[email].append(contact)
            else:
                reverse_index[email] = [contact]
    return reverse_index


def _create_graph_from_reverse_index(reverse_index: dict):
    graph = dict()
    for contact_group in reverse_index.values():
        for element in contact_group:
            if element not in graph:
                graph[element] = []

            for neighbor in contact_group:
                if neighbor != element:
                    graph[element].append(neighbor)
    return graph
