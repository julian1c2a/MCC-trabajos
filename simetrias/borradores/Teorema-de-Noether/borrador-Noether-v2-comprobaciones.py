r"""Comprobaciones simbólicas de los apartados 6.7 (casos particulares), 8 (varias funciones), 9 (varias variables) y 10 (flujos)
de borrador-Noether-v2.md y de los comentarios del final (partícula en un campo central).
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


# Apartado 6.7: los dos casos particulares, con una sola función
def apartado6_casos():
    f = sp.Function("f")(x)
    g, h, c = sp.Function("g"), sp.Function("h"), sp.Function("c")
    fp = f.diff(x)
    # Beltrami con L dependiente de x: H' = -d_x L - phi f'
    y, z = sp.symbols("y z")
    Ls = g(y) * z**2 + sp.sin(x) * z * y + x**2 * h(y) + x * z**3
    al = lambda e: e.subs({y: f, z: fp}, simultaneous=True)
    L, p = al(Ls), al(sp.diff(Ls, z))
    phi = al(sp.diff(Ls, y)) - sp.diff(p, x)
    H = p * fp - L
    ok(sp.diff(H, x) + al(sp.diff(Ls, x)) + phi * fp, "6.7: H' = -d_x L - phi f' (Beltrami con L dependiente de x)")
    # Coordenada con d_y L = c(x): Q = p - int c, con Q' = -phi
    s = sp.Symbol("s")
    Lc = fp**2 / 2 + c(x) * f
    Qc = sp.diff(Lc, fp) - sp.Integral(c(s), (s, 0, x))
    ok(sp.diff(Qc, x).doit() + EL(Lc, f), "6.7: d_y L = gamma(x), Q = p - int gamma y Q' = -phi")


# Apartado 8.5: lagrangiano homogéneo de grado 1 (principio de Fermat en el plano)
def apartado8_homogeneo():
    n = sp.Function("n")
    Lf = n(f1, f2) * sp.sqrt(f1.diff(x)**2 + f2.diff(x)**2)
    p1, p2 = sp.diff(Lf, f1.diff(x)), sp.diff(Lf, f2.diff(x))
    ok(p1 * f1.diff(x) + p2 * f2.diff(x) - Lf, "8.5: L homogénea de grado 1, H = 0")
    ok(f1.diff(x) * EL(Lf, f1) + f2.diff(x) * EL(Lf, f2), "8.5: L homogénea de grado 1, f1' phi1 + f2' phi2 = 0")


# Apartado 9: varias variables. Comprobaciones generales con un lagrangiano y una
# transformación sin ninguna simetría especial: D desde la definición (determinante y
# jacobiana, exactos en epsilon), forma de cuatro términos, lema e identidad.
def apartado9(n, Ls, y, Z, var, f, tau_s, xi_s, etiqueta):
    m = len(var)
    eps = sp.Symbol("epsilon")
    reglas = {y[i]: f[i] for i in range(n)}
    reglas.update({Z[i, k]: f[i].diff(var[k]) for i in range(n) for k in range(m)})
    al = lambda e: e.subs(reglas, simultaneous=True)
    d = lambda e, k: sp.diff(e, var[k])
    L = al(Ls)
    Ly = [al(sp.diff(Ls, y[i])) for i in range(n)]
    Lx = [al(sp.diff(Ls, var[k])) for k in range(m)]
    u = [[al(sp.diff(Ls, Z[i, k])) for k in range(m)] for i in range(n)]
    tau = [al(e) for e in tau_s]
    xi = [al(e) for e in xi_s]

    Xt = [var[k] + eps * tau[k] for k in range(m)]
    Yt = [f[i] + eps * xi[i] for i in range(n)]
    JX = sp.Matrix(m, m, lambda k, l: d(Xt[k], l))
    JY = sp.Matrix(n, m, lambda i, l: d(Yt[i], l))
    Jf = JY * JX.inv()
    sust = {y[i]: Yt[i] for i in range(n)}
    sust.update({var[k]: Xt[k] for k in range(m)})
    sust.update({Z[i, k]: Jf[i, k] for i in range(n) for k in range(m)})
    D = sp.diff(Ls.subs(sust, simultaneous=True) * JX.det(), eps).subs(eps, 0)

    D4 = (sum(Ly[i] * xi[i] for i in range(n))
          + sum(u[i][l] * (d(xi[i], l) - sum(d(f[i], k) * d(tau[k], l) for k in range(m)))
                for i in range(n) for l in range(m))
          + sum(Lx[k] * tau[k] for k in range(m)) + L * sum(d(tau[k], k) for k in range(m)))
    ok(D - D4, f"apartado 9 ({etiqueta}): D desde la definición = forma de cuatro términos")
    orden = max(sum(c for _, c in der.variable_count) for der in sp.expand(D4).atoms(sp.Derivative))
    ok(orden - 1, f"apartado 9 ({etiqueta}): D no contiene derivadas segundas")
    xib = [xi[i] - sum(tau[k] * d(f[i], k) for k in range(m)) for i in range(n)]
    lema = (sum(Ly[i] * xib[i] + sum(u[i][k] * d(xib[i], k) for k in range(m)) for i in range(n))
            + sum(d(tau[k] * L, k) for k in range(m)))
    ok(D4 - lema, f"apartado 9 ({etiqueta}): forma de cuatro términos = lema")
    phi = [Ly[i] - sum(d(u[i][k], k) for k in range(m)) for i in range(n)]
    T = [[sum(u[i][k] * d(f[i], l) for i in range(n)) - (L if k == l else 0) for l in range(m)] for k in range(m)]
    Q = [sum(u[i][k] * xi[i] for i in range(n)) - sum(T[k][l] * tau[l] for l in range(m)) for k in range(m)]
    ok(sum(d(Q[k], k) for k in range(m)) - D + sum(phi[i] * xib[i] for i in range(n)),
       f"apartado 9 ({etiqueta}): identidad, div(Q + F) - D = -sum phi_i xi barra_i")


def apartado9_n1_m2():
    t, s = var = sp.symbols("t s", real=True)
    f = [sp.Function("f")(t, s)]
    y = sp.symbols("y1:2")
    Z = sp.Matrix(1, 2, sp.symbols("z11 z12"))
    g, W = sp.Function("g"), sp.Function("W")
    Ls = g(y[0]) * Z[0, 0]**2 + sp.sin(s) * Z[0, 0] * Z[0, 1] + t * Z[0, 1]**3 + W(y[0]) * s
    apartado9(1, Ls, y, Z, var, f, [t * y[0], s**2 + y[0]**2], [sp.sin(t) * y[0] + s], "n = 1, m = 2")


def apartado9_n2_m2():
    x1, x2 = var = sp.symbols("x1 x2", real=True)
    f = [sp.Function("f1")(x1, x2), sp.Function("f2")(x1, x2)]
    y = sp.symbols("y1:3")
    Z = sp.Matrix(2, 2, sp.symbols("z11 z12 z21 z22"))
    g = sp.Function("g")
    Ls = (g(y[0]) * Z[0, 0]**2 + sp.sin(x2) * Z[0, 1] * Z[1, 0] + x1 * Z[1, 1]**3
          + y[1] * Z[0, 1] * x2 + y[0]**2 * y[1])
    apartado9(2, Ls, y, Z, var, f, [x1 * y[0] + y[1], x2**2 + y[0] * y[1]],
              [sp.sin(x1) * y[1] + x2, y[0]**2 + x1 * x2], "n = m = 2")

    # Un campo que depende de las derivadas y cuya divergencia es det J_f, un lagrangiano nulo
    div = sp.diff(f[0] * f[1].diff(x2), x1) + sp.diff(-f[0] * f[1].diff(x1), x2)
    detJ = f[0].diff(x1) * f[1].diff(x2) - f[0].diff(x2) * f[1].diff(x1)
    ok(div - detJ, "apartado 9: div(f1 d2 f2, -f1 d1 f2) = det J_f")
    Ldet = Z[0, 0] * Z[1, 1] - Z[0, 1] * Z[1, 0]
    reglas = {Z[i, k]: f[i].diff(var[k]) for i in range(2) for k in range(2)}
    for i in range(2):
        phi = -sum(sp.diff(sp.diff(Ldet, Z[i, k]).subs(reglas, simultaneous=True), var[k]) for k in range(2))
        ok(phi, f"apartado 9: det J_f es un lagrangiano nulo (expresión de Euler-Lagrange {i + 1})")


# Apartado 9.8: la cuerda vibrante, tensor de energía-momento y las tres traslaciones
def cuerda():
    t, x, c = sp.symbols("t x c", real=True)
    f = sp.Function("f")(t, x)
    ft, fx = f.diff(t), f.diff(x)
    L = ft**2 / 2 - c**2 * fx**2 / 2
    E = ft**2 / 2 + c**2 * fx**2 / 2
    u = [ft, -c**2 * fx]
    df = [ft, fx]
    T = [[u[mu] * df[nu] - (L if mu == nu else 0) for nu in range(2)] for mu in range(2)]
    ok(T[0][0] - E, "cuerda: T_00 = E")
    ok(T[0][1] - ft * fx, "cuerda: T_01 = f_t f_x")
    ok(T[1][0] + c**2 * fx * ft, "cuerda: T_10 = -c^2 f_x f_t")
    ok(T[1][1] + E, "cuerda: T_11 = -E")
    phi = -sp.diff(u[0], t) - sp.diff(u[1], x)
    ok(phi - (c**2 * f.diff(x, 2) - f.diff(t, 2)), "cuerda: phi = c^2 f_xx - f_tt")
    tabla = [
        ("traslación en t", (1, 0), 0, (-E, c**2 * fx * ft)),
        ("traslación en x", (0, 1), 0, (-ft * fx, E)),
        ("desplazamiento vertical", (0, 0), 1, (ft, -c**2 * fx)),
    ]
    for nombre, tau, xi, (Q0, Q1) in tabla:
        Q = [u[mu] * xi - sum(T[mu][nu] * tau[nu] for nu in range(2)) for mu in range(2)]
        ok(Q[0] - Q0, f"cuerda, {nombre}: Q_0 de la tabla")
        ok(Q[1] - Q1, f"cuerda, {nombre}: Q_1 de la tabla")
        xib = xi - sum(tau[nu] * df[nu] for nu in range(2))
        ok(sp.diff(Q[0], t) + sp.diff(Q[1], x) + phi * xib, f"cuerda, {nombre}: div Q = -phi xi barra")


# Apartado 10: flujos, prolongación, derivada de Lie, invariancia finita y simetrías generalizadas
def apartado10():
    eps, eta, s = sp.symbols("epsilon eta s", real=True)
    X0, Y0, P = sp.symbols("x y yp", real=True)   # punto (x, y) y pendiente y'
    Y2 = sp.Symbol("ypp", real=True)               # y''

    def dx(G):
        # derivada total respecto de x de una función de (x, y, y')
        return sp.diff(G, X0) + P * sp.diff(G, Y0) + Y2 * sp.diff(G, P)

    # 10.1: los flujos del giro y del cambio de velocidad resuelven la ecuación del campo
    Xg = X0 * sp.cos(eps) - Y0 * sp.sin(eps)
    Yg = X0 * sp.sin(eps) + Y0 * sp.cos(eps)
    ok(sp.diff(Xg, eps) + Yg, "10.1: giro, dX/de = -Y")
    ok(sp.diff(Yg, eps) - Xg, "10.1: giro, dY/de = X")
    ok(sp.diff(X0 + 0 * eps, eps), "10.1: cambio de velocidad, dX/de = 0")
    ok(sp.diff(Y0 + eps * X0, eps) - X0, "10.1: cambio de velocidad, dY/de = X")

    # 10.3: prolongación del giro; su generador y la ley de grupo para la pendiente
    Y1 = sp.simplify(dx(Yg) / dx(Xg))
    ok(Y1 - (sp.sin(eps) + P * sp.cos(eps)) / (sp.cos(eps) - P * sp.sin(eps)), "10.3: pendiente girada")
    xi1 = sp.diff(Y1, eps).subs(eps, 0)
    tau, xi = -Y0, X0
    ok(xi1 - (dx(xi) - P * dx(tau)), "10.3: xi^(1) = d_x xi - y' d_x tau (giro)")
    ok(xi1 - (1 + P**2), "10.3: xi^(1) = 1 + y'^2 (giro)")
    comp = Y1.subs(eps, eta).subs(P, Y1)   # primero el giro eps, después el giro eta
    ok(sp.simplify(sp.expand_trig(comp - Y1.subs(eps, eps + eta))), "10.3: ley de grupo de la pendiente prolongada")

    # 10.4: derivada de Lie de L dx = forma de cuatro términos = parte evolutiva + derivada total
    g, h = sp.Function("g"), sp.Function("h")
    Ls = lambda y, p, x: g(y) * p**2 + sp.sin(x) * p * y + x**2 * h(y) + x * p**3
    tau_g = X0 * Y0 + sp.sin(Y0)          # un generador cualquiera
    xi_g = X0**2 + sp.exp(Y0)
    Xe, Ye = X0 + eps * tau_g, Y0 + eps * xi_g
    Pe = dx(Ye) / dx(Xe)
    lie = sp.diff(Ls(Ye, Pe, Xe) * dx(Xe), eps).subs(eps, 0)
    L0 = Ls(Y0, P, X0)
    xi1_g = dx(xi_g) - P * dx(tau_g)
    cuatro = sp.diff(L0, Y0) * xi_g + sp.diff(L0, P) * xi1_g + sp.diff(L0, X0) * tau_g + L0 * dx(tau_g)
    ok(lie - cuatro, "10.4: derivada de Lie de L dx = forma de cuatro términos")
    xib = xi_g - P * tau_g
    evolutiva = sp.diff(L0, Y0) * xib + sp.diff(L0, P) * dx(xib)
    ok(cuatro - (evolutiva + dx(tau_g * L0)), "10.4: D = parte evolutiva + d_x(tau L)")
    G = sp.Function("G")(X0, Y0, P)
    lieG = tau_g * sp.diff(G, X0) + xi_g * sp.diff(G, Y0) + xi1_g * sp.diff(G, P)
    ok(lieG - (xib * sp.diff(G, Y0) + dx(xib) * sp.diff(G, P) + tau_g * dx(G)), "10.4: V^(1) = parte evolutiva + tau d_x")

    # 10.5: invariancia finita de la longitud bajo el giro, para todo epsilon
    longitud = sp.sqrt(1 + Y1**2) * dx(Xg)
    ok(sp.simplify(longitud**2 - (1 + P**2)), "10.5: giro, sqrt(1 + y'^2) dx es invariante (al cuadrado)")
    # Sin ley de grupo no basta el primer orden: (x, y + eps + eps^2 y) con L = y'^2 / 2
    Yn = Y0 + eps + eps**2 * Y0
    Pn = dx(Yn)
    ok(sp.diff(Pn**2 / 2, eps).subs(eps, 0), "10.5: sin ley de grupo, D = 0")
    ok(sp.simplify(Pn**2 / 2 - P**2 / 2 - ((1 + eps**2)**2 - 1) * P**2 / 2), "10.5: sin ley de grupo, cambio de orden eps^2")
    # Cambio de velocidad con L = y'^2 / 2 y F = y: fórmula exacta
    c, d = sp.symbols("c d", real=True)
    f = sp.Function("f")
    exacta = sp.integrate((f(d) + s * d) - (f(c) + s * c), (s, 0, eps))
    # directamente: int_c^d ((f' + eps)^2 - f'^2) / 2 dx = eps (f(d) - f(c)) + eps^2 (d - c) / 2
    ok(exacta - (eps * (f(d) - f(c)) + eps**2 * (d - c) / 2), "10.5: cambio de velocidad, fórmula exacta con F = y")

    # 10.6: xi barra = y' genera la traslación por la ecuación de transporte
    xv = sp.Symbol("xv", real=True)
    u = f(xv + eps)
    ok(sp.diff(u, eps) - sp.diff(u, xv), "10.6: u = f(x + eps) cumple du/deps = du/dx")
    # Las dos formas dan la misma Q: p xi barra - F barra = p xi - tau H - F
    pp, Fp, Lp, tp, xp = sp.symbols("p F L tau xi")
    ok(pp * (xp - tp * P) - (Fp - tp * Lp) - (pp * xp - tp * (pp * P - Lp) - Fp), "10.6: Q barra = Q")


# Apartado 10.6: el vector de Laplace–Runge–Lenz como simetría generalizada (problema de Kepler)
def apartado10_lrl():
    t = sp.Symbol("t", real=True)
    m, k = sp.symbols("m k", positive=True)
    q = [sp.Function(n)(t) for n in ("q1", "q2", "q3")]
    v = [c.diff(t) for c in q]
    r = sp.sqrt(sum(c**2 for c in q))
    L = m * sum(w**2 for w in v) / 2 + k / r
    p = [sp.diff(L, w) for w in v]
    ell = [q[1] * p[2] - q[2] * p[1], q[2] * p[0] - q[0] * p[2], q[0] * p[1] - q[1] * p[0]]
    pxl = [p[1] * ell[2] - p[2] * ell[1], p[2] * ell[0] - p[0] * ell[2], p[0] * ell[1] - p[1] * ell[0]]
    A = [pxl[i] - m * k * q[i] / r for i in range(3)]
    rv = sum(q[i] * v[i] for i in range(3))
    j = 0   # componente x del vector
    xi = [m * (2 * v[i] * q[j] - q[i] * v[j] - (1 if i == j else 0) * rv) for i in range(3)]
    dL = sum(sp.diff(L, q[i]) * xi[i] + p[i] * sp.diff(xi[i], t) for i in range(3))
    Fb = sum(p[i] * xi[i] for i in range(3)) - A[j]
    ok(dL - sp.diff(Fb, t), "10.6: LRL, el generador es una simetría con F barra = p xi - A_x")
    ecs = [sp.diff(L, q[i]) - sp.diff(p[i], t) for i in range(3)]
    acc = sp.solve(ecs, [c.diff(t, 2) for c in q], dict=True)[0]
    ok(sp.diff(A[j], t).subs(acc), "10.6: LRL, A_x constante sobre las soluciones")


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


apartado6_casos()
apartado8_homogeneo()
apartado9_n1_m2()
apartado9_n2_m2()
cuerda()
apartado10()
apartado10_lrl()
particula()
