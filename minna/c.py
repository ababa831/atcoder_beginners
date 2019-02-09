# Not submitted (may be TLE)
class BiscketYen(object):
    def __init__(self, k, a, b):
        self.biscket = 1
        self.yen = 0
        self.n_trial = 1
        self.k = k
        self.a = a
        self.b = b
        self.conv_ratio = float(b / a)
    
    def p1_biscket(self, biscket, n_trial):
        biscket += 1
        n_trial += 1
        return biscket, n_trial
    
    def to_yen(self, yen, biscket, n_trial):
        yen += 1
        biscket -= self.a
        n_trial += 1
        return yen, biscket, n_trial
    
    def is_2yen_able(self, biscket):
        if biscket >= self.a:
            return True
        else:
            return False
    
    def to_biscket(self, yen, biscket, n_trial):
        yen -= 1
        biscket += self.b
        n_trial += 1
        return yen, biscket, n_trial

    def is_2biscket_able(self, yen):
        if yen >= 1:
            return True
        else:
            return False
     
    def update(self, yen, biscket, n_trial):
        self.biscket = biscket
        self.yen = yen
        self.n_trial = n_trial
    
    def maximize_biscket(self, yen, biscket, n_trial):
        diff_biscket = int(self.conv_ratio * biscket) - biscket
        remaining = self.k - n_trial
        if diff_biscket > 1 and self.is_2yen_able(biscket) and remaining >= 2:
            yen, biscket, n_trial = self.to_yen(yen, biscket, n_trial)
            yen, biscket, n_trial = self.to_biscket(yen, biscket, n_trial)
        else:
            biscket, n_trial = self.p1_biscket(biscket, n_trial)
        self.update(yen, biscket, n_trial)


k, a, b = map(int, input().split())
by = BiscketYen(k, a, b)
while by.n_trial <= k:
    by.maximize_biscket(by.yen, by.biscket, by.n_trial)
print(by.biscket)