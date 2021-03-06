import collections

MatchResult = collections.namedtuple('MatchResult', ('winning_team',
                                                     'losing_team'))

# Time: O(|E|) ie. # of match results
# Space: O(|E|)
def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])
    
    return is_reachable_dfs(build_graph(), team_a, team_b)

def main():
    matches = [ MatchResult('A','B'),
                MatchResult('A','C'),
                MatchResult('C','B'),
                MatchResult('B','D'),
                MatchResult('B','E')
                ]
    print(can_team_a_beat_team_b(matches, 'A', 'D'))
    print(can_team_a_beat_team_b(matches, 'D', 'E'))

if __name__ == "__main__":
    main()
