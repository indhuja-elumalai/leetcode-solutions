class Solution:
    def pushDominoes(self, dominoes: str) -> str:
            prev=""
            while dominoes!=prev:
                prev=dominoes
                dominoes=dominoes.replace('R.L','xxx').replace('.L','LL').replace('R.','RR')
            return dominoes.replace('xxx','R.L')


