#!/usr/bin/python3
"""
handles the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    checks if all boxes can be opened
    """
    if boxes:
        visited = [False] * (len(boxes))
        visited[0] = True
        queue = [0]

        while queue:
            node = queue.pop(0)

            for n in boxes[node]:
                if n not in visited:
                    if 0 <= n < (len(boxes)):
                        visited[n] = True
                        queue.append(n)
        return all(visited)

    return False
