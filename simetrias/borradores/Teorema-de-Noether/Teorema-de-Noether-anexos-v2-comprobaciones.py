r"""Comprobaciones simbólicas de «El teorema de Noether: anexos (versión 2)»: rotaciones, exponencial
de una matriz, grupos de Galileo, de Lorentz y de Poincaré, contracción y carga central.
Se ejecuta desde la raíz del repositorio con .venv\Scripts\python.exe -W error; termina con
«FALLOS: ninguno» si todo es correcto."""
import sympy as sp

fallos = []


def ok(e, msg):
    if isinstance(e, sp.MatrixBase):
        e = e.applyfunc(lambda z: sp.simplify(sp.expand(z)))
        nulo = all(z == 0 for z in e)
    else:
        e = sp.simplify(sp.expand(e))
        nulo = e == 0
    print(("OK   " if nulo else "FALLA") + " " + msg)
    if not nulo:
        fallos.append(msg)


def conm(A, B):
    return A * B - B * A


I3, I4, I5 = sp.eye(3), sp.eye(4), sp.eye(5)
th, s, z = sp.symbols("theta s zeta", real=True)


def R1(a):
    return sp.Matrix([[1, 0, 0], [0, sp.cos(a), -sp.sin(a)], [0, sp.sin(a), sp.cos(a)]])


def R2(a):
    return sp.Matrix([[sp.cos(a), 0, sp.sin(a)], [0, 1, 0], [-sp.sin(a), 0, sp.cos(a)]])


def R3(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a), 0], [sp.sin(a), sp.cos(a), 0], [0, 0, 1]])


def cruz(w):
    """Matriz antisimétrica A con A v = w x v."""
    return sp.Matrix([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])


J = [cruz(e) for e in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1]))]


# 1. Rotaciones en tres dimensiones
def rotaciones():
    for k, Rk in enumerate((R1, R2, R3), start=1):
        ok(Rk(th).T * Rk(th) - I3, f"rotaciones: R_{k}^T R_{k} = I")
        ok(Rk(th).det() - 1, f"rotaciones: det R_{k} = 1")
        ok(sp.diff(Rk(th), th).subs(th, 0) - J[k - 1], f"rotaciones: dR_{k}/dtheta en 0 = J_{k}")
    t1, t2, t3 = sp.symbols("theta1:4", real=True)
    c1, c2, c3 = sp.cos(t1), sp.cos(t2), sp.cos(t3)
    s1, s2, s3 = sp.sin(t1), sp.sin(t2), sp.sin(t3)
    R = R3(t3) * R2(t2) * R1(t1)
    Rexp = sp.Matrix([[c3 * c2, c3 * s2 * s1 - s3 * c1, c3 * s2 * c1 + s3 * s1],
                      [s3 * c2, s3 * s2 * s1 + c3 * c1, s3 * s2 * c1 - c3 * s1],
                      [-s2, c2 * s1, c2 * c1]])
    ok(R - Rexp, "rotaciones: R(theta1, theta2, theta3) = R3 R2 R1")
    ok(R.T * R - I3, "rotaciones: R^T R = I para la rotación general")
    col1 = sp.Matrix([c3 * c2, s3 * c2, -s2])
    w1 = sp.Matrix([-s3, c3, 0])
    w2 = col1.cross(w1)
    ok(w2 - sp.Matrix([c3 * s2, s3 * s2, c2]), "rotaciones: w2 = c1 x w1")
    col2 = c1 * w1 + s1 * w2
    ok(sp.Matrix.hstack(col1, col2, col1.cross(col2)) - Rexp, "rotaciones: construcción por columnas")
    h = sp.pi / 2
    ok(R1(h) * R2(h) - sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), "rotaciones: R1(pi/2) R2(pi/2)")
    ok(R2(h) * R1(h) - sp.Matrix([[0, 1, 0], [0, 0, -1], [-1, 0, 0]]), "rotaciones: R2(pi/2) R1(pi/2)")
    w = sp.Matrix(sp.symbols("w1:4", real=True))
    v = sp.Matrix(sp.symbols("v1:4", real=True))
    ok(cruz(w) * v - w.cross(v), "rotaciones: A v = w x v")
    ok(conm(J[0], J[1]) - J[2], "rotaciones: [J1, J2] = J3")
    ok(conm(J[1], J[2]) - J[0], "rotaciones: [J2, J3] = J1")
    ok(conm(J[2], J[0]) - J[1], "rotaciones: [J3, J1] = J2")
    ok(R3(th) - (I3 + sp.sin(th) * J[2] + (1 - sp.cos(th)) * J[2]**2), "rotaciones: R3 = I + sin J3 + (1 - cos) J3^2")


# 2. La exponencial de una matriz
def exponencial():
    al, be = sp.symbols("alpha beta", real=True)
    n = sp.Matrix([sp.sin(al) * sp.cos(be), sp.sin(al) * sp.sin(be), sp.cos(al)])
    An = cruz(n)
    ok(An**3 + An, "exponencial: A_n^3 = -A_n")
    Rod = I3 + sp.sin(th) * An + (1 - sp.cos(th)) * An**2
    ok(sp.diff(Rod, th) - An * Rod, "exponencial: la fórmula de Rodrigues cumple dM/dtheta = A_n M")
    ok(Rod.subs(th, 0) - I3, "exponencial: Rodrigues en theta = 0 es I")
    ok(Rod.T * Rod - I3, "exponencial: Rodrigues es ortogonal")
    # det(I + h M) = 1 + h tr M + O(h^2)
    h = sp.Symbol("h")
    M = sp.Matrix(3, 3, sp.symbols("m1:10"))
    d = sp.expand((I3 + h * M).det())
    ok(d.coeff(h, 0) - 1, "exponencial: det(I + h M) en h = 0")
    ok(d.coeff(h, 1) - M.trace(), "exponencial: coeficiente de h en det(I + h M) = tr M")
    # producto de exponenciales hasta segundo orden
    A = sp.Matrix(3, 3, sp.symbols("a1:10"))
    Bm = sp.Matrix(3, 3, sp.symbols("b1:10"))
    e2 = lambda X: I3 + s * X + s**2 * X**2 / 2
    trunc = lambda Mx: Mx.applyfunc(lambda z: sp.expand(z).series(s, 0, 3).removeO())
    izq = trunc(e2(A) * e2(Bm))
    C = s * (A + Bm) + s**2 * conm(A, Bm) / 2
    der = trunc(I3 + C + C**2 / 2)
    ok(izq - der, "exponencial: e^{sA} e^{sB} = e^{s(A+B) + s^2 [A,B]/2} + O(s^3)")
    em2 = lambda X: I3 - s * X + s**2 * X**2 / 2
    com = trunc(e2(A) * e2(Bm) * em2(A) * em2(Bm))
    ok(com - trunc(I3 + s**2 * conm(A, Bm)), "exponencial: e^{sA} e^{sB} e^{-sA} e^{-sB} = I + s^2 [A,B] + O(s^3)")
    # potencias que se repiten con signo +: K^3 = K
    K = sp.zeros(4, 4)
    K[0, 1:] = n.T
    K[1:, 0] = n
    ok(K**3 - K, "exponencial: n . K cumple (n . K)^3 = n . K")
    H = I4 + sp.sinh(z) * K + (sp.cosh(z) - 1) * K**2
    ok(sp.diff(H, z) - K * H, "exponencial: I + sinh K + (cosh - 1) K^2 cumple dM/dzeta = K M")


# Matrices de Galileo, 5 x 5, sobre (q, t, 1)
def Gam(R, v, a, b):
    M = sp.zeros(5, 5)
    M[:3, :3] = R
    M[:3, 3] = v
    M[:3, 4] = a
    M[3, 3] = 1
    M[3, 4] = b
    M[4, 4] = 1
    return M


def Eij(i, j, n=5):
    M = sp.zeros(n, n)
    M[i, j] = 1
    return M


def galileo():
    v1, v2, a1, a2 = (sp.Matrix(sp.symbols(f"{nm}1:4", real=True)) for nm in ("v", "w", "a", "c"))
    b1, b2 = sp.symbols("b1 b2", real=True)
    Ra = sp.Matrix(3, 3, sp.symbols("r1:10", real=True))
    Rb = sp.Matrix(3, 3, sp.symbols("p1:10", real=True))
    G1, G2 = Gam(Ra, v1, a1, b1), Gam(Rb, v2, a2, b2)
    ok(G2 * G1 - Gam(Rb * Ra, Rb * v1 + v2, Rb * a1 + v2 * b1 + a2, b1 + b2), "Galileo: ley de composición")
    t1, t2, t3 = sp.symbols("theta1:4", real=True)
    R = R3(t3) * R2(t2) * R1(t1)
    G = Gam(R, v1, a1, b1)
    Gi = Gam(R.T, -R.T * v1, -R.T * (a1 - v1 * b1), -b1)
    ok(Gi * G - I5, "Galileo: inversa por la izquierda")
    ok(G * Gi - I5, "Galileo: inversa por la derecha")
    u = sp.Matrix(sp.symbols("u1:4", real=True))
    z3 = sp.zeros(3, 1)
    ok((Gam(I3, u, z3, 0) * Gam(I3, z3, z3, b1))[:3, 4] - u * b1, "Galileo: tiempo y después velocidad, a = u b")
    ok((Gam(I3, z3, z3, b1) * Gam(I3, u, z3, 0))[:3, 4], "Galileo: velocidad y después tiempo, a = 0")
    # generadores
    Jg = []
    for k in range(3):
        M = sp.zeros(5, 5)
        M[:3, :3] = J[k]
        Jg.append(M)
    Kg = [Eij(k, 3) for k in range(3)]
    Pg = [Eij(k, 4) for k in range(3)]
    T = Eij(3, 4)
    cic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    for i, j, k in cic:
        ok(conm(Jg[i], Jg[j]) - Jg[k], f"Galileo: [J{i+1}, J{j+1}] = J{k+1}")
        ok(conm(Jg[i], Kg[j]) - Kg[k], f"Galileo: [J{i+1}, K{j+1}] = K{k+1}")
        ok(conm(Jg[i], Pg[j]) - Pg[k], f"Galileo: [J{i+1}, P{j+1}] = P{k+1}")
    for i in range(3):
        ok(conm(Jg[i], T), f"Galileo: [J{i+1}, T] = 0")
        ok(conm(Kg[i], T) - Pg[i], f"Galileo: [K{i+1}, T] = P{i+1}")
        ok(conm(Pg[i], T), f"Galileo: [P{i+1}, T] = 0")
        for j in range(3):
            ok(conm(Kg[i], Kg[j]), f"Galileo: [K{i+1}, K{j+1}] = 0")
            ok(conm(Kg[i], Pg[j]), f"Galileo: [K{i+1}, P{j+1}] = 0")
            ok(conm(Pg[i], Pg[j]), f"Galileo: [P{i+1}, P{j+1}] = 0")
    ok(conm(Jg[0], Kg[0]), "Galileo: [J1, K1] = 0")
    # forma de producto: Gamma(R, v, a, b) = e^{a.P + b T} e^{v.K} Gamma(R, 0, 0, 0)
    X1 = sum((a1[k] * Pg[k] for k in range(3)), sp.zeros(5, 5)) + b1 * T
    ok(X1**2, "Galileo: (a . P + b T)^2 = 0")
    X2 = sum((v1[k] * Kg[k] for k in range(3)), sp.zeros(5, 5))
    ok(X2**2, "Galileo: (v . K)^2 = 0")
    ok((I5 + X1) * (I5 + X2) * Gam(Ra, z3, z3, 0) - Gam(Ra, v1, a1, b1), "Galileo: forma de producto")
    # una sola exponencial: V y W
    al, be = sp.symbols("alpha beta", real=True)
    n = sp.Matrix([sp.sin(al) * sp.cos(be), sp.sin(al) * sp.sin(be), sp.cos(al)])
    An = cruz(n)
    E = lambda x: I3 + sp.sin(x) * An + (1 - sp.cos(x)) * An**2
    V = lambda x: I3 + (1 - sp.cos(x)) / x * An + (x - sp.sin(x)) / x * An**2
    W = lambda x: I3 / 2 + (x - sp.sin(x)) / x**2 * An + (x**2 / 2 - 1 + sp.cos(x)) / x**2 * An**2
    ok(sp.diff(s * V(s), s) - E(s), "Galileo: d/ds [s V(s A_n)] = e^{s A_n}")
    ok(sp.diff(s**2 * W(s), s) - s * V(s), "Galileo: d/ds [s^2 W(s A_n)] = s V(s A_n)")
    ok((V(s) * s).applyfunc(lambda e: sp.limit(e, s, 0)), "Galileo: s V(s A_n) se anula en s = 0")
    ok((W(s) * s**2).applyfunc(lambda e: sp.limit(e, s, 0)), "Galileo: s^2 W(s A_n) se anula en s = 0")


# Lorentz y Poincaré sobre (c t, q) y (c t, q, 1); filas y columnas numeradas desde 0
eta = sp.diag(1, -1, -1, -1)


def lorentz():
    c, v = sp.symbols("c v", positive=True)
    gam = 1 / sp.sqrt(1 - v**2 / c**2)
    B1 = sp.eye(4)
    B1[0, 0] = B1[1, 1] = gam
    B1[0, 1] = B1[1, 0] = gam * v / c
    t, q1 = sp.symbols("t q1", real=True)
    x = sp.Matrix([c * t, q1, 0, 0])
    xp = B1 * x
    ok(xp[0] / c - gam * (t + v * q1 / c**2), "Lorentz: t' = gamma (t + v q1 / c^2), activo")
    ok(xp[1] - gam * (q1 + v * t), "Lorentz: q1' = gamma (q1 + v t), activo")
    ok(B1.T * eta * B1 - eta, "Lorentz: B1^T eta B1 = eta")
    Kl = []
    for k in range(1, 4):
        M = sp.zeros(4, 4)
        M[0, k] = M[k, 0] = 1
        Kl.append(M)
    Jl = []
    for k in range(3):
        M = sp.zeros(4, 4)
        M[1:, 1:] = J[k]
        Jl.append(M)
    Bz = I4 + sp.sinh(z) * Kl[0] + (sp.cosh(z) - 1) * Kl[0]**2
    ok(Bz - sp.Matrix([[sp.cosh(z), sp.sinh(z), 0, 0], [sp.sinh(z), sp.cosh(z), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), "Lorentz: e^{zeta K1} con cosh y sinh")
    ok(B1 - Bz.subs(z, sp.atanh(v / c)), "Lorentz: la rapidez cumple tanh zeta = v / c, cosh zeta = gamma")
    for X, nom in [(Kl[0], "K1"), (Jl[2], "J3")]:
        ok(X.T * eta + eta * X, f"Lorentz: {nom}^T eta + eta {nom} = 0")
    cic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    for i, j, k in cic:
        ok(conm(Jl[i], Jl[j]) - Jl[k], f"Lorentz: [J{i+1}, J{j+1}] = J{k+1}")
        ok(conm(Jl[i], Kl[j]) - Kl[k], f"Lorentz: [J{i+1}, K{j+1}] = K{k+1}")
        ok(conm(Kl[i], Kl[j]) + Jl[k], f"Lorentz: [K{i+1}, K{j+1}] = -J{k+1}")
    for i in range(3):
        ok(conm(Jl[i], Kl[i]), f"Lorentz: [J{i+1}, K{i+1}] = 0")
    # cambio de velocidad en una dirección cualquiera
    al, be = sp.symbols("alpha beta", real=True)
    n = sp.Matrix([sp.sin(al) * sp.cos(be), sp.sin(al) * sp.sin(be), sp.cos(al)])
    Kn = sum((n[k] * Kl[k] for k in range(3)), sp.zeros(4, 4))
    Bn = I4 + sp.sinh(z) * Kn + (sp.cosh(z) - 1) * Kn**2
    bloque = sp.zeros(4, 4)
    bloque[0, 0] = sp.cosh(z)
    bloque[0, 1:] = sp.sinh(z) * n.T
    bloque[1:, 0] = sp.sinh(z) * n
    bloque[1:, 1:] = I3 + (sp.cosh(z) - 1) * n * n.T
    ok(Bn - bloque, "Lorentz: forma por bloques del cambio de velocidad en la dirección n")
    ok(Bn.T * eta * Bn - eta, "Lorentz: el cambio de velocidad general conserva eta")
    ok(eta * Bn.T * eta * Bn - I4, "Lorentz: inversa eta B^T eta")
    # suma de rapideces y de velocidades
    z1, z2 = sp.symbols("zeta1 zeta2", real=True)
    ok(Bz.subs(z, z1) * Bz.subs(z, z2) - Bz.subs(z, z1 + z2), "Lorentz: las rapideces se suman")
    u1, u2 = sp.symbols("u1 u2", real=True)
    ok(sp.expand_trig(sp.tanh(z1 + z2)) - (sp.tanh(z1) + sp.tanh(z2)) / (1 + sp.tanh(z1) * sp.tanh(z2)), "Lorentz: tanh de la suma")
    # orto-cronía: a b - sqrt(a^2 - 1) sqrt(b^2 - 1) > 0, por (a b)^2 - (a^2 - 1)(b^2 - 1) = a^2 + b^2 - 1
    a, b = sp.symbols("a b", positive=True)
    ok((a * b)**2 - (a**2 - 1) * (b**2 - 1) - (a**2 + b**2 - 1), "Lorentz: (a b)^2 - (a^2-1)(b^2-1) = a^2 + b^2 - 1")
    # descomposición polar de dos cambios de velocidad no paralelos (rotación de Thomas–Wigner)
    Bx = Bz.subs(z, z1)
    By = I4 + sp.sinh(z2) * Kl[1] + (sp.cosh(z2) - 1) * Kl[1]**2
    L = By * Bx
    col = L[:, 0]
    w = col[1:, 0]
    nw = sp.sqrt(sum(e**2 for e in w))
    Bp = sp.zeros(4, 4)
    Bp[0, 0] = col[0]
    Bp[0, 1:] = w.T
    Bp[1:, 0] = w
    Bp[1:, 1:] = I3 + (col[0] - 1) / nw**2 * w * w.T
    ok(Bp.T * eta * Bp - eta, "Lorentz: el cambio de velocidad de la primera columna es de Lorentz")
    Rp = (eta * Bp.T * eta) * L
    ok(Rp[0, 1:], "Lorentz: B^{-1} Lambda tiene primera fila (1, 0, 0, 0)")
    ok(Rp[1:, 0], "Lorentz: B^{-1} Lambda tiene primera columna (1, 0, 0, 0)")
    ok(Rp[0, 0] - 1, "Lorentz: B^{-1} Lambda tiene elemento (0, 0) igual a 1")
    Rr = Rp[1:, 1:]
    ok(Rr.T * Rr - I3, "Lorentz: el bloque espacial es ortogonal (rotación de Thomas–Wigner)")
    print("     rotación de Thomas–Wigner, elemento (1, 2):", sp.simplify(Rr[0, 1]))
    # primer orden: generador de la parte física
    eps, uu = sp.symbols("epsilon u", real=True)
    X = (eps * uu / c) * Kl[0]
    dx = X * sp.Matrix([c * t, q1, 0, 0])
    ok(dx[0] / c - eps * uu * q1 / c**2, "Lorentz: tau = u q1 / c^2")
    ok(dx[1] - eps * uu * t, "Lorentz: xi = u t")


def Pi(L, a):
    M = sp.zeros(5, 5)
    M[:4, :4] = L
    M[:4, 4] = a
    M[4, 4] = 1
    return M


def poincare():
    L1 = sp.Matrix(4, 4, sp.symbols("l1:17", real=True))
    L2 = sp.Matrix(4, 4, sp.symbols("k1:17", real=True))
    a1 = sp.Matrix(sp.symbols("a0:4", real=True))
    a2 = sp.Matrix(sp.symbols("b0:4", real=True))
    ok(Pi(L2, a2) * Pi(L1, a1) - Pi(L2 * L1, L2 * a1 + a2), "Poincaré: ley de composición")
    Bz = sp.eye(4)
    Bz[0, 0] = Bz[1, 1] = sp.cosh(z)
    Bz[0, 1] = Bz[1, 0] = sp.sinh(z)
    Bzi = eta * Bz.T * eta
    ok(Pi(Bzi, -Bzi * a1) * Pi(Bz, a1) - I5, "Poincaré: inversa")
    Jp, Kp = [], []
    for k in range(3):
        M = sp.zeros(5, 5)
        M[1:4, 1:4] = J[k]
        Jp.append(M)
        M = sp.zeros(5, 5)
        M[0, k + 1] = M[k + 1, 0] = 1
        Kp.append(M)
    Pp = [Eij(mu, 4) for mu in range(4)]
    cic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    for i, j, k in cic:
        ok(conm(Jp[i], Pp[j + 1]) - Pp[k + 1], f"Poincaré: [J{i+1}, P{j+1}] = P{k+1}")
    for i in range(3):
        ok(conm(Jp[i], Pp[0]), f"Poincaré: [J{i+1}, P0] = 0")
        ok(conm(Kp[i], Pp[0]) - Pp[i + 1], f"Poincaré: [K{i+1}, P0] = P{i+1}")
        for j in range(3):
            ok(conm(Kp[i], Pp[j + 1]) - (Pp[0] if i == j else sp.zeros(5, 5)), f"Poincaré: [K{i+1}, P{j+1}] = delta P0")
    for mu in range(4):
        for nu in range(4):
            ok(conm(Pp[mu], Pp[nu]), f"Poincaré: [P{mu}, P{nu}] = 0")
    # forma de producto
    Xa = sum((a1[mu] * Pp[mu] for mu in range(4)), sp.zeros(5, 5))
    ok(Xa**2, "Poincaré: (a . P)^2 = 0")
    ok((I5 + Xa) * Pi(L1, sp.zeros(4, 1)) - Pi(L1, a1), "Poincaré: Pi(Lambda, a) = e^{a . P} Pi(Lambda, 0)")
    # una sola exponencial con X = zeta K1: V(X) = I + (cosh - 1)/zeta K + (sinh - zeta)/zeta K^2
    K1 = sp.zeros(4, 4)
    K1[0, 1] = K1[1, 0] = 1
    E = lambda x: I4 + sp.sinh(x) * K1 + (sp.cosh(x) - 1) * K1**2
    V = lambda x: I4 + (sp.cosh(x) - 1) / x * K1 + (sp.sinh(x) - x) / x * K1**2
    ok(sp.diff(s * V(s), s) - E(s), "Poincaré: d/ds [s V(s K1)] = e^{s K1}")
    ok((s * V(s)).applyfunc(lambda e: sp.limit(e, s, 0)), "Poincaré: s V(s K1) se anula en s = 0")
    # campo del generador general sobre (c t, q, 1)
    c = sp.Symbol("c", positive=True)
    t = sp.Symbol("t", real=True)
    q = sp.Matrix(sp.symbols("q1:4", real=True))
    om = sp.Matrix(sp.symbols("omega1:4", real=True))
    u = sp.Matrix(sp.symbols("u1:4", real=True))
    d = sp.Matrix(sp.symbols("d1:4", real=True))
    tau = sp.Symbol("tau", real=True)
    X = (sum((om[k] * Jp[k] + u[k] / c * Kp[k] + d[k] * Pp[k + 1] for k in range(3)), sp.zeros(5, 5)) + c * tau * Pp[0])
    campo = X * sp.Matrix([c * t, q[0], q[1], q[2], 1])
    ok(campo[0] / c - (tau + u.dot(q) / c**2), "Poincaré: dt/ds = tau + u . q / c^2")
    ok(campo[1:4, 0] - (om.cross(q) + u * t + d), "Poincaré: dq/ds = omega x q + u t + d")


def contraccion():
    c = sp.Symbol("c", positive=True)
    # S lleva (c t, q, 1) a (q, t, 1)
    S = sp.zeros(5, 5)
    S[0, 1] = S[1, 2] = S[2, 3] = 1
    S[3, 0] = 1 / c
    S[4, 4] = 1
    Si = S.inv()
    Kp, Jp = [], []
    for k in range(3):
        M = sp.zeros(5, 5)
        M[0, k + 1] = M[k + 1, 0] = 1
        Kp.append(M)
        M = sp.zeros(5, 5)
        M[1:4, 1:4] = J[k]
        Jp.append(M)
    P0 = Eij(0, 4)
    Pk = [Eij(k + 1, 4) for k in range(3)]
    Kc = [S * (Kp[k] / c) * Si for k in range(3)]
    Tc = S * (c * P0) * Si
    Pc = [S * Pk[k] * Si for k in range(3)]
    Jc = [S * Jp[k] * Si for k in range(3)]
    Kg = [Eij(k, 3) for k in range(3)]
    Pg = [Eij(k, 4) for k in range(3)]
    Tg = Eij(3, 4)
    for k in range(3):
        ok(Kc[k] - (Kg[k] + Eij(3, k) / c**2), f"contracción: K{k+1} en (q, t, 1) = K{k+1} de Galileo + E_t{k+1} / c^2")
        ok(Kc[k].applyfunc(lambda e: sp.limit(e, c, sp.oo)) - Kg[k], f"contracción: K{k+1} tiende al de Galileo")
        ok(Pc[k] - Pg[k], f"contracción: P{k+1} coincide con el de Galileo")
        ok(Jc[k][:3, :3] - J[k], f"contracción: J{k+1} coincide con el de Galileo")
    ok(Tc - Tg, "contracción: c P0 en (q, t, 1) es el T de Galileo")
    cic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    for i, j, k in cic:
        ok(conm(Kc[i], Kc[j]) + Jc[k] / c**2, f"contracción: [K{i+1}, K{j+1}] = -J{k+1} / c^2")
    for i in range(3):
        ok(conm(Kc[i], Tc) - Pc[i], f"contracción: [K{i+1}, T] = P{i+1}")
        for j in range(3):
            ok(conm(Kc[i], Pc[j]) - (Tc / c**2 if i == j else sp.zeros(5, 5)), f"contracción: [K{i+1}, P{j+1}] = delta T / c^2")


def carga_central():
    # corchetes de Poisson de las cantidades conservadas
    m1, m2, c = sp.symbols("m1 m2 c", positive=True)
    t = sp.Symbol("t", real=True)
    qs = [sp.Matrix([sp.Symbol(f"x{j}_{k}", real=True) for k in (1, 2, 3)]) for j in (1, 2)]
    ps = [sp.Matrix([sp.Symbol(f"y{j}_{k}", real=True) for k in (1, 2, 3)]) for j in (1, 2)]
    allq = list(qs[0]) + list(qs[1])
    allp = list(ps[0]) + list(ps[1])
    pb = lambda f, g: sum(sp.diff(f, a) * sp.diff(g, b) - sp.diff(f, b) * sp.diff(g, a) for a, b in zip(allq, allp))
    M = m1 + m2
    P = ps[0] + ps[1]
    G = m1 * qs[0] + m2 * qs[1] - P * t
    Jt = qs[0].cross(ps[0]) + qs[1].cross(ps[1])
    H = ps[0].dot(ps[0]) / (2 * m1) + ps[1].dot(ps[1]) / (2 * m2)
    for j in range(3):
        ok(pb(G[j], H) - P[j], f"carga central: {{G{j+1}, H}} = P{j+1}")
        for k in range(3):
            ok(pb(G[j], P[k]) - (M if j == k else 0), f"carga central: {{G{j+1}, P{k+1}}} = M delta")
            ok(pb(G[j], G[k]), f"carga central: {{G{j+1}, G{k+1}}} = 0")
    ok(pb(Jt[0], Jt[1]) - Jt[2], "carga central: {J1, J2} = J3")
    ok(pb(Jt[0], P[1]) - P[2], "carga central: {J1, P2} = P3")
    ok(pb(Jt[0], G[1]) - G[2], "carga central: {J1, G2} = G3")
    ok(pb(P[0], H), "carga central: {P1, H} = 0")
    ok(pb(Jt[0], H), "carga central: {J1, H} = 0")
    # partícula relativista libre
    q = sp.Matrix(sp.symbols("x1:4", real=True))
    p = sp.Matrix(sp.symbols("y1:4", real=True))
    m = sp.Symbol("m", positive=True)
    pb1 = lambda f, g: sum(sp.diff(f, a) * sp.diff(g, b) - sp.diff(f, b) * sp.diff(g, a) for a, b in zip(q, p))
    E = sp.sqrt(p.dot(p) * c**2 + m**2 * c**4)
    Gr = E * q / c**2 - p * t
    ell = q.cross(p)
    for j in range(3):
        ok(pb1(Gr[j], E) - p[j], f"carga central: {{G_rel{j+1}, E}} = p{j+1}")
        for k in range(3):
            ok(pb1(Gr[j], p[k]) - (E / c**2 if j == k else 0), f"carga central: {{G_rel{j+1}, p{k+1}}} = delta E / c^2")
    ok(pb1(Gr[0], Gr[1]) + ell[2] / c**2, "carga central: {G_rel1, G_rel2} = -l3 / c^2")
    ok(sp.limit(E / c**2, c, sp.oo) - m, "carga central: E / c^2 tiende a m")
    # mecánica cuántica: [G_j, p_k] = i hbar m delta_jk
    x1 = sp.Symbol("x1", real=True)
    hb = sp.Symbol("hbar", positive=True)
    f = sp.Function("f")(x1)
    Gq = lambda h: m * x1 * h - t * (-sp.I * hb * sp.diff(h, x1))
    pq = lambda h: -sp.I * hb * sp.diff(h, x1)
    ok(Gq(pq(f)) - pq(Gq(f)) - sp.I * hb * m * f, "carga central: [G1, p1] = i hbar m")


rotaciones()
exponencial()
galileo()
lorentz()
poincare()
contraccion()
carga_central()
print("FALLOS: " + ("ninguno" if not fallos else ", ".join(fallos)))
