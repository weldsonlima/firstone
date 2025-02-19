class cpf():
    def __init__(self, numero):
        self.numero = numero

    def emissao(self):
        if ((self.numero[8]) == "1"):
            return "DF, GO, MT, MS ou TO"
        elif (self.numero[8] == "2"):
            return "PA, AM, AC, AM, RO ou RR"
        elif (self.numero[8] == "3"):
            return "CE, MA ou PI"
        elif (self.numero[8] == "4"):
            return "PE, RN, PB ou AL"
        elif (self.numero[8] == "5"):
            return "BA ou SE"
        elif (self.numero[8] == "6"):
            return "MG"
        elif (self.numero[8] == "7"):
            return "RJ ou ES"
        elif (self.numero[8] == "8"):
            return "SP"
        elif (self.numero[8] == "9"):
            return "PR ou SC"
        elif (self.numero[8] == "0"):
            return "RS"

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
    
    def validar(self): # Cálculo ds dígitos verificadores segundo https://www.macoratti.net/alg_cpf.htm
        PriDigVer = 0
        SegDigVer = 0
        acumulador = 0

        #Cálculo do Primeiro Dígito
        for i in range(8,-1,-1):
            acumulador += (int(self.numero[i])*(10-i))
        if (acumulador % 11 < 2):
            PriDigVer = 0
        else:
            PriDigVer = 11 - (acumulador % 11)

        #Cálculo do Segundo Dígito
        acumulador = PriDigVer * 2
        for i in range(8,-1,-1):
            acumulador += (int(self.numero[i])*(11-i))
        if (acumulador % 11 < 2):
            SegDigVer = 0
        else:
            SegDigVer = 11 - (acumulador % 11)

        return (self.numero[-2:]==(str(PriDigVer)+str(SegDigVer)))


meucpf = cpf("11144477735")

print("CPF número: ",meucpf.numero)
print("CPF formatado: ",meucpf.formatar())
print("CPF mascarado: ",meucpf.mascarar())
print("CPF válido: ",meucpf.validar())
print("CPF emissão: ",meucpf.emissao())