r"""Comprobaciones simbólicas de la serie «El teorema de Noether» (versión 2).
Parte matemática (apartados 6.7, 7, 8, 9 y 10), ejemplos matemáticos (apartados 2 y 4),
parte física (apartados 9 y 10) y ejemplos físicos (apartados 1 a 8).
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


# Ejemplos, apartado 2.5: lagrangiano homogéneo de grado 1 (principio de Fermat en el plano)
def apartado8_homogeneo():
    n = sp.Function("n")
    Lf = n(f1, f2) * sp.sqrt(f1.diff(x)**2 + f2.diff(x)**2)
    p1, p2 = sp.diff(Lf, f1.diff(x)), sp.diff(Lf, f2.diff(x))
    ok(p1 * f1.diff(x) + p2 * f2.diff(x) - Lf, "ejemplos 2.5: L homogénea de grado 1, H = 0")
    ok(f1.diff(x) * EL(Lf, f1) + f2.diff(x) * EL(Lf, f2), "ejemplos 2.5: L homogénea de grado 1, f1' phi1 + f2' phi2 = 0")


# Apartado 8: varias variables. Comprobaciones generales con un lagrangiano y una
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
    ok(D - D4, f"apartado 8 ({etiqueta}): D desde la definición = forma de cuatro términos")
    orden = max(sum(c for _, c in der.variable_count) for der in sp.expand(D4).atoms(sp.Derivative))
    ok(orden - 1, f"apartado 8 ({etiqueta}): D no contiene derivadas segundas")
    xib = [xi[i] - sum(tau[k] * d(f[i], k) for k in range(m)) for i in range(n)]
    lema = (sum(Ly[i] * xib[i] + sum(u[i][k] * d(xib[i], k) for k in range(m)) for i in range(n))
            + sum(d(tau[k] * L, k) for k in range(m)))
    ok(D4 - lema, f"apartado 8 ({etiqueta}): forma de cuatro términos = lema")
    phi = [Ly[i] - sum(d(u[i][k], k) for k in range(m)) for i in range(n)]
    T = [[sum(u[i][k] * d(f[i], l) for i in range(n)) - (L if k == l else 0) for l in range(m)] for k in range(m)]
    Q = [sum(u[i][k] * xi[i] for i in range(n)) - sum(T[k][l] * tau[l] for l in range(m)) for k in range(m)]
    ok(sum(d(Q[k], k) for k in range(m)) - D + sum(phi[i] * xib[i] for i in range(n)),
       f"apartado 8 ({etiqueta}): identidad, div(Q + F) - D = -sum phi_i xi barra_i")


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
    ok(div - detJ, "apartado 8: div(f1 d2 f2, -f1 d1 f2) = det J_f")
    Ldet = Z[0, 0] * Z[1, 1] - Z[0, 1] * Z[1, 0]
    reglas = {Z[i, k]: f[i].diff(var[k]) for i in range(2) for k in range(2)}
    for i in range(2):
        phi = -sum(sp.diff(sp.diff(Ldet, Z[i, k]).subs(reglas, simultaneous=True), var[k]) for k in range(2))
        ok(phi, f"apartado 8: det J_f es un lagrangiano nulo (expresión de Euler-Lagrange {i + 1})")


# Apartado 8.8: la cuerda vibrante, tensor de energía-momento y las tres traslaciones
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


# Apartado 9: flujos, prolongación, derivada de Lie, invariancia finita y simetrías generalizadas
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
    ok(sp.diff(Xg, eps) + Yg, "9.1: giro, dX/de = -Y")
    ok(sp.diff(Yg, eps) - Xg, "9.1: giro, dY/de = X")
    ok(sp.diff(X0 + 0 * eps, eps), "9.1: cambio de velocidad, dX/de = 0")
    ok(sp.diff(Y0 + eps * X0, eps) - X0, "9.1: cambio de velocidad, dY/de = X")

    # 10.3: prolongación del giro; su generador y la ley de grupo para la pendiente
    Y1 = sp.simplify(dx(Yg) / dx(Xg))
    ok(Y1 - (sp.sin(eps) + P * sp.cos(eps)) / (sp.cos(eps) - P * sp.sin(eps)), "9.3: pendiente girada")
    xi1 = sp.diff(Y1, eps).subs(eps, 0)
    tau, xi = -Y0, X0
    ok(xi1 - (dx(xi) - P * dx(tau)), "9.3: xi^(1) = d_x xi - y' d_x tau (giro)")
    ok(xi1 - (1 + P**2), "9.3: xi^(1) = 1 + y'^2 (giro)")
    comp = Y1.subs(eps, eta).subs(P, Y1)   # primero el giro eps, después el giro eta
    ok(sp.simplify(sp.expand_trig(comp - Y1.subs(eps, eps + eta))), "9.3: ley de grupo de la pendiente prolongada")

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
    ok(lie - cuatro, "9.4: derivada de Lie de L dx = forma de cuatro términos")
    xib = xi_g - P * tau_g
    evolutiva = sp.diff(L0, Y0) * xib + sp.diff(L0, P) * dx(xib)
    ok(cuatro - (evolutiva + dx(tau_g * L0)), "9.4: D = parte evolutiva + d_x(tau L)")
    G = sp.Function("G")(X0, Y0, P)
    lieG = tau_g * sp.diff(G, X0) + xi_g * sp.diff(G, Y0) + xi1_g * sp.diff(G, P)
    ok(lieG - (xib * sp.diff(G, Y0) + dx(xib) * sp.diff(G, P) + tau_g * dx(G)), "9.4: V^(1) = parte evolutiva + tau d_x")

    # 10.5: invariancia finita de la longitud bajo el giro, para todo epsilon
    longitud = sp.sqrt(1 + Y1**2) * dx(Xg)
    ok(sp.simplify(longitud**2 - (1 + P**2)), "9.5: giro, sqrt(1 + y'^2) dx es invariante (al cuadrado)")
    # Sin ley de grupo no basta el primer orden: (x, y + eps + eps^2 y) con L = y'^2 / 2
    Yn = Y0 + eps + eps**2 * Y0
    Pn = dx(Yn)
    ok(sp.diff(Pn**2 / 2, eps).subs(eps, 0), "9.5: sin ley de grupo, D = 0")
    ok(sp.simplify(Pn**2 / 2 - P**2 / 2 - ((1 + eps**2)**2 - 1) * P**2 / 2), "9.5: sin ley de grupo, cambio de orden eps^2")
    # Cambio de velocidad con L = y'^2 / 2 y F = y: fórmula exacta
    c, d = sp.symbols("c d", real=True)
    f = sp.Function("f")
    exacta = sp.integrate((f(d) + s * d) - (f(c) + s * c), (s, 0, eps))
    # directamente: int_c^d ((f' + eps)^2 - f'^2) / 2 dx = eps (f(d) - f(c)) + eps^2 (d - c) / 2
    ok(exacta - (eps * (f(d) - f(c)) + eps**2 * (d - c) / 2), "9.5: cambio de velocidad, fórmula exacta con F = y")

    # 10.6: xi barra = y' genera la traslación por la ecuación de transporte
    xv = sp.Symbol("xv", real=True)
    u = f(xv + eps)
    ok(sp.diff(u, eps) - sp.diff(u, xv), "9.6: u = f(x + eps) cumple du/deps = du/dx")
    # Las dos formas dan la misma Q: p xi barra - F barra = p xi - tau H - F
    pp, Fp, Lp, tp, xp = sp.symbols("p F L tau xi")
    ok(pp * (xp - tp * P) - (Fp - tp * Lp) - (pp * xp - tp * (pp * P - Lp) - Fp), "9.6: Q barra = Q")


# Apartado 9.6: el vector de Laplace–Runge–Lenz como simetría generalizada (problema de Kepler)
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
    ok(dL - sp.diff(Fb, t), "9.6: LRL, el generador es una simetría con F barra = p xi - A_x")
    ecs = [sp.diff(L, q[i]) - sp.diff(p[i], t) for i in range(3)]
    acc = sp.solve(ecs, [c.diff(t, 2) for c in q], dict=True)[0]
    ok(sp.diff(A[j], t).subs(acc), "9.6: LRL, A_x constante sobre las soluciones")


# Apartado 10.3: la ecuación de Schrödinger en C^2 como lagrangiano con cuatro funciones reales
def apartado11_schrodinger():
    t = sp.Symbol("t", real=True)
    hb = sp.Symbol("hbar", positive=True)
    h11, h22, hr, hi = sp.symbols("h11 h22 hr hi", real=True)
    I = sp.I
    Hm = sp.Matrix([[h11, hr + I * hi], [hr - I * hi, h22]])          # matriz hermítica
    # Primero con símbolos reales (posiciones y velocidades), para que re e im se simplifiquen
    Y = sp.symbols("q1 r1 q2 r2", real=True)
    V = sp.symbols("vq1 vr1 vq2 vr2", real=True)
    psi = sp.Matrix([Y[0] + I * Y[1], Y[2] + I * Y[3]])
    dpsi = sp.Matrix([V[0] + I * V[1], V[2] + I * V[3]])
    prod = lambda u, v: sp.expand((u.H * v)[0, 0])                      # <u, v>, antilineal en u
    Ls = sp.re(prod(psi, I * hb * dpsi)) - sp.re(prod(psi, Hm * psi))
    # Después, a lo largo de cuatro funciones reales de t
    fun = [sp.Function(n)(t) for n in ("Fq1", "Fr1", "Fq2", "Fr2")]
    reglas = {**{Y[a]: fun[a] for a in range(4)}, **{V[a]: fun[a].diff(t) for a in range(4)}}
    al = lambda e: sp.expand(e).subs(reglas, simultaneous=True)
    L = al(Ls)
    p = [al(sp.diff(Ls, v)) for v in V]
    phi = [al(sp.diff(Ls, y)) - sp.diff(pc, t) for y, pc in zip(Y, p)]
    S = I * hb * dpsi - Hm * psi                                         # residuo de Schrödinger
    for j in range(2):
        Sj = sp.expand(S[j])
        ok(phi[2 * j] - al(2 * sp.re(Sj)),
           f"10.3: phi_q{j + 1} = 2 Re S_{j + 1}")
        ok(phi[2 * j + 1] - al(2 * sp.im(Sj)), f"10.3: phi_r{j + 1} = 2 Im S_{j + 1}")

    def reales(v):   # componentes reales (q1, r1, q2, r2) de un vector de C^2, ya a lo largo de las funciones
        v = [sp.expand(c) for c in v]
        return [al(sp.re(v[0])), al(sp.im(v[0])), al(sp.re(v[1])), al(sp.im(v[1]))]

    norma2 = sum(c**2 for c in fun)
    # Fase: xi = i psi, Q = -hbar |psi|^2
    xi = reales(I * psi)
    Q = sum(a * b for a, b in zip(p, xi))
    ok(Q + hb * norma2, "10.3: fase, Q = -hbar |psi|^2")
    ok(sp.diff(Q, t) + sum(a * b for a, b in zip(phi, xi)), "10.3: fase, identidad de Noether")
    # A = H^2 conmuta con H: xi = -i A psi, Q = hbar <psi, A psi>
    A = Hm * Hm
    xi = reales(-I * A * psi)
    Q = sum(a * b for a, b in zip(p, xi))
    ok(Q - hb * al(sp.re(prod(psi, A * psi))), "10.3: A = H^2, Q = hbar <psi, A psi>")
    ok(sp.diff(Q, t) + sum(a * b for a, b in zip(phi, xi)), "10.3: A = H^2, identidad de Noether")
    # Traslación en el tiempo: la función H es <psi, H psi>, y H' = -sum phi u'
    du = [c.diff(t) for c in fun]
    Hf = sum(a * b for a, b in zip(p, du)) - L
    ok(Hf - al(sp.re(prod(psi, Hm * psi))), "10.3: la función H es <psi, H psi>")
    ok(sp.diff(Hf, t) + sum(a * b for a, b in zip(phi, du)), "10.3: traslación en el tiempo, identidad")
    # L es lineal en las velocidades: la matriz W es nula
    ok(sum(sp.diff(Ls, a, b)**2 for a in V for b in V), "10.3: W = 0 (L lineal en las velocidades)")


# Ejemplos matemáticos (versión 2): camino paramétrico y ecuación de Laplace
def ejemplos_v2():
    # 2.2: giro del camino paramétrico; D = 0 y Q constante sobre una recta
    g1, g2 = sp.Function("g1")(x), sp.Function("g2")(x)
    Lp = sp.sqrt(g1.diff(x)**2 + g2.diff(x)**2)
    p1, p2 = sp.diff(Lp, g1.diff(x)), sp.diff(Lp, g2.diff(x))
    D = p1 * (-g2.diff(x)) + p2 * g1.diff(x)
    ok(D, "ejemplos 2.2: giro del camino paramétrico, D = 0")
    A1, A2, w1, w2, s = sp.symbols("A1 A2 w1 w2 s", real=True)
    Q = (A1 + s * w1) * w2 - (A2 + s * w2) * w1
    ok(sp.diff(Q, s), "ejemplos 2.2: Q_giro no depende de s sobre la recta")
    # 4: Laplace con dos variables, corrientes de la altura, de la traslación en x1 y del giro
    x1, x2 = var = sp.symbols("x1 x2", real=True)
    f = sp.Function("f")(x1, x2)
    d1, d2 = f.diff(x1), f.diff(x2)
    L = (d1**2 + d2**2) / 2
    u = [d1, d2]
    df = [d1, d2]
    phi = -(f.diff(x1, 2) + f.diff(x2, 2))
    T = [[u[k] * df[l] - (L if k == l else 0) for l in range(2)] for k in range(2)]
    ok(T[0][0] - (d1**2 - d2**2) / 2, "ejemplos 4: T_11")
    ok(T[0][1] - d1 * d2, "ejemplos 4: T_12")
    div = lambda Qv: sp.diff(Qv[0], x1) + sp.diff(Qv[1], x2)
    ok(div(u) + phi * 1, "ejemplos 4.1: altura, div Q = -phi xi barra")
    Qt = [-T[k][0] for k in range(2)]
    ok(div(Qt) + phi * (-d1), "ejemplos 4.2: traslación en x1, div Q = -phi xi barra")
    tau = [-x2, x1]
    Qg = [-sum(T[k][l] * tau[l] for l in range(2)) for k in range(2)]
    xib = -sum(tau[k] * df[k] for k in range(2))
    ok(div(Qg) + phi * xib, "ejemplos 4.3: giro, div Q = -phi xi barra")
    ok(Qg[0] - (x2 * T[0][0] - x1 * T[0][1]), "ejemplos 4.3: Q_1 = x2 T_11 - x1 T_12")


# Ejemplos físicos (versión 2), apartados 3 y 4: campo central en esféricas y en cartesianas
# (convenio activo) y dos partículas
def particula():
    t, m = sp.symbols("t m", positive=True)
    V = sp.Function("V")
    r, th, ph = [sp.Function(n)(t) for n in ("r", "theta", "phi")]
    xs, ys, zs = r * sp.sin(th) * sp.cos(ph), r * sp.sin(th) * sp.sin(ph), r * sp.cos(th)
    vel = [sp.diff(c, t) for c in (xs, ys, zs)]
    L = sp.simplify(m * sum(v**2 for v in vel) / 2 - V(r))
    ok(L - (m * (r.diff(t)**2 + r**2 * th.diff(t)**2 + r**2 * sp.sin(th)**2 * ph.diff(t)**2) / 2 - V(r)), "ejemplos físicos 3, esféricas: L")
    q = [r, th, ph]
    p = [sp.diff(L, c.diff(t)) for c in q]
    ecs = [sp.diff(L, c) - sp.diff(pi, t) for c, pi in zip(q, p)]
    acc = sp.solve(ecs, [c.diff(t, 2) for c in q], dict=True)[0]
    l = [m * (ys * vel[2] - zs * vel[1]), m * (zs * vel[0] - xs * vel[2]), m * (xs * vel[1] - ys * vel[0])]
    gens = [(0, -sp.sin(ph), -sp.cot(th) * sp.cos(ph)), (0, sp.cos(ph), -sp.cot(th) * sp.sin(ph)), (0, 0, 1)]
    for eje, gen, lk in zip("xyz", gens, l):
        Q = sum(pi * gi for pi, gi in zip(p, gen))
        ok(Q - lk, f"ejemplos físicos 3, esféricas: giro alrededor de {eje}, Q = l_{eje}")
        ok(sp.diff(Q, t).subs(acc), f"ejemplos físicos 3, esféricas: l_{eje} constante sobre las soluciones")
    ok(l[0] + m * r**2 * (sp.sin(ph) * th.diff(t) + sp.sin(th) * sp.cos(th) * sp.cos(ph) * ph.diff(t)), "ejemplos físicos 3, esféricas: expresión de l_x")
    ok(l[1] - m * r**2 * (sp.cos(ph) * th.diff(t) - sp.sin(th) * sp.cos(th) * sp.sin(ph) * ph.diff(t)), "ejemplos físicos 3, esféricas: expresión de l_y")
    ok(sum(lk**2 for lk in l) - (p[1]**2 + p[2]**2 / sp.sin(th)**2), "ejemplos físicos 3, esféricas: |l|^2 = p_theta^2 + p_phi^2 / sin^2(theta)")
    H = sum(pi * c.diff(t) for pi, c in zip(p, q)) - L
    ok(H - (m * (r.diff(t)**2 + r**2 * th.diff(t)**2 + r**2 * sp.sin(th)**2 * ph.diff(t)**2) / 2 + V(r)), "ejemplos físicos 3, esféricas: H = energía")
    ok(sp.diff(H, t).subs(acc), "ejemplos físicos 3, esféricas: energía constante sobre las soluciones")

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
    ok(D + Vp * dot(e, R) / rho, "ejemplos físicos 3: traslación, D = -V'(r) (e . r) / r")
    xi = [ui * t for ui in u]
    D = dot([sp.diff(Lc, c) for c in R], xi) + dot(pc, [sp.diff(c, t) for c in xi])
    ok(D - (m * dot(u, [c.diff(t) for c in R]) - t * Vp * dot(u, R) / rho), "ejemplos físicos 3: cambio de velocidad, D = m u . v - t V'(r) (u . r) / r")
    # Partícula libre: F = m u . r y Q = -u . (m r - p t)
    L0 = m * sum(c.diff(t)**2 for c in R) / 2
    p0 = [sp.diff(L0, c.diff(t)) for c in R]
    D0 = dot(p0, [sp.diff(c, t) for c in xi])
    F0 = m * dot(u, R)
    ok(D0 - sp.diff(F0, t), "ejemplos físicos 1: D = dF/dt con F = m u . r")
    Q0 = dot(p0, xi) - F0
    ok(Q0 + dot(u, [m * c - pi * t for c, pi in zip(R, p0)]), "ejemplos físicos 1: Q = -u . (m r - p t)")
    ok(sp.diff(Q0, t).subs({c.diff(t, 2): 0 for c in R}), "ejemplos físicos 1: Q constante sobre las soluciones")

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
    F2 = dot(u, [m1 * a + m2 * b for a, b in zip(R1, R2)])
    ok(D2 - sp.diff(F2, t), "ejemplos físicos 4: D = dF/dt con F = u . (m1 r1 + m2 r2)")
    Q2 = dot(p2, xi2) - F2
    P = [p2[k] + p2[k + 3] for k in range(3)]
    ok(Q2 + dot(u, [m1 * a + m2 * b - Pk * t for a, b, Pk in zip(R1, R2, P)]), "ejemplos físicos 4: Q = -u . (M X - P t)")
    ecs2 = [sp.diff(L2, c) - sp.diff(pi, t) for c, pi in zip(todas, p2)]
    acc2 = sp.solve(ecs2, [c.diff(t, 2) for c in todas], dict=True)[0]
    ok(sp.diff(Q2, t).subs(acc2), "ejemplos físicos 4: Q constante sobre las soluciones")


# Parte física (versión 2): partícula relativista, cuerda de Lorentz y mecánica cuántica
def fisica_relativista():
    t = sp.Symbol("t", real=True)
    m, c = sp.symbols("m c", positive=True)
    q = [sp.Function(n)(t) for n in ("q1", "q2", "q3")]
    v = [w.diff(t) for w in q]
    v2 = sum(w**2 for w in v)
    L = -m * c**2 * sp.sqrt(1 - v2 / c**2)
    p = [sp.diff(L, w) for w in v]
    H = sp.simplify(sum(a * b for a, b in zip(p, v)) - L)
    gam = 1 / sp.sqrt(1 - v2 / c**2)
    ok(H - m * c**2 * gam, "física 9.2: H = gamma m c^2")
    ok(p[0] - gam * m * v[0], "física 9.2: p = gamma m v")
    # Cambio de velocidad de Lorentz, activo: tau = u.q / c^2, xi = u t
    u = sp.symbols("u1:4", real=True)
    tau = sum(a * b for a, b in zip(u, q)) / c**2
    xi = [a * t for a in u]
    # forma de cuatro términos con n funciones: sum dL/dq xi + sum p (xi' - tau' q') + dL/dt tau + L tau'
    D = sum(p[i] * (sp.diff(xi[i], t) - sp.diff(tau, t) * v[i]) for i in range(3)) + L * sp.diff(tau, t)
    ok(D, "física 9.3: el cambio de velocidad de Lorentz es una simetría con F = 0")
    Q = sum(p[i] * xi[i] for i in range(3)) - tau * H
    K = [H * q[i] / c**2 - p[i] * t for i in range(3)]
    ok(Q + sum(a * b for a, b in zip(u, K)), "física 9.3: Q = -u . K, K = E q / c^2 - p t")
    acc = {w.diff(t, 2): 0 for w in q}   # la partícula libre relativista: aceleración nula
    ok(sp.diff(K[0], t).subs(acc), "física 9.3: K constante sobre las soluciones")
    # Límite de Galileo: L = -m c^2 + m v^2 / 2 + O(1/c^2), K -> m q - p t, tau H -> m u . q
    eps = sp.Symbol("eps", positive=True)   # eps = 1 / c^2
    Le = sp.series(L.subs(c, 1 / sp.sqrt(eps)) * eps, eps, 0, 2).removeO() / eps
    ok(sp.expand(Le - (-m / eps + m * v2 / 2)), "física 9.4: L = -m c^2 + m v^2 / 2 + O(1/c^2)")
    tH = sp.series((tau * H).subs(c, 1 / sp.sqrt(eps)), eps, 0, 1).removeO()
    ok(sp.expand(tH - m * sum(a * b for a, b in zip(u, q))), "física 9.4: tau H -> m u . q")


def fisica_cuerda_lorentz():
    t, x, c = sp.symbols("t x c", real=True)
    f = sp.Function("f")(t, x)
    ft, fx = f.diff(t), f.diff(x)
    L = ft**2 / 2 - c**2 * fx**2 / 2
    u = [ft, -c**2 * fx]
    df = [ft, fx]
    var = (t, x)
    T = [[u[a] * df[b] - (L if a == b else 0) for b in range(2)] for a in range(2)]
    tau = [x / c**2, t]                   # cambio de velocidad activo: t -> t + eps x / c^2, x -> x + eps t
    d = lambda e, k: sp.diff(e, var[k])
    # forma de cuatro términos con m = 2 variables y una función, xi = 0
    D = sum(u[l] * (-sum(df[k] * d(tau[k], l) for k in range(2))) for l in range(2)) + L * sum(d(tau[k], k) for k in range(2))
    ok(D, "física ejemplos 6: la cuerda es invariante bajo el cambio de velocidad de Lorentz")
    Q = [-sum(T[a][b] * tau[b] for b in range(2)) for a in range(2)]
    phi = -d(u[0], 0) - d(u[1], 1)
    xib = -sum(tau[k] * df[k] for k in range(2))
    ok(d(Q[0], 0) + d(Q[1], 1) + phi * xib, "física ejemplos 6: corriente de Lorentz, div Q = -phi xi barra")
    E = ft**2 / 2 + c**2 * fx**2 / 2
    ok(Q[0] + (x * E / c**2 + t * ft * fx), "física ejemplos 6: Q_0 = -(x E / c^2 + t f_t f_x)")


def fisica_cuantica():
    x, y, t = sp.symbols("x y t", real=True)
    hb, m = sp.symbols("hbar m", positive=True)
    I = sp.I
    psi = sp.Function("psi")
    # Cambio de velocidad de Galileo de la partícula libre en una dimensión
    u = sp.Symbol("u", real=True)
    sch = lambda g: I * hb * sp.diff(g, t) + hb**2 / (2 * m) * sp.diff(g, x, 2)   # residuo con V = 0
    base = psi(x - u * t, t)
    nueva = sp.exp(I * m * u * x / hb - I * m * u**2 * t / (2 * hb)) * base
    # Si psi cumple la ecuación, la transformada también: el residuo de la nueva es la fase por el de psi en (x - u t)
    X = sp.Symbol("X", real=True)
    res_psi = (I * hb * sp.Derivative(psi(X, t), t) + hb**2 / (2 * m) * sp.Derivative(psi(X, t), X, 2))
    dif = sp.simplify(sp.expand(sch(nueva) / sp.exp(I * m * u * x / hb - I * m * u**2 * t / (2 * hb))))
    dif = dif.subs(x, X + u * t).doit()
    ok(sp.simplify(dif - res_psi.doit()), "física 10.5: el cambio de velocidad con la fase lleva soluciones en soluciones")
    # Operadores sobre una función de prueba g(x, y)
    g = sp.Function("g")(x, y)
    V = sp.Function("V")
    px = lambda h: -I * hb * sp.diff(h, x)
    py = lambda h: -I * hb * sp.diff(h, y)
    Hc = lambda h, W: -hb**2 / (2 * m) * (sp.diff(h, x, 2) + sp.diff(h, y, 2)) + W * h
    conm = lambda A, B, h: A(B(h)) - B(A(h))
    # [q, p] = i hbar
    ok(conm(lambda h: x * h, px, g) - I * hb * g, "física 10.1: [q_x, p_x] = i hbar")
    # Potencial central en el plano: L_z = x p_y - y p_x conmuta con H
    r = sp.sqrt(x**2 + y**2)
    Lz = lambda h: x * py(h) - y * px(h)
    ok(conm(lambda h: Hc(h, V(r)), Lz, g), "física 10.4: [H, L_z] = 0 con potencial central")
    # Con un potencial cualquiera, p_x no conmuta con H: [H, p_x] = i hbar dV/dx
    W = sp.Function("W")(x, y)
    ok(conm(lambda h: Hc(h, W), px, g) - I * hb * sp.diff(W, x) * g, "física 10.4: [H, p_x] = i hbar dV/dx")
    # Partícula libre: G = m x - p_x t cumple (i / hbar) [H, G] + dG/dt = 0
    G = lambda h: m * x * h - t * px(h)
    dGdt = lambda h: -px(h)
    ok(I / hb * conm(lambda h: Hc(h, 0), G, g) + dGdt(g), "física 10.5: G = m q - p t se conserva para la partícula libre")


def fisica_cuantica_campo():
    # La ecuación de Schrödinger como teoría de campos (parte matemática, apartado 8): psi = psiR + i psiI
    t, x1, x2, x3 = var = sp.symbols("t x1 x2 x3", real=True)
    hb, m = sp.symbols("hbar m", positive=True)
    V = sp.Function("V")(x1, x2, x3)
    R = sp.Function("psiR", real=True)(*var)
    J = sp.Function("psiI", real=True)(*var)
    f = [R, J]
    d = lambda e, k: sp.diff(e, var[k])
    L = hb * (J * d(R, 0) - R * d(J, 0)) - hb**2 / (2 * m) * sum(d(R, k)**2 + d(J, k)**2 for k in (1, 2, 3)) - V * (R**2 + J**2)
    # momentos u_{ik} y expresiones de Euler–Lagrange
    Z = [[sp.Symbol(f"Z{i}{k}") for k in range(4)] for i in range(2)]
    Y = [sp.Symbol("Y0"), sp.Symbol("Y1")]
    sub = {f[i].diff(var[k]): Z[i][k] for i in range(2) for k in range(4)}
    Ls = L.subs(sub).subs({R: Y[0], J: Y[1]})
    back = {Z[i][k]: f[i].diff(var[k]) for i in range(2) for k in range(4)}
    back.update({Y[0]: R, Y[1]: J})
    u = [[sp.diff(Ls, Z[i][k]).subs(back) for k in range(4)] for i in range(2)]
    phi = [sp.diff(Ls, Y[i]).subs(back) - sum(d(u[i][k], k) for k in range(4)) for i in range(2)]
    psi = R + sp.I * J
    lap = lambda h: sum(sp.diff(h, w, 2) for w in (x1, x2, x3))
    res = sp.I * hb * d(psi, 0) - (-hb**2 / (2 * m) * lap(psi) + V * psi)   # residuo de Schrödinger
    ok(phi[0] - 2 * (-hb * d(J, 0) + hb**2 / (2 * m) * lap(R) - V * R),
       "física 10.3: la expresión de Euler–Lagrange de psiR es el doble de la parte real del residuo")
    ok(phi[1] - 2 * (hb * d(R, 0) + hb**2 / (2 * m) * lap(J) - V * J),
       "física 10.3: la expresión de Euler–Lagrange de psiI es el doble de la parte imaginaria del residuo")
    # comprobación de que esas son las partes real e imaginaria de i hbar psi_t - H psi
    ok(sp.expand(res - ((-hb * d(J, 0) + hb**2 / (2 * m) * lap(R) - V * R) + sp.I * (hb * d(R, 0) + hb**2 / (2 * m) * lap(J) - V * J))),
       "física 10.3: partes real e imaginaria del residuo de Schrödinger")
    # simetría de fase: xi = (-psiI, psiR), tau = 0; corriente y ecuación de continuidad
    xi = [-J, R]
    Q = [sum(u[i][k] * xi[i] for i in range(2)) for k in range(4)]
    ok(Q[0] + hb * (R**2 + J**2), "física 10.3: fase, Q_0 = -hbar |psi|^2")
    for k in (1, 2, 3):
        ok(Q[k] + hb**2 / m * (R * d(J, k) - J * d(R, k)), f"física 10.3: fase, Q_{k} = -hbar j_{k}")
    ok(sum(d(Q[k], k) for k in range(4)) + sum(phi[i] * xi[i] for i in range(2)), "física 10.3: fase, div Q = -sum phi xi")
    # tensor de energía-momento: densidad de energía y de cantidad de movimiento
    df = [[d(f[i], k) for k in range(4)] for i in range(2)]
    T = lambda a, b: sum(u[i][a] * df[i][b] for i in range(2)) - (L if a == b else 0)
    ok(T(0, 0) - (hb**2 / (2 * m) * sum(d(R, k)**2 + d(J, k)**2 for k in (1, 2, 3)) + V * (R**2 + J**2)),
       "física 10.3: T_00 = hbar^2/(2m) |grad psi|^2 + V |psi|^2")
    ok(-T(0, 1) - hb * (R * d(J, 1) - J * d(R, 1)), "física 10.3: -T_01 = hbar (psiR d1 psiI - psiI d1 psiR)")
    r0, i0, r1, i1 = sp.symbols("r0 i0 r1 i1", real=True)   # valores y derivadas como símbolos reales
    expr = sp.re(sp.expand((r0 - sp.I * i0) * (-sp.I * hb * (r1 + sp.I * i1))))
    ok(sp.expand(expr - hb * (r0 * i1 - i0 * r1)), "física 10.3: -T_01 = Re(conj(psi) p_1 psi)")


def fisica_generador_temporal():
    # D para psi -> exp(-i eps A(t)) psi con L = Re<psi, i hbar psi'> - <psi, H psi>, en C^2.
    # Valores y derivadas como símbolos reales; la derivada temporal se hace con la regla de la cadena.
    hb = sp.Symbol("hbar", positive=True)
    a, b_, c_, w1, w2 = sp.symbols("a b c w1 w2", real=True)
    Hm = sp.Matrix([[a, w1 + sp.I * w2], [w1 - sp.I * w2, c_]])
    A = sp.symbols("A1:5", real=True)        # entradas reales de A(t)
    dA = sp.symbols("dA1:5", real=True)      # sus derivadas
    Am = sp.Matrix([[A[0], A[2] + sp.I * A[3]], [A[2] - sp.I * A[3], A[1]]])
    dAm = sp.Matrix([[dA[0], dA[2] + sp.I * dA[3]], [dA[2] - sp.I * dA[3], dA[1]]])
    y = sp.symbols("y1:5", real=True)        # partes real e imaginaria de psi
    z = sp.symbols("z1:5", real=True)        # sus derivadas
    psi = sp.Matrix([y[0] + sp.I * y[1], y[2] + sp.I * y[3]])
    dpsi = sp.Matrix([z[0] + sp.I * z[1], z[2] + sp.I * z[3]])
    br = lambda U, W: sp.expand((U.H * W)[0, 0])
    L = sp.re(br(psi, sp.I * hb * dpsi)) - sp.re(br(psi, Hm * psi))
    xc = sp.expand(-sp.I * Am * psi)
    xi = [sp.re(xc[0]), sp.im(xc[0]), sp.re(xc[1]), sp.im(xc[1])]
    dxi = [sum(sp.diff(e, y[j]) * z[j] for j in range(4)) + sum(sp.diff(e, A[k]) * dA[k] for k in range(4)) for e in xi]
    D = sum(sp.diff(L, y[i]) * xi[i] + sp.diff(L, z[i]) * dxi[i] for i in range(4))
    Op = dAm + sp.I / hb * (Hm * Am - Am * Hm)
    ok(sp.expand(D - sp.re(hb * br(psi, Op * psi))), "física 10.4: D = hbar <psi, (dA/dt + (i/hbar)[H, A]) psi>")
    ok(sp.expand(sp.im(br(psi, Op * psi))), "física 10.4: <psi, (dA/dt + (i/hbar)[H, A]) psi> es real")
    pg = sum(sp.diff(L, z[i]) * xi[i] for i in range(4))
    ok(sp.expand(pg - sp.re(hb * br(psi, Am * psi))), "física 10.4: p(xi) = hbar <psi, A psi>")


def fisica_klein_gordon():
    t, x = sp.symbols("t x", real=True)
    hb, m, c = sp.symbols("hbar m c", positive=True)
    psi = sp.Function("psi")(t, x)
    phi = sp.exp(-sp.I * m * c**2 * t / hb) * psi
    kg = sp.diff(phi, t, 2) / c**2 - sp.diff(phi, x, 2) + (m * c / hb)**2 * phi
    resto = sp.expand(sp.simplify(kg / sp.exp(-sp.I * m * c**2 * t / hb)))
    # resto = psi_tt / c^2 - (2 i m / hbar) psi_t - psi_xx: sin el primer término, es Schrödinger libre por -2m/hbar^2
    ok(resto - (sp.diff(psi, t, 2) / c**2 - 2 * sp.I * m / hb * sp.diff(psi, t) - sp.diff(psi, x, 2)),
       "física 10.6: Klein–Gordon con la fase de la energía en reposo")
    sch = sp.I * hb * sp.diff(psi, t) + hb**2 / (2 * m) * sp.diff(psi, x, 2)
    ok(resto - sp.diff(psi, t, 2) / c**2 + 2 * m / hb**2 * sch, "física 10.6: sin psi_tt / c^2 queda la ecuación de Schrödinger libre")


def fisica_relativista_extra():
    t = sp.Symbol("t", real=True)
    m, c = sp.symbols("m c", positive=True)
    q = [sp.Function(n)(t) for n in ("q1", "q2", "q3")]
    v = [w.diff(t) for w in q]
    v2 = sum(w**2 for w in v)
    L = -m * c**2 * sp.sqrt(1 - v2 / c**2)
    p = [sp.diff(L, w) for w in v]
    E = sp.simplify(sum(a * b for a, b in zip(p, v)) - L)
    ok(sp.simplify(E**2 - (sum(w**2 for w in p) * c**2 + m**2 * c**4)), "física 9.2: E^2 = |p|^2 c^2 + m^2 c^4")
    # giro alrededor de z: xi = (-q2, q1, 0), D = p . xi' = 0
    xi = [-q[1], q[0], 0]
    D = sum(p[i] * sp.diff(xi[i], t) for i in range(3))
    ok(D, "física 9.3: los giros son simetrías de la partícula relativista")
    # en el límite: la parte -m c^2 del lagrangiano aporta L tau' = -m u . q' con tau = u . q / c^2
    u = sp.symbols("u1:4", real=True)
    tau = sum(a * b for a, b in zip(u, q)) / c**2
    ok(-m * c**2 * sp.diff(tau, t) + m * sum(a * b for a, b in zip(u, v)), "física 9.4: -m c^2 tau' = -m u . q'")


def fisica_cuantica_3d():
    x1, x2, x3, t = sp.symbols("x1 x2 x3 t", real=True)
    X = (x1, x2, x3)
    hb, m = sp.symbols("hbar m", positive=True)
    I = sp.I
    g = sp.Function("g")(x1, x2, x3)
    p = [lambda h, k=k: -I * hb * sp.diff(h, X[k]) for k in range(3)]
    qo = [lambda h, k=k: X[k] * h for k in range(3)]
    lap = lambda h: sum(sp.diff(h, w, 2) for w in X)
    conm = lambda A, B, h: sp.expand(A(B(h)) - B(A(h)))
    l1 = lambda h: x2 * p[2](h) - x3 * p[1](h)
    l2 = lambda h: x3 * p[0](h) - x1 * p[2](h)
    l3 = lambda h: x1 * p[1](h) - x2 * p[0](h)
    ok(conm(l1, l2, g) - I * hb * l3(g), "física 10.4: [l1, l2] = i hbar l3")
    r = sp.sqrt(x1**2 + x2**2 + x3**2)
    U = sp.Function("U")
    H = lambda h: -hb**2 / (2 * m) * lap(h) + U(r) * h
    ok(conm(H, l3, g), "física 10.4: [H, l3] = 0 con potencial central en tres dimensiones")
    ok(conm(lambda h: -hb**2 / (2 * m) * lap(h), l3, g), "física 10.4: [laplaciano, l3] = 0")
    H0 = lambda h: -hb**2 / (2 * m) * lap(h)
    ok(conm(H0, qo[0], g) + I * hb / m * p[0](g), "física 10.5: [H0, q1] = -i hbar p1 / m")
    # campo uniforme: V = -kappa a . q con a = e1; A = p1 - kappa t cumple dA/dt + (i/hbar)[H, A] = 0
    kap = sp.Symbol("kappa", real=True)
    gt = sp.Function("g")(x1, x2, x3, t)
    Hu = lambda h: -hb**2 / (2 * m) * lap(h) - kap * x1 * h
    A = lambda h: -I * hb * sp.diff(h, x1) - kap * t * h
    dA = lambda h: -kap * h
    ok(dA(gt) + I / hb * conm(Hu, A, gt), "física 10.5: campo uniforme, A = a . p - kappa t se conserva")
    # cambio de velocidad con la fase, en tres dimensiones
    u = sp.symbols("u1:4", real=True)
    psi = sp.Function("psi")
    Y = sp.symbols("Y1:4", real=True)
    fase = sp.exp(I * m * sum(a * b for a, b in zip(u, X)) / hb - I * m * sum(a**2 for a in u) * t / (2 * hb))
    nueva = fase * psi(*[X[k] - u[k] * t for k in range(3)], t)
    sch = lambda h: I * hb * sp.diff(h, t) + hb**2 / (2 * m) * lap(h)
    dif = sp.expand(sp.simplify(sch(nueva) / fase))
    dif = dif.subs({X[k]: Y[k] + u[k] * t for k in range(3)}).doit()
    base = psi(*Y, t)
    res = I * hb * sp.diff(base, t) + hb**2 / (2 * m) * sum(sp.diff(base, w, 2) for w in Y)
    ok(sp.simplify(dif - res), "física 10.5: el cambio de velocidad con la fase lleva soluciones en soluciones (tres dimensiones)")
    # conmutación de cambio de velocidad y traslación: B T = exp(i m u . a / hbar) T B, con t fijo
    a = sp.symbols("a1:4", real=True)
    f0 = sp.Function("f0")
    T = lambda h: h.subs({X[k]: X[k] - a[k] for k in range(3)}, simultaneous=True)
    B = lambda h: sp.exp(I * m * sum(uu * xx for uu, xx in zip(u, X)) / hb) * h.subs({X[k]: X[k] - u[k] * t for k in range(3)}, simultaneous=True)
    h0 = f0(x1, x2, x3)
    ok(sp.simplify(B(T(h0)) - sp.exp(I * m * sum(uu * aa for uu, aa in zip(u, a)) / hb) * T(B(h0))), "física 10.5: B T = exp(i m u . a / hbar) T B")


def fisica_relativista_dos():
    # dos partículas libres relativistas: el cambio de velocidad como simetría generalizada (parte matemática, 9.6)
    t = sp.Symbol("t", real=True)
    m1, m2, c = sp.symbols("m1 m2 c", positive=True)
    u = sp.symbols("u1:4", real=True)
    qs = [[sp.Function(f"q{j}{k}")(t) for k in range(3)] for j in (1, 2)]
    ms = [m1, m2]
    Ls = [-ms[j] * c**2 * sp.sqrt(1 - sum(w.diff(t)**2 for w in qs[j]) / c**2) for j in range(2)]
    L = Ls[0] + Ls[1]
    ps = [[sp.diff(L, w.diff(t)) for w in qs[j]] for j in range(2)]
    taus = [sum(a * w for a, w in zip(u, qs[j])) / c**2 for j in range(2)]
    xib = [[u[k] * t - taus[j] * qs[j][k].diff(t) for k in range(3)] for j in range(2)]
    D = sum(sp.diff(L, qs[j][k]) * xib[j][k] + ps[j][k] * sp.diff(xib[j][k], t) for j in range(2) for k in range(3))
    Fb = -sum(taus[j] * Ls[j] for j in range(2))
    ok(sp.simplify(D - sp.diff(Fb, t)), "física 9.5: dos partículas, D = dF/dt con F = -sum tau_i L_i")
    E = [sp.simplify(sum(ps[j][k] * qs[j][k].diff(t) for k in range(3)) - Ls[j]) for j in range(2)]
    Qb = sum(ps[j][k] * xib[j][k] for j in range(2) for k in range(3)) - Fb
    G = [sum(E[j] * qs[j][k] for j in range(2)) / c**2 - sum(ps[j][k] for j in range(2)) * t for k in range(3)]
    ok(sp.simplify(Qb + sum(u[k] * G[k] for k in range(3))), "física 9.5: Q = -u . G_rel, G_rel = sum E_i q_i / c^2 - P t")


# Ejemplos físicos (versión 2): cuatro pasos y comprobación sobre la solución explícita
def fisica_ejemplos():
    t = sp.Symbol("t", real=True)
    m, g, c, kap, mu, T0, hb = sp.symbols("m g c kappa mu T0 hbar", positive=True)
    q = sp.Matrix([sp.Function(f"q{i}")(t) for i in (1, 2, 3)])
    qd = q.diff(t)
    u = sp.Matrix(sp.symbols("u1:4", real=True))
    q0 = sp.Matrix(sp.symbols("q01:4", real=True))
    v0 = sp.Matrix(sp.symbols("v01:4", real=True))
    e3 = sp.Matrix([0, 0, 1])

    Ys = sp.symbols("Y1:4", real=True)
    Zs = sp.symbols("Z1:4", real=True)

    def parcial_t(L):
        """Derivada parcial respecto del argumento t, con posiciones y velocidades fijas."""
        ida = {qd[i]: Zs[i] for i in range(3)}
        Ls = L.subs(ida).subs({q[i]: Ys[i] for i in range(3)})
        vuelta = {Ys[i]: q[i] for i in range(3)}
        vuelta.update({Zs[i]: qd[i] for i in range(3)})
        return sp.diff(Ls, t).subs(vuelta)

    def D4(L, tau, xi):
        """Forma de cuatro términos con n = 3 funciones."""
        p = [sp.diff(L, w) for w in qd]
        tdot = sp.diff(tau, t)
        return (sum(sp.diff(L, q[i]) * xi[i] + p[i] * (sp.diff(xi[i], t) - tdot * qd[i]) for i in range(3))
                + parcial_t(L) * tau + L * tdot)

    def mom(L):
        return sp.Matrix([sp.diff(L, w) for w in qd])

    def ham(L):
        return mom(L).dot(qd) - L

    # 1. Partícula libre
    L0 = m * qd.dot(qd) / 2
    p0 = mom(L0)
    sol0 = {q[i]: q0[i] + v0[i] * t for i in range(3)}
    G = m * q - p0 * t
    ok(D4(L0, 0, u * t) - sp.diff(m * u.dot(q), t), "ejemplos físicos 1: cambio de velocidad, F = m u . q")
    ok(D4(L0, 1, [0, 0, 0]), "ejemplos físicos 1: traslación en el tiempo, D = 0")
    ok((G.subs(sol0).doit() - m * q0).norm()**2, "ejemplos físicos 1: G = m q0 sobre la solución")
    ok(sp.diff(ham(L0).subs(sol0).doit(), t), "ejemplos físicos 1: H constante sobre la solución")

    # 2. Tiro parabólico: L = m |q'|^2 / 2 - m g q3
    L1 = L0 - m * g * q[2]
    p1 = mom(L1)
    sol1 = {q[i]: q0[i] + v0[i] * t - (g * t**2 / 2 if i == 2 else 0) for i in range(3)}
    ok(D4(L1, 0, e3) + m * g, "ejemplos físicos 2: traslación vertical, D = -m g")
    ok(sp.diff((p1[2] + m * g * t).subs(sol1).doit(), t), "ejemplos físicos 2: p3 + m g t constante")
    Dg1 = D4(L1, 0, sp.Matrix([1, 0, 0]).cross(q))
    ok(Dg1 + m * g * q[1], "ejemplos físicos 2: giro alrededor de q1, D = -m g q2")
    l1 = (q.cross(p1))[0]
    ok(sp.diff(l1.subs(sol1).doit(), t) + m * g * q[1].subs(sol1), "ejemplos físicos 2: dl1/dt = -m g q2")
    l3 = (q.cross(p1))[2]
    ok(sp.diff(l3.subs(sol1).doit(), t), "ejemplos físicos 2: l3 constante")
    Fb = m * u.dot(q) - m * g * u[2] * t**2 / 2
    ok(D4(L1, 0, u * t) - sp.diff(Fb, t), "ejemplos físicos 2: cambio de velocidad, F = m u . q - m g u3 t^2 / 2")
    Qb = (p1.dot(u * t) - Fb).subs(sol1).doit()
    ok(Qb + m * u.dot(q0), "ejemplos físicos 2: Q = -m u . q0 sobre la solución")
    ok(sp.diff(ham(L1).subs(sol1).doit(), t), "ejemplos físicos 2: energía constante")

    # 3. Campo central, convenio activo: traslación y cambio de velocidad
    V = sp.Function("V")
    r = sp.sqrt(q.dot(q))
    rr = sp.Symbol("rr", positive=True)
    Vp = sp.diff(V(rr), rr).subs(rr, r)
    L2 = L0 - V(r)
    a = sp.Matrix(sp.symbols("a1:4", real=True))
    ok(D4(L2, 0, a) + Vp * a.dot(q) / r, "ejemplos físicos 3: traslación, D = -V'(r) (a . q) / r")
    ok(D4(L2, 0, u * t) - (m * u.dot(qd) - t * Vp * u.dot(q) / r), "ejemplos físicos 3: cambio de velocidad, D = m u . q' - t V'(r) (u . q) / r")
    # coordenadas polares en el plano q3 = 0
    rp, th = sp.Function("r")(t), sp.Function("theta")(t)
    x1, x2 = rp * sp.cos(th), rp * sp.sin(th)
    ok(sp.simplify(m * (x1 * sp.diff(x2, t) - x2 * sp.diff(x1, t)) - m * rp**2 * sp.diff(th, t)), "ejemplos físicos 3: m (q1 q2' - q2 q1') = m r^2 theta'")
    ell = sp.Symbol("ell", positive=True)
    Ep = m * (sp.diff(x1, t)**2 + sp.diff(x2, t)**2) / 2 + V(rp)
    ok(sp.simplify(Ep.subs(sp.diff(th, t), ell / (m * rp**2)) - (m * sp.diff(rp, t)**2 / 2 + ell**2 / (2 * m * rp**2) + V(rp))),
       "ejemplos físicos 3: energía con l = m r^2 theta'")

    # 4. Dos partículas: descomposición de J y de E
    m1, m2 = sp.symbols("m1 m2", positive=True)
    M = m1 + m2
    X = sp.Matrix([sp.Function(f"X{i}")(t) for i in (1, 2, 3)])
    rv = sp.Matrix([sp.Function(f"r{i}")(t) for i in (1, 2, 3)])
    qa = X + m2 / M * rv
    qb = X - m1 / M * rv
    mb = m1 * m2 / M
    J = m1 * qa.cross(qa.diff(t)) + m2 * qb.cross(qb.diff(t))
    ok((J - (M * X.cross(X.diff(t)) + mb * rv.cross(rv.diff(t)))).applyfunc(sp.simplify).norm()**2, "ejemplos físicos 4: J = M X x X' + m_red r x r'")
    T = m1 * qa.diff(t).dot(qa.diff(t)) / 2 + m2 * qb.diff(t).dot(qb.diff(t)) / 2
    ok(sp.simplify(T - (M * X.diff(t).dot(X.diff(t)) / 2 + mb * rv.diff(t).dot(rv.diff(t)) / 2)), "ejemplos físicos 4: T = M |X'|^2 / 2 + m_red |r'|^2 / 2")

    # 5. Carga en un campo magnético uniforme (fase chi)
    e, B = sp.symbols("e B", positive=True)
    Bv = sp.Matrix([0, 0, B])
    L3 = L0 + e * qd.dot(Bv.cross(q) / 2)
    pc = mom(L3)
    c1, c2, c3, vp, vpar, chi = sp.symbols("c1 c2 c3 v_perp v_par chi", real=True)
    w = e * B / m
    ph = chi - w * t
    solh = {q[0]: c1 - vp / w * sp.sin(ph), q[1]: c2 + vp / w * sp.cos(ph), q[2]: c3 + vpar * t}
    eqs = (m * q.diff(t, 2) - e * qd.cross(Bv)).subs(solh).doit()
    ok(eqs.norm()**2, "ejemplos físicos 5: la hélice cumple las ecuaciones")
    K = m * qd - e * q.cross(Bv)
    ok((K.subs(solh).doit() - sp.Matrix([-e * B * c2, e * B * c1, m * vpar])).norm()**2, "ejemplos físicos 5: K = (-e B c2, e B c1, m v_par)")
    Qg = pc.dot(e3.cross(q))
    ok(Qg.subs(solh).doit() - e * B / 2 * (c1**2 + c2**2 - (vp / w)**2), "ejemplos físicos 5: Q_giro = e B (c1^2 + c2^2 - R^2) / 2")
    ok(D4(L3, 0, e3 * t) - sp.diff(m * q[2], t), "ejemplos físicos 5: cambio de velocidad paralelo a B, F = m q3")
    ok((pc.dot(e3 * t) - m * q[2]).subs(solh).doit() + m * c3, "ejemplos físicos 5: Q = -m c3 sobre la hélice")
    ok(sp.diff(ham(L3).subs(solh).doit(), t), "ejemplos físicos 5: H constante sobre la hélice")
    ok(D4(L3, 1, [0, 0, 0]), "ejemplos físicos 5: traslación en el tiempo, D = 0")

    # 6. Cuerda vibrante con densidad mu y tensión T0, c^2 = T0 / mu
    x = sp.Symbol("x", real=True)
    f = sp.Function("f")(t, x)
    ft, fx = f.diff(t), f.diff(x)
    Lc = mu * ft**2 / 2 - T0 * fx**2 / 2
    uu = [mu * ft, -T0 * fx]
    df = [ft, fx]
    var = (t, x)
    dd = lambda h, k: sp.diff(h, var[k])
    Tt = lambda i, k: uu[i] * df[k] - (Lc if i == k else 0)
    phi = -dd(uu[0], 0) - dd(uu[1], 1)
    Ed = mu * ft**2 / 2 + T0 * fx**2 / 2
    ok(Tt(0, 0) - Ed, "ejemplos físicos 6: T_00 = densidad de energía")
    ok(-Tt(1, 0) - T0 * fx * ft, "ejemplos físicos 6: Q_1 de la traslación en t = T0 f_x f_t")
    A, k, n, a1, b1 = sp.symbols("A k n a1 b1", positive=True)
    om = sp.sqrt(T0 / mu) * k
    fe = A * sp.sin(k * (x - a1)) * sp.cos(om * t)
    Ee = (mu * sp.diff(fe, t)**2 / 2 + T0 * sp.diff(fe, x)**2 / 2)
    Etot = sp.integrate(Ee, (x, a1, a1 + n * sp.pi / k))
    ok(sp.simplify(Etot.subs(n, 3) - A**2 * (3 * sp.pi / k) * T0 * k**2 / 4), "ejemplos físicos 6: energía de la onda estacionaria (n = 3)")
    Pt = sp.integrate(mu * sp.diff(fe, t), (x, a1, a1 + 3 * sp.pi / k))
    ok(sp.simplify(Pt + 2 * mu * A * om / k * sp.sin(om * t)), "ejemplos físicos 6: cantidad de movimiento transversal (n = 3)")
    cc = sp.sqrt(T0 / mu)
    tau = [x / cc**2, t]
    Dl = sum(uu[l] * (-sum(df[kk] * dd(tau[kk], l) for kk in range(2))) for l in range(2)) + Lc * sum(dd(tau[kk], kk) for kk in range(2))
    ok(Dl, "ejemplos físicos 6: cambio de velocidad de Lorentz, D = 0")
    Ql = [-sum(Tt(i, kk) * tau[kk] for kk in range(2)) for i in range(2)]
    xib = -sum(tau[kk] * df[kk] for kk in range(2))
    ok(dd(Ql[0], 0) + dd(Ql[1], 1) + phi * xib, "ejemplos físicos 6: Lorentz, d_t Q_0 + d_x Q_1 = -phi xi barra")
    ok(Ql[0] + (x * Ed / cc**2 + t * mu * ft * fx), "ejemplos físicos 6: Q_0 = -(x E / c^2 + t mu f_t f_x)")
    ok(Ql[1] - (mu * x * fx * ft + t * Ed), "ejemplos físicos 6: Q_1 = mu x f_x f_t + t E")
    tg = [0, t]
    Dg = sum(uu[l] * (-sum(df[kk] * dd(tg[kk], l) for kk in range(2))) for l in range(2)) + Lc * sum(dd(tg[kk], kk) for kk in range(2))
    ok(Dg + mu * ft * fx, "ejemplos físicos 6: cambio de velocidad de Galileo, D = -mu f_t f_x")
    gg = sp.Function("g")
    s = sp.Symbol("s", real=True)
    pulso = gg(x - cc * t)
    integ = (x * Ed / cc**2 + t * mu * ft * fx).subs(f, pulso).doit()
    ok(sp.simplify(integ - mu * (x - cc * t) * sp.Subs(sp.Derivative(gg(s), s), s, x - cc * t).doit()**2),
       "ejemplos físicos 6: pulso, densidad = mu (x - c t) g'(x - c t)^2")

    # 7. Partícula libre relativista y partícula relativista en un campo uniforme
    gam = 1 / sp.sqrt(1 - qd.dot(qd) / c**2)
    Lr = -m * c**2 / gam
    pr = mom(Lr)
    Er = sp.simplify(ham(Lr))
    Grel = Er * q / c**2 - pr * t
    sol7 = {q[i]: q0[i] + v0[i] * t for i in range(3)}
    ok((Grel.subs(sol7).doit() - (Er * q0 / c**2).subs(sol7).doit()).applyfunc(sp.simplify).norm()**2, "ejemplos físicos 7: G_rel = E q0 / c^2 sobre la solución")
    Lk = Lr + kap * q[0]
    pk = mom(Lk)
    Hk = sp.simplify(ham(Lk))
    ok(sp.simplify(Hk - (m * c**2 * gam - kap * q[0])), "ejemplos físicos 7: H = gamma m c^2 - kappa q1")
    ok(D4(Lk, 0, sp.Matrix([1, 0, 0])) - kap, "ejemplos físicos 7: traslación en q1, D = kappa")
    uu1 = sp.Symbol("u", real=True)
    taup = uu1 * q[0] / c**2
    Fk = kap * uu1 * (t**2 / 2 + q[0]**2 / (2 * c**2))
    Dp = D4(Lk, taup, sp.Matrix([uu1 * t, 0, 0]))
    ok(sp.simplify(Dp - sp.diff(Fk, t)), "ejemplos físicos 7: cambio de velocidad paralelo, F = kappa u (t^2/2 + q1^2/(2 c^2))")
    Dperp = sp.simplify(D4(Lk, uu1 * q[1] / c**2, sp.Matrix([0, uu1 * t, 0])))
    ok(Dperp - kap * uu1 * q[0] * qd[1] / c**2, "ejemplos físicos 7: cambio de velocidad perpendicular, D = kappa u q1 q2' / c^2")
    Qk = pk[0] * uu1 * t - taup * Hk - Fk
    ok(sp.simplify(Qk / uu1 - (pk[0] * t - m * gam * q[0] + kap * q[0]**2 / (2 * c**2) - kap * t**2 / 2)), "ejemplos físicos 7: Q / u")
    ecs = [sp.diff(Lk, q[i]) - sp.diff(pk[i], t) for i in range(3)]
    acc = sp.solve(ecs, list(q.diff(t, 2)), dict=True)[0]
    ok(sp.simplify(sp.diff(Qk, t).subs(acc)), "ejemplos físicos 7: Q constante sobre las soluciones")
    ok(sp.simplify(sp.diff(Hk, t).subs(acc)), "ejemplos físicos 7: H constante sobre las soluciones")
    hip = m * c**2 / kap * (sp.sqrt(1 + (kap * t / (m * c))**2) - 1)
    solk = {q[0]: hip, q[1]: 0, q[2]: 0}
    ok(sp.simplify(ecs[0].subs(solk).doit()), "ejemplos físicos 7: el movimiento hiperbólico cumple la ecuación")
    ok(sp.simplify(Hk.subs(solk).doit() - m * c**2), "ejemplos físicos 7: H = m c^2 en el movimiento hiperbólico")
    ok(sp.simplify(Qk.subs(solk).doit()), "ejemplos físicos 7: Q = 0 en el movimiento hiperbólico")
    ok(sp.simplify(pk[0].subs(solk).doit() - kap * t), "ejemplos físicos 7: p1 = kappa t en el movimiento hiperbólico")

    # 8. Partícula cuántica en un potencial central
    x1, x2, x3 = Xs = sp.symbols("x1 x2 x3", real=True)
    I = sp.I
    hfun = sp.Function("h")(x1, x2, x3)
    P = [lambda h, kk=kk: -I * hb * sp.diff(h, Xs[kk]) for kk in range(3)]
    l1o = lambda h: x2 * P[2](h) - x3 * P[1](h)
    l2o = lambda h: x3 * P[0](h) - x1 * P[2](h)
    l3o = lambda h: x1 * P[1](h) - x2 * P[0](h)
    l2tot = lambda h: l1o(l1o(h)) + l2o(l2o(h)) + l3o(l3o(h))
    lmas = lambda h: l1o(h) + I * l2o(h)
    lmenos = lambda h: l1o(h) - I * l2o(h)
    ok(sp.expand(l3o(lmas(hfun)) - lmas(l3o(hfun)) - hb * lmas(hfun)), "ejemplos físicos 8: [l3, l+] = hbar l+")
    ok(sp.expand(lmenos(lmas(hfun)) - (l2tot(hfun) - l3o(l3o(hfun)) - hb * l3o(hfun))), "ejemplos físicos 8: l- l+ = l^2 - l3^2 - hbar l3")
    ok(sp.expand(lmas(lmenos(hfun)) - (l2tot(hfun) - l3o(l3o(hfun)) + hb * l3o(hfun))), "ejemplos físicos 8: l+ l- = l^2 - l3^2 + hbar l3")
    ok(sp.expand(l2tot(l3o(hfun)) - l3o(l2tot(hfun))), "ejemplos físicos 8: [l^2, l3] = 0")
    rr3 = sp.sqrt(x1**2 + x2**2 + x3**2)
    Rf = sp.Function("R")
    casos = [(sp.Integer(1), 0, 0), (x3 / rr3, 1, 0), ((x1 + I * x2) / rr3, 1, 1),
             ((3 * x3**2 - rr3**2) / rr3**2, 2, 0), ((x1 + I * x2) * x3 / rr3**2, 2, 1), ((x1 + I * x2)**2 / rr3**2, 2, 2)]
    for Y, l, mm in casos:
        ok(sp.simplify(l2tot(Y) - hb**2 * l * (l + 1) * Y), f"ejemplos físicos 8: l^2 Y = hbar^2 l (l+1) Y, l = {l}, m = {mm}")
        ok(sp.simplify(l3o(Y) - hb * mm * Y), f"ejemplos físicos 8: l3 Y = hbar m Y, l = {l}, m = {mm}")
    # l^2 = -hbar^2 (r^2 lap - Eu^2 - Eu), con Eu = sum q_k d_k (operador de Euler)
    Eu = lambda h: sum(Xs[kk] * sp.diff(h, Xs[kk]) for kk in range(3))
    lap = lambda h: sum(sp.diff(h, w, 2) for w in Xs)
    ok(sp.expand(l2tot(hfun) + hb**2 * (rr3**2 * lap(hfun) - Eu(Eu(hfun)) - Eu(hfun))), "ejemplos físicos 8: l^2 = -hbar^2 (r^2 lap - E^2 - E)")
    # separación: lap(R(r) Y) = (R'' + 2 R'/r - l (l+1) R / r^2) Y
    ss = sp.Symbol("ss", positive=True)
    for Y, l, mm in casos[1:4]:
        lhs = lap(Rf(rr3) * Y)
        Rpp = sp.diff(Rf(ss), ss, 2).subs(ss, rr3)
        Rp = sp.diff(Rf(ss), ss).subs(ss, rr3)
        rhs = (Rpp + 2 * Rp / rr3 - l * (l + 1) * Rf(rr3) / rr3**2) * Y
        ok(sp.simplify(lhs - rhs), f"ejemplos físicos 8: laplaciano de R(r) Y con l = {l}")


apartado6_casos()
apartado8_homogeneo()
apartado9_n1_m2()
apartado9_n2_m2()
cuerda()
apartado10()
apartado10_lrl()
apartado11_schrodinger()
ejemplos_v2()
particula()
fisica_relativista()
fisica_relativista_extra()
fisica_relativista_dos()
fisica_cuantica()
fisica_cuantica_3d()
fisica_cuantica_campo()
fisica_generador_temporal()
fisica_klein_gordon()
fisica_cuerda_lorentz()
fisica_ejemplos()
