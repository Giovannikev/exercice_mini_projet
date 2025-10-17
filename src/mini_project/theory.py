def rho(lam, mu): return lam/mu
def Ew(lam, mu):
    r = rho(lam, mu)
    return r / (mu * (1 - r))
def Et(lam, mu):
    return 1 / (mu - lam)
def pi_n(lam, mu, n):
    r = rho(lam, mu)
    return (1 - r) * (r ** n)
