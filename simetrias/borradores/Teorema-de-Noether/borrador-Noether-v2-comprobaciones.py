r"""Comprobaciones simbólicas del apartado 8 de borrador-Noether-v2.md (varias funciones)
y de los comentarios del final (varias variables independientes; partícula en un campo central).
Se ejecuta desde la raíz del repositorio con .venv\Scripts\python.exe."""
import sympy as sp

x, B = sp.symbols("x B", real=True)
f1, f2 = sp.Function("f1")(x), sp.Function("f2")(x)
U = sp.Function("U")
r = sp.sqrt(f1**2 + f2**2)

def EL(L, f):
    return sp.diff(L, f) - sp.diff(sp.diff(L, f.diff(x)), x)

def ok(e, msg):
    e = sp.simplify(sp.expand(e))
    print(("OK   " if e == 0 else "FALLA") + " " + msg + ("" if e == 0 else f" -> {e}"))

# Giro con potencial central
L = (f1.diff(x)**2 + f2.diff(x)**2) / 2 - U(r)
E1, E2 = EL(L, f1), EL(L, f2)
xi1, xi2 = -f2, f1
D = sp.diff(L, f1) * xi1 + sp.diff(L, f2) * xi2 + sp.diff(L, f1.diff(x)) * xi1.diff(x) + sp.diff(L, f2.diff(x)) * xi2.diff(x)
ok(D, "giro: D = 0")
Q = sp.diff(L, f1.diff(x)) * xi1 + sp.diff(L, f2.diff(x)) * xi2
ok(Q - (f1 * f2.diff(x) - f2 * f1.diff(x)), "giro: Q = f1 f2' - f2 f1'")
ok(sp.diff(Q, x) + (E1 * xi1 + E2 * xi2), "giro: identidad de Noether Q' = -(phi1 xi1 + phi2 xi2)")
# Energía (tau = 1, xi = 0): Q = -H
H = sp.diff(L, f1.diff(x)) * f1.diff(x) + sp.diff(L, f2.diff(x)) * f2.diff(x) - L
ok(H - ((f1.diff(x)**2 + f2.diff(x)**2) / 2 + U(r)), "energía: H = T + U")
ok(sp.diff(-H, x) + (E1 * (0 - f1.diff(x)) + E2 * (0 - f2.diff(x))), "energía: identidad general con tau = 1")

# Campo magnético uniforme, traslación en y1
Lm = (f1.diff(x)**2 + f2.diff(x)**2) / 2 + B / 2 * (f1 * f2.diff(x) - f2 * f1.diff(x))
Dm = sp.diff(Lm, f1) * 1
ok(Dm - B / 2 * f2.diff(x), "magnético: D = (B/2) f2'")
F = B / 2 * f2
ok(Dm - sp.diff(F, x), "magnético: D = dF/dx con F = (B/2) y2")
Qm = sp.diff(Lm, f1.diff(x)) * 1 - F
ok(Qm - (f1.diff(x) - B * f2), "magnético: Q = f1' - B f2")
ok(sp.diff(Qm, x) + EL(Lm, f1) * 1, "magnético: identidad de Noether")

# Camino paramétrico: cambio de parámetro con tau(x) arbitraria
tau = sp.Function("tau")(x)
Lp = sp.sqrt(f1.diff(x)**2 + f2.diff(x)**2)
p1, p2 = sp.diff(Lp, f1.diff(x)), sp.diff(Lp, f2.diff(x))
Hp = p1 * f1.diff(x) + p2 * f2.diff(x) - Lp
ok(Hp, "paramétrico: H = 0")
Dp = p1 * (0 - tau.diff(x) * f1.diff(x)) + p2 * (0 - tau.diff(x) * f2.diff(x)) + Lp * tau.diff(x)
ok(Dp, "paramétrico: D = 0 con xi = 0 y tau cualquiera")
ok(f1.diff(x) * EL(Lp, f1) + f2.diff(x) * EL(Lp, f2), "paramétrico: f1' phi1 + f2' phi2 = 0")


# Comentarios, pregunta 1: dos variables independientes (t, s) y una función (n = 1, m = 2)
def campos():
    t, s, eps, c = sp.symbols("t s epsilon c", real=True)
    var = (t, s)
    f = sp.Function("f")(t, s)
    y, z1, z2 = sp.symbols("y z1 z2")
    g, W = sp.Function("g"), sp.Function("W")
    # Un lagrangiano y una transformación sin ninguna simetría especial
    Ls = g(y) * z1**2 + sp.sin(s) * z1 * z2 + t * z2**3 + W(y) * s
    reglas = {y: f, z1: f.diff(t), z2: f.diff(s)}
    a_lo_largo = lambda e: e.subs(reglas, simultaneous=True)
    L = a_lo_largo(Ls)
    Ly = a_lo_largo(sp.diff(Ls, y))
    u = [a_lo_largo(sp.diff(Ls, z)) for z in (z1, z2)]
    df = [f.diff(v) for v in var]
    tau = [a_lo_largo(t * y), a_lo_largo(s**2 + y**2)]
    xi = a_lo_largo(sp.sin(t) * y + s)

    # D desde la definición: pendientes J_Y * J_X^(-1) y factor det J_X, exactos en epsilon
    Xt = [var[k] + eps * tau[k] for k in range(2)]
    Yt = f + eps * xi
    JX = sp.Matrix(2, 2, lambda k, l: sp.diff(Xt[k], var[l]))
    JY = sp.Matrix(1, 2, lambda _, l: sp.diff(Yt, var[l]))
    Jf = JY * JX.inv()
    integrando = Ls.subs({y: Yt, z1: Jf[0, 0], z2: Jf[0, 1], t: Xt[0], s: Xt[1]}, simultaneous=True) * JX.det()
    D = sp.diff(integrando, eps).subs(eps, 0)

    phi = Ly - sum(sp.diff(u[k], var[k]) for k in range(2))
    xib = xi - sum(tau[k] * df[k] for k in range(2))
    lema = Ly * xib + sum(u[k] * sp.diff(xib, var[k]) for k in range(2)) + sum(sp.diff(tau[k] * L, var[k]) for k in range(2))
    ok(D - lema, "campos: D desde la definición = lema con divergencia")
    T = [[u[k] * df[l] - (L if k == l else 0) for l in range(2)] for k in range(2)]
    J = [u[k] * xi - sum(T[k][l] * tau[l] for l in range(2)) for k in range(2)]
    ok(sum(sp.diff(J[k], var[k]) for k in range(2)) - D + phi * xib, "campos: div(J + F) - D = -phi xi barra")

    # Un campo F que depende de las derivadas y cuya divergencia es det J_f (n = m = 2)
    h1, h2 = sp.Function("h1")(t, s), sp.Function("h2")(t, s)
    div = sp.diff(h1 * h2.diff(s), t) + sp.diff(-h1 * h2.diff(t), s)
    ok(div - sp.Matrix([[h1.diff(t), h1.diff(s)], [h2.diff(t), h2.diff(s)]]).det(), "campos: div(h1 d2 h2, -h1 d1 h2) = det J")

    # Cuerda vibrante: traslación en t, densidad de energía y flujo
    Lw = f.diff(t)**2 / 2 - c**2 * f.diff(s)**2 / 2
    e = f.diff(t)**2 / 2 + c**2 * f.diff(s)**2 / 2
    uw = [f.diff(t), -c**2 * f.diff(s)]
    Jw = [-(uw[0] * f.diff(t) - Lw), -(uw[1] * f.diff(t))]
    ok(Jw[0] + e, "cuerda: J_1 = -e")
    ok(Jw[1] - c**2 * f.diff(s) * f.diff(t), "cuerda: J_2 = c^2 f_s f_t")
    phiw = -sp.diff(uw[0], t) - sp.diff(uw[1], s)
    ok(sp.diff(Jw[0], t) + sp.diff(Jw[1], s) - phiw * f.diff(t), "cuerda: div J = -phi xi barra, con xi barra = -f_t")


# Comentarios, pregunta 2: partícula en un campo central
def particula():
    t, m = sp.symbols("t m", positive=True)
    V = sp.Function("V")
    r, th, ph = [sp.Function(n)(t) for n in ("r", "theta", "phi")]
    xs, ys, zs = r * sp.sin(th) * sp.cos(ph), r * sp.sin(th) * sp.sin(ph), r * sp.cos(th)
    vel = [sp.diff(c, t) for c in (xs, ys, zs)]
    L = sp.simplify(m * sum(v**2 for v in vel) / 2 - V(r))
    ok(L - (m * (r.diff(t)**2 + r**2 * th.diff(t)**2 + r**2 * sp.sin(th)**2 * ph.diff(t)**2) / 2 - V(r)), "esféricas: L")
    q = [r, th, ph]
    p = [sp.diff(L, c.diff(t)) for c in q]
    ecs = [sp.diff(L, c) - sp.diff(pi, t) for c, pi in zip(q, p)]
    acc = sp.solve(ecs, [c.diff(t, 2) for c in q], dict=True)[0]
    l = [m * (ys * vel[2] - zs * vel[1]), m * (zs * vel[0] - xs * vel[2]), m * (xs * vel[1] - ys * vel[0])]
    gens = [(0, -sp.sin(ph), -sp.cot(th) * sp.cos(ph)), (0, sp.cos(ph), -sp.cot(th) * sp.sin(ph)), (0, 0, 1)]
    for eje, gen, lk in zip("xyz", gens, l):
        Q = sum(pi * gi for pi, gi in zip(p, gen))
        ok(Q - lk, f"esféricas: giro alrededor de {eje}, Q = l_{eje}")
        ok(sp.diff(Q, t).subs(acc), f"esféricas: l_{eje} constante sobre las soluciones")
    ok(l[0] + m * r**2 * (sp.sin(ph) * th.diff(t) + sp.sin(th) * sp.cos(th) * sp.cos(ph) * ph.diff(t)), "esféricas: expresión de l_x")
    ok(l[1] - m * r**2 * (sp.cos(ph) * th.diff(t) - sp.sin(th) * sp.cos(th) * sp.sin(ph) * ph.diff(t)), "esféricas: expresión de l_y")
    ok(sum(lk**2 for lk in l) - (p[1]**2 + p[2]**2 / sp.sin(th)**2), "esféricas: |l|^2 = p_theta^2 + p_phi^2 / sin^2(theta)")
    H = sum(pi * c.diff(t) for pi, c in zip(p, q)) - L
    ok(H - (m * (r.diff(t)**2 + r**2 * th.diff(t)**2 + r**2 * sp.sin(th)**2 * ph.diff(t)**2) / 2 + V(r)), "esféricas: H = energía")
    ok(sp.diff(H, t).subs(acc), "esféricas: energía constante sobre las soluciones")

    # Cartesianas: traslación y cambio de velocidad
    R = [sp.Function(n)(t) for n in ("X", "Y", "Z")]
    e = sp.symbols("e1:4", real=True)
    u = sp.symbols("u1:4", real=True)
    rho = sp.sqrt(sum(c**2 for c in R))
    rr = sp.Symbol("rr", positive=True)
    Vp = sp.diff(V(rr), rr).subs(rr, rho)
    Lc = m * sum(c.diff(t)**2 for c in R) / 2 - V(rho)
    pc = [sp.diff(Lc, c.diff(t)) for c in R]
    dot = lambda a, b: sum(ai * bi for ai, bi in zip(a, b))
    D = dot([sp.diff(Lc, c) for c in R], e)
    ok(D + Vp * dot(e, R) / rho, "traslación: D = -V'(r) (e . r) / r")
    xi = [-ui * t for ui in u]
    D = dot([sp.diff(Lc, c) for c in R], xi) + dot(pc, [sp.diff(c, t) for c in xi])
    ok(D - (t * Vp * dot(u, R) / rho - m * dot(u, [c.diff(t) for c in R])), "cambio de velocidad: D = t V'(r) (u . r) / r - m u . v")
    # Partícula libre: F = -m u . r y Q = u . (m r - p t)
    L0 = m * sum(c.diff(t)**2 for c in R) / 2
    p0 = [sp.diff(L0, c.diff(t)) for c in R]
    D0 = dot(p0, [sp.diff(c, t) for c in xi])
    F0 = -m * dot(u, R)
    ok(D0 - sp.diff(F0, t), "libre: D = dF/dt con F = -m u . r")
    Q0 = dot(p0, xi) - F0
    ok(Q0 - dot(u, [m * c - pi * t for c, pi in zip(R, p0)]), "libre: Q = u . (m r - p t)")
    ok(sp.diff(Q0, t).subs({c.diff(t, 2): 0 for c in R}), "libre: Q constante sobre las soluciones")

    # Dos cuerpos con V(|r1 - r2|): el cambio de velocidad de los dos es una simetría
    m1, m2 = sp.symbols("m1 m2", positive=True)
    R1 = [sp.Function(n)(t) for n in ("X1", "Y1", "Z1")]
    R2 = [sp.Function(n)(t) for n in ("X2", "Y2", "Z2")]
    d12 = sp.sqrt(sum((a - b)**2 for a, b in zip(R1, R2)))
    L2 = m1 * sum(c.diff(t)**2 for c in R1) / 2 + m2 * sum(c.diff(t)**2 for c in R2) / 2 - V(d12)
    todas = R1 + R2
    p2 = [sp.diff(L2, c.diff(t)) for c in todas]
    xi2 = xi + xi
    D2 = dot([sp.diff(L2, c) for c in todas], xi2) + dot(p2, [sp.diff(c, t) for c in xi2])
    F2 = -dot(u, [m1 * a + m2 * b for a, b in zip(R1, R2)])
    ok(D2 - sp.diff(F2, t), "dos cuerpos: D = dF/dt con F = -u . (m1 r1 + m2 r2)")
    Q2 = dot(p2, xi2) - F2
    P = [p2[k] + p2[k + 3] for k in range(3)]
    ok(Q2 - dot(u, [m1 * a + m2 * b - Pk * t for a, b, Pk in zip(R1, R2, P)]), "dos cuerpos: Q = u . (M R - P t)")
    ecs2 = [sp.diff(L2, c) - sp.diff(pi, t) for c, pi in zip(todas, p2)]
    acc2 = sp.solve(ecs2, [c.diff(t, 2) for c in todas], dict=True)[0]
    ok(sp.diff(Q2, t).subs(acc2), "dos cuerpos: Q constante sobre las soluciones")


campos()
particula()
