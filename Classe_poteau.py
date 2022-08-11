from os import listdir, path
import configlog

class Nro:
    def __init__(self, name):
            self.name = name 
            self.sro = {'sro'}
    
    def get_sro(self):
        for file in listdir(configlog.c6initial_folder):
            if file.startswith(self.name):
                self.sro.add(file.split("_")[1])

    class Sro:
        def __init__(self,name):
            self.name = name   
            self.pa = {}
        
        def get_pa_c6(self):
            for file in listdir(configlog.c6initial_folder):
                if file.startswith(self.nro+ "_"+ self.name):
                    self.pa[file.replace(self.nro+ "_"+ self.name,"")] = path.basename(file)
    

NEU = Nro('86NEU')
NEU.get_sro()
print(NEU.sro)
NEU.sro.remove('sro')
print(NEU.sro)
for el in NEU.sro:
    el = NEU.Sro(el)
    el.get_pa_c6()
    print(el.pa)