from collections import deque


def person_is_seller(pers):
    return len(pers) == 6


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, searched)
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False


graph = {'you': ['alice', 'bob', 'claire']}
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

print(search('you'))

# Time to complete = O(amount_people + amount_edge)