def rearrange_by_sign(self, A, n):
        pos = []  
        neg = []  

        for i in range(n):
            if A[i] > 0:
                pos.append(A[i])
            else:
                neg.append(A[i])
        for i in range(n // 2):
            A[2 * i] = pos[i]      
            A[2 * i + 1] = neg[i]  

        return A



    

