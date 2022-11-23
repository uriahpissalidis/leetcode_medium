class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        d = {}
        for _,_,food in orders:
            foods.add(food)
        foods = list(sorted(foods))
        table = defaultdict(lambda:[0]*len(foods))
        for i, food in enumerate(foods):
            d[food] = i
        for _, tnum, food in orders:
            table[tnum][d[food]] += 1
        head = ["Table"]
        head.extend(foods)
        res = [head]
        for i in sorted(table.keys(), key = lambda x: int(x)):
            table[i].insert(0, i)
            res.append(map(str,table[i]))
        return res
