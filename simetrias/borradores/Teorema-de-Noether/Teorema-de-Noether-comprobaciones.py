"""Comprobaciones simbólicas de las cuentas de la serie «El teorema de Noether»: ejemplos
matemáticos y físicos y la versión para el trabajo. Se ejecuta desde la raíz del repositorio con
.venv\Scripts\python.exe; termina con «FALLOS: ninguno» si todo es correcto."""
import sympy as sp

t, eps, m, g, e, B = sp.symbols("t epsilon m g e B", positive=True)
fails = []


def ok(expr, msg):
    r = sp.simplify(sp.expand(expr))
    print(("OK   " if r == 0 else "FALLA") + " " + msg + ("" if r == 0 else f"  -> {r}"))
    if r != 0:
        fails.append(msg)


q = sp.Matrix([sp.Function(f"q{i}")(t) for i in (1, 2, 3)])
qd = q.diff(t)
qdd = q.diff(t, 2)
a = sp.Matrix(sp.symbols("a1:4", real=True))
n = sp.Matrix(sp.symbols("n1:4", real=True))
u = sp.Matrix(sp.symbols("u1:4", real=True))


def first_order(L, xi):
    """Coeficiente de primer orden de L(q + eps*xi, qd + eps*xi') - L."""
    sub = {q[i]: q[i] + eps * xi[i] for i in range(3)}
    Lt = L.subs(sub, simultaneous=True).doit()
    return sp.expand(sp.diff(Lt, eps).subs(eps, 0).doit())


def is_total_derivative(expr, F):
    return sp.expand(expr - sp.diff(F, t))


# 1. Partícula libre
L0 = sp.Rational(1, 2) * m * qd.dot(qd)
p = m * qd
ok(first_order(L0, a), "libre: traslación, F = 0")
ok(first_order(L0, n.cross(q)), "libre: giro, F = 0")
F_b = m * u.dot(q)
ok(first_order(L0, u * t) - sp.diff(F_b, t), "libre: cambio de velocidad, F = m u.q")
Qb = p.dot(u * t) - F_b
ok(Qb + u.dot(m * q - p * t), "libre: Q_boost = -u.(m q - p t)")
# comprobación con la solución q = q0 + v0 t
q0 = sp.Matrix(sp.symbols("x0 y0 z0", real=True))
v0 = sp.Matrix(sp.symbols("v1 v2 v3", real=True))
sol = {q[i]: q0[i] + v0[i] * t for i in range(3)}
ell = q.cross(p)
ell_s = ell.subs(sol).doit()
ok((ell_s - m * q0.cross(v0)).norm() ** 2, "libre: l = m q0 x v0 en la solución")
G_s = (m * q - p * t).subs(sol).doit()
ok((G_s - m * q0).norm() ** 2, "libre: g = m q0 en la solución")

# 2. Campo uniforme: L = 1/2 m |qd|^2 + m gvec.q, con gvec = (0, 0, -g)
gv = sp.Matrix([0, 0, -g])
L1 = L0 + m * gv.dot(q)
ez = sp.Matrix([0, 0, 1])
ok(first_order(L1, sp.Matrix([1, 0, 0])), "uniforme: traslación horizontal, F = 0")
F_v = -m * g * t
ok(first_order(L1, ez) - sp.diff(F_v, t), "uniforme: traslación vertical, F = -m g t")
ok(first_order(L1, ez.cross(q)), "uniforme: giro alrededor de la vertical, F = 0")
print("   uniforme: giro alrededor de x da δL/ε =", first_order(L1, sp.Matrix([1, 0, 0]).cross(q)))
F_bu = m * u.dot(q) + sp.Rational(1, 2) * m * gv.dot(u) * t**2
ok(first_order(L1, u * t) - sp.diff(F_bu, t), "uniforme: cambio de velocidad, F = m u.q + 1/2 m (g.u) t^2")
sol1 = {q[i]: q0[i] + v0[i] * t + sp.Rational(1, 2) * gv[i] * t**2 for i in range(3)}
Qv = (p.dot(ez) - F_v).subs(sol1).doit()
ok(sp.diff(Qv, t), "uniforme: p_z + m g t constante en la solución")
Qbu = (p.dot(u * t) - F_bu).subs(sol1).doit()
ok(Qbu + m * u.dot(q0), "uniforme: Q_boost = -m u.q0 en la solución")
Lz = ell[2].subs(sol1).doit()
ok(sp.diff(Lz, t), "uniforme: l_z constante en la solución")
E1 = (sp.Rational(1, 2) * m * qd.dot(qd) - m * gv.dot(q)).subs(sol1).doit()
ok(sp.diff(E1, t), "uniforme: E constante en la solución")

# 3. Campo central
r = sp.sqrt(q.dot(q))
U = sp.Function("U")
L2 = L0 - e * U(r)
ok(first_order(L2, n.cross(q)), "central: giro, F = 0")
print("   central: traslación da δL/ε =", sp.simplify(first_order(L2, a)))

# 4. Campo magnético uniforme, A = 1/2 B x q
Bv = sp.Matrix([0, 0, B])
A = Bv.cross(q) / 2
L3 = L0 + e * qd.dot(A)
pc = m * qd + e * A
F_t = sp.Rational(1, 2) * e * q.dot(Bv.cross(a))
ok(first_order(L3, a) - sp.diff(F_t, t), "magnético: traslación, F = 1/2 e q.(B x a)")
K = m * qd - e * q.cross(Bv)
ok(pc.dot(a) - F_t - a.dot(K), "magnético: Q = a.K, K = m qd - e q x B")
ok(first_order(L3, ez.cross(q)), "magnético: giro alrededor de B, F = 0")
Qrot = pc.dot(ez.cross(q))
rho2 = q[0] ** 2 + q[1] ** 2
ok(Qrot - (ell[2] + sp.Rational(1, 2) * e * B * rho2), "magnético: Q_giro = l_z + 1/2 e B rho^2")
dbz = first_order(L3, ez * t)
print("   magnético: cambio de velocidad a lo largo de B da δL/ε =", dbz)
ok(dbz - sp.diff(m * q[2], t), "magnético: cambio de velocidad paralelo a B, F = m q3")
print("   magnético: cambio de velocidad en x da δL/ε =", first_order(L3, sp.Matrix([t, 0, 0])))
# solución en hélice
c1, c2, c3, vp, vpar, gam = sp.symbols("c1 c2 c3 v_perp v_par gamma", real=True)
w = e * B / m
ph = gam - w * t
solh = {q[0]: c1 - vp / w * sp.sin(ph), q[1]: c2 + vp / w * sp.cos(ph), q[2]: c3 + vpar * t}
eqs = (m * qdd - e * qd.cross(Bv)).subs(solh).doit()
ok(eqs.norm() ** 2, "magnético: la hélice cumple las ecuaciones")
Kh = K.subs(solh).doit()
ok((Kh - sp.Matrix([-e * B * c2, e * B * c1, m * vpar])).norm() ** 2, "magnético: K = (-e B c2, e B c1, m v_par)")
Qh = (ell[2] + sp.Rational(1, 2) * e * B * rho2).subs(solh).doit()
ok(Qh - sp.Rational(1, 2) * e * B * (c1**2 + c2**2 - (vp / w) ** 2), "magnético: Q_giro = 1/2 e B (c1^2 + c2^2 - R^2)")

# 5. Traslación en el tiempo: xi = qd, δL/ε = dL/dt - ∂L/∂t
V = sp.Function("V")
Lgen = L0 - V(q[0], q[1], q[2], t)
xi = qd
# Con un V explícito que depende del tiempo, para poder escribir ∂L/∂t sin ambigüedad.
kt = sp.Function("k")(t)
Vt = kt * q[0] ** 2 + sp.sin(t) * q[1] * q[2]
Lt_ = L0 - Vt
d = first_order(Lt_, xi)
dLdt_parcial = -(sp.diff(kt, t) * q[0] ** 2 + sp.cos(t) * q[1] * q[2])
ok(d - (sp.diff(Lt_, t) - dLdt_parcial), "tiempo: δL/ε = dL/dt - ∂L/∂t")
H = p.dot(qd) - L0 + V(q[0], q[1], q[2], t)  # H = T + V
ok(p.dot(qd) - Lgen - H, "tiempo: Q = p.qd - L = T + V")

# 6. Camino más corto como gráfica
x = sp.Symbol("x")
f = sp.Function("f")(x)
fp = f.diff(x)
Lg = sp.sqrt(1 + fp**2)
pg = sp.diff(Lg, fp)
Hg = fp * pg - Lg
ok(Hg + 1 / sp.sqrt(1 + fp**2), "camino: H = -1/sqrt(1+f'^2)")

# 7. Camino paramétrico: identidad sum f'_i E_i = 0 y cantidad del giro
s = sp.Symbol("s")
f1, f2 = sp.Function("f1")(s), sp.Function("f2")(s)
v = sp.sqrt(f1.diff(s) ** 2 + f2.diff(s) ** 2)
Lp = v
E1p = sp.diff(Lp, f1) - sp.diff(sp.diff(Lp, f1.diff(s)), s)
E2p = sp.diff(Lp, f2) - sp.diff(sp.diff(Lp, f2.diff(s)), s)
ok(f1.diff(s) * E1p + f2.diff(s) * E2p, "paramétrico: f1' E1 + f2' E2 = 0 idénticamente")
Qr = (f1 * f2.diff(s) - f2 * f1.diff(s)) / v
# identidad de Noether para el giro: dQ/ds = -(xi1 E1 + xi2 E2), xi = (-f2, f1)
ok(sp.diff(Qr, s) + (-f2 * E1p + f1 * E2p), "paramétrico: identidad de Noether del giro")
Hp = f1.diff(s) * sp.diff(Lp, f1.diff(s)) + f2.diff(s) * sp.diff(Lp, f2.diff(s)) - Lp
ok(Hp, "paramétrico: H = 0 idénticamente")

# 8. Laplace: corriente de la traslación en x_l
X, Y = sp.symbols("X Y")
F2 = sp.Function("F")(X, Y)
fx, fy = F2.diff(X), F2.diff(Y)
Lm = (fx**2 + fy**2) / 2
Q1 = fx * fx - Lm  # k = 1, l = 1
Q2 = fy * fx       # k = 2, l = 1
ok(sp.diff(Q1, X) + sp.diff(Q2, Y) - (F2.diff(X, 2) + F2.diff(Y, 2)) * fx, "Laplace: div Q = Δf ∂_x f")

# 9. Cuerda: corriente de energía
mu, tau = sp.symbols("mu tau", positive=True)
ux = sp.Function("u")(X, t)
L_c = mu * ux.diff(t) ** 2 / 2 - tau * ux.diff(X) ** 2 / 2
# traslación en t: xi = u_t, F_t = L, F_x = 0
Q_t = sp.diff(L_c, ux.diff(t)) * ux.diff(t) - L_c
Q_x = sp.diff(L_c, ux.diff(X)) * ux.diff(t)
ok(Q_t - (mu * ux.diff(t) ** 2 / 2 + tau * ux.diff(X) ** 2 / 2), "cuerda: Q_t = densidad de energía")
EL = tau * ux.diff(X, 2) - mu * ux.diff(t, 2)
ok(sp.diff(Q_t, t) + sp.diff(Q_x, X) + ux.diff(t) * EL, "cuerda: ∂_t Q_t + ∂_x Q_x = -u_t · (EL)")
# desplazamiento u -> u + eps
Qs_t = sp.diff(L_c, ux.diff(t))
Qs_x = sp.diff(L_c, ux.diff(X))
ok(sp.diff(Qs_t, t) + sp.diff(Qs_x, X) + EL, "cuerda: corriente del desplazamiento = -EL")

# 10. Transformación que mueve la variable: Q = sum p xi - H tau - F
# Comprobación con la traslación temporal pura (xi = 0, tau = 1, F = 0): Q = -H,
# y con la descripción a tiempo fijo (xi_bar = -qd, Fbar = -L): Q = p.(-qd) + L = -H.
ok((p.dot(-qd) - (-Lgen)) + (p.dot(qd) - Lgen), "tiempo: las dos descripciones dan -H")

# 11. Newton con V(|f|): giro en el plano (1,2)
fv = sp.Matrix([sp.Function(f"f{i}")(t) for i in (1, 2, 3)])
W = sp.Function("W")
LN = fv.diff(t).dot(fv.diff(t)) / 2 - W(sp.sqrt(fv.dot(fv)))
xi12 = sp.Matrix([-fv[1], fv[0], 0])
subN = {fv[i]: fv[i] + eps * xi12[i] for i in range(3)}
dN = sp.expand(sp.diff(LN.subs(subN, simultaneous=True).doit(), eps).subs(eps, 0).doit())
ok(dN, "Newton: giro en el plano 12 es simetría si V depende de |f|")

print()
print("FALLOS:", fails if fails else "ninguno")
