"""
class Solution:
    def suggestedProducts(self, products: List[str], s: str) -> List[List[str]]:
        # edge case :kreygasm: (HOW TF DO I DO THIS)
        # if len(products) == 1 and s == products[0]: return products
        products.sort()
        row, temp, prods = 0, '', [[]]
        # get one char at a time from the search word, return the PREFIX in each row of the 2d list
        for char in s:
            c = 0
            temp += char
            while c != 3:
                for j in range(len(products)-1):
                    if products[j].startswith(temp, 0, len(temp)):
                        prods[row].append(products[j])
                c += 1
            row += 1
        return prods
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answ=[]
        products.sort()
        for i in range(len(searchWord)):
            newProduct=[]
            for p in products:
                if i<len(p) and p[i]==searchWord[i]:
                    newProduct.append(p)
            answ.append(newProduct[:3])
            products=newProduct
        return answ
