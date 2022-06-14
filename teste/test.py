import unittest


class Calculadora:

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, c, d):
        return c * d

    def div(self, a, b):
        if b != 0:
            return a / b




class TesteCalculadora(unittest.TestCase):

    def setup(self):
        self.Calculadora = ('Calculadora')


    def testeSoma(self):
        self.calc = Calculadora()
        resultado = self.calc.soma(10, 5)
        esperado = 15
        self.assertEqual(resultado, esperado)

    def testeSub(self):
        self.calc = Calculadora()
        resultado = self.calc.sub(27, 14)
        esperado = 13
        self.assertEqual(resultado, esperado)

    def testeMulti(self):
        self.calc = Calculadora()
        resultado = self.calc.multi(4, 14)
        esperado = 56
        self.assertEqual(resultado, esperado)

    def testeDiv(self):
        self.calc = Calculadora()
        resultado = self.calc.div(15, 3)
        esperado = 5
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
