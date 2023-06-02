from sympy import *


def polynomial_example():
    """
        Funcion que ejemplifica como se escribe un polinomio usando sympy
    """
    # La funcion Symbol es usada para crear variables simbolicas
    x = Symbol('x')
    # Las variables simbolicas se combinan entre si como si se tratara de 
    # cantidades numericas
    pol1 = x**3 + x**2 + x + 7
    pol2 = 4*x**3 - x**2 + 2*x
    # Los caracteres de tipo \033[96m solo se usan para resaltar los resultados
    print(f'El primer polinomio corresponde a: \033[96m{pol1}\033[0m')
    print(f'El segundo polinomio corresponde a: \033[96m{pol2}\033[0m')
    print(
        f'La suma de los polinomios corresponde a: \033[93m{pol1 + pol2}\033[0m'
    )
    print(
        f'La diferencia de los polinomios corresponde a: \033[93m{pol1 - pol2}\033[0m'
    )
    print(
        f'El producto de los polinomios corresponde a: \033[93m{expand(pol1 * pol2)}\033[0m'
    )
    print(
        f'La división de los polinomios y su residuo corresponde a: \033[93m{div(pol1, pol2)[1]}\033[0m y \033[93m{div(pol1, pol2)[0]}\033[0m'
    )


def derivatives_example():
    """
        Funcion que ejemplifica como se deriva usando sympy
    """
    # De esta manera se declaran varias variables simbolicas
    x, y, z = symbols('x y z')
    fx = Rational(1, 5)*x**5
    fy = sqrt(y)
    fz = sin(z) + cos(z)
    fxyz = 3*x**2*y**3 - 2*z**5
    print(
        f'La tercer derivada de la función \033[96m{fx}\033[0m corresponde a \033[93m{diff(fx, x, 3)}\033[0m'
    )
    print(
        f'La derivada de la función \033[96m{fy}\033[0m corresponde a \033[93m{diff(fy, y)}\033[0m'
    )
    print(
        f'La segunda derivada de la función \033[96m{fz}\033[0m corresponde a \033[93m{diff(fz, z, 2)}\033[0m'
    )
    print(
        f'La derivada de la función \033[96m{fxyz}\033[0m respecto a {x} y {y} corresponde a \033[93m{diff(fxyz, x, y)}\033[0m'
    )
    print(
        f'La derivada de la función \033[96m{fxyz}\033[0m respecto a {z} corresponde a \033[93m{diff(fxyz, z)}\033[0m'
    )


def main():
    print('Ejemplo de polinomios\n')
    polynomial_example()
    print('\n\nEjemplo de derivadas\n')
    derivatives_example()


if __name__ == '__main__':
    main()