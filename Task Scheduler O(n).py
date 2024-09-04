def leastInterval(self, tasks: List[str], n: int) -> int:
    count = defaultdict(list)

    for task in Counter(tasks).items():
        count[task[1]].append(task[0])
        
    highest_freq, other_tasks = max(count), 0
    most_freq = len(count[highest_freq])
    del count[highest_freq]

    for key in count:
        other_tasks += key * len(count[key])

    return most_freq * highest_freq + max(other_tasks, (highest_freq - 1) * (n + 1 - most_freq))
