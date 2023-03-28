from conta import Conta

conta_victor = Conta(154223, "Victor Yazigi", 2500, 5000)
conta_sabrina = Conta(458987, "Sabrina Leonel", 5000, 10000)
conta_victor.extrato()
conta_victor.depositar(500)
conta_victor.sacar(1000)
conta_sabrina.transferir(2500,conta_victor)
conta_victor.extrato()
conta_victor.limite = 3000
print(conta_victor.limite)
conta_victor.sacar(7400)