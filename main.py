"""
CNPJ

04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.922/0001-05
"""

class validatorCnpj:
    def __init__(self, value: str):
        self.original = value
        self.value = self.remove_character(value)
        self.value = [int(i) for i in self.value]
        self.original_value = self.value.copy()
        self.res_first = []
        self.res_second = []
        self.first_digit(self.value)
        
    def remove_character(self, cnpj: str):
        """It removes special characters"""
        
        cnpj = cnpj.replace('/','')
        cnpj = cnpj.replace('.','')
        cnpj = cnpj.replace('-','')
        return cnpj
        
    
    
    def first_digit(self, value: int):
        """It calculates the value of the first digit"""
        
        self.value.pop(len(self.value) - 1)
        self.value.pop(len(self.value) - 1)
        self.count = 0
        self.j = 5
        for i in self.value:
            self.res_first.append(i * self.j)
            self.count += 1
            self.j -= 1
            if self.count == 4:
                self.j = 9
            
        
            if self.count == 12:
                self.first = 11 - (sum(self.res_first) % 11)
                if self.first > 9: 
                    self.first = 0
                
                self.value.append(self.first)
                # print(self.value)
                
        def second_digit():
            """It calculates the value of the second digit"""
            
            self.count = 0
            self.j = 6
            for i in self.value:
                self.res_second.append(i * self.j)
                self.count += 1
                self.j -= 1
                
                if self.count == 5:
                    self.j = 9
                    
                if self.count == 13:
                    self.second = 11 - (sum(self.res_second) % 11)
                    
                    if self.second > 9:
                        self.second = 0
                        
                    
                    self.value.append(self.second)
        second_digit()
        if self.value == self.original_value:
            print(f'{self.original} is valid')
            
        else:
            print(f'{self.original} is not valid')
    
    
                
            
validatorCnpj("12.544.922/0001-05")
            
            