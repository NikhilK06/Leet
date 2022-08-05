class Solution:
    def findComplement(self, num: int) -> int:
        nik = []
        nik_trans = []
        a = bin(num)
        b =''
        for i in range(len(a)): nik.append(a[i]) 
        for i in range(len(nik)):
            if not(i == 0 or i == 1):
                if nik[i] == '1': nik_trans.append('0')
                else: nik_trans.append('1') 
        for i in range(len(nik_trans)):
            b = b + nik_trans[i]
        return int(b, 2)