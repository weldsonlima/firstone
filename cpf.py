class cpf():
    def __init__(self, numero):
        self.numero = numero
    
    def formatar(self):
        cpf_formatado = ""
        i = 0

        while i < len(self.numero):
            if (i != 0)and(i % 3 == 0)and( i > len(self.numero)-3):
                cpf_formatado += "-"
            elif (i !=0)and(i % 3 == 0):
                cpf_formatado += "."
            cpf_formatado += str(self.numero[i])
            i += 1
        
        return cpf_formatado
    
    def mascarar(self):
        cpf_mascarado = ""
        i = 0

        while i < len(self.numero):
            if (i != 0)and(i % 3 == 0)and(i > len(self.numero)-3):
                cpf_mascarado += "-"
            elif (i != 0)and(i % 3 == 0):
                cpf_mascarado += "."
            
            if (i < 3)or(i > len(self.numero)-3):
                cpf_mascarado += "*"
            else:
                cpf_mascarado += str(self.numero[i])
            i += 1

        return cpf_mascarado

meucpf = cpf("03467573479")

print("CPF número: ",meucpf.numero)
print("CPF formatado: ",meucpf.formatar())
print("CPF formatado: ",meucpf.mascarar())
