from os import listdir, path
import configlog

class Nro:
    def __init__(self, name):
            self.name = name 
            self.Sro = {'Sro'}      
    
    def get_sro(self):
        for file in listdir(configlog.c6initial_folder):
            if file.startswith(self.name):
                self.sro.add(file.split("_")[1])

    class Sro:
        def __init__(self,nro, name):
            self.nro = nro
            self.name = name   
            self.pa = {'pa'} 
            self.art = {'art'}
            self.Poteau = {'ptnum'}
        
        def get_pa_c6(self):
            for file in listdir(configlog.c6initial_folder):
                if file.startswith(self.nro + "_"+ self.name):
                    self.pa[file.replace(self.nro+ "_"+ self.name,"")] = path.basename(file)

    
        class Poteau:
            def __init__(self, pt_num):
                self.ptnum = pt_num

            def get_gps(self):
                self.gps_coord = ('x', 'y')
                return self.gps_coord
            
            def get_info():
                
                self.info =


NEU = Nro('86NEU')
NEU.get_sro()
print(NEU.Sro(NEU.name))
# NEU.sro.remove('sro')
# print(NEU.sro)
# for el in NEU.sro:
#     el = NEU.Sro(NEU.name, el)
#     el.get_pa_c6()
#     print(el.pa)