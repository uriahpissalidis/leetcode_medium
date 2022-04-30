# 399. Evaluation Division
"""
Problem can be modeled with a graph

For example: we are given,
a/b = 2.0, b/c = 3.0
the above can be built with a directed graph
a -- 2.0 --> b -- 3.0 --> c

If we were asked to find a/c, we have:
a/c = a/b * b/c = 2.0 * 3.0
In the graph, it is the product of the costs of the edges!

Do notice that, 2 edges need to be added into the graph with one given equation,
because with a/b we also get the result of b/a, which is the reciprocal of a/b.

so the previous example also gives edges:
c -- 0.333 --> b -- 0.5 --> a

Now we know how to model the problem
So we build a graph with given equations and traverse the graph,
either utilize DFS or BFS, to find a path for the given query,
so the result is the product of costs of edges on the path.
"""

class solution(object):
	def calcEquation(self, equations, values, queries):
		graph = {}

		def build_graph(equations, values):
			def add_edge(f, t, value):
				if f in graph:
					graph[f].append((t, value))
				else:
					graph[f] = [(t, value)]

		for vertices, value in zip(equations, values):
			f, t = vertices
			add_edge(f, t, value)
			add_edge(t, f, 1/value)

		def find_path(query):
			b, e = query

			if b not in graph or e not in graph:
				return -1.0

			while q:
				from, curr_product = q.popleft()
				if front == e:
					return curr_product
				visited.add(front)
				for neighbor, value in graph[front]:
					if neighbor not in visited:
						q.append((neighbor, curr_product*value))

			return -1.0

		build_graph(equations, values)
		return [find_path(q) for q in queries]