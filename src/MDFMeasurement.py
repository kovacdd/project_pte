import asammdf

class MDFMeasurement():

    def __init__(self, file):
        self.file = file
        self.data = []
        self.values = ()

        try:
            self.mdf = asammdf.MDF(file)
        except asammdf.blocks.utils.MdfException as e:
            print(e)

    def set_data(self):

        f = self.file.split('/')[-1]
        vehicle = f.split('_')[0] 

        column = ['SPEED','N','MD','NOX_EO','NOX_TP','T_OIL','T_W_I','T_W_O','MF_FUEL']
        rows = self.mdf.get(column[0])

        print(f + ': ' + str(len(rows)) + ' rows')

        for i in range(len(rows)):
            vehicle = vehicle
            speed = self.mdf.get(column[0]).samples[i]
            n = self.mdf.get(column[1]).samples[i]
            md = self.mdf.get(column[2]).samples[i]
            nox_eo = self.mdf.get(column[3]).samples[i]
            nox_tp = self.mdf.get(column[4]).samples[i]
            t_oil = self.mdf.get(column[5]).samples[i]
            t_w_i = self.mdf.get(column[6]).samples[i]
            t_w_o = self.mdf.get(column[7]).samples[i]
            mf_fuel = self.mdf.get(column[8]).samples[i]

            self.values = (vehicle, speed, n, md, nox_eo, nox_tp, t_oil, t_w_i, t_w_o, mf_fuel)
            self.data.append(self.values)

            # print(str(i+1)+' -> '+str(self.values)+'\n')
            # print(str(i+1)+' -> '+str(self.data)+'\n')
            # if i == 11: break
            # l = len(rows) - (i+1)
            # print(str(l)+'\n')

            if i == 9:
                return self.data
            
        return self.data
    
    # set 'SPEED','N','MD','NOX_EO','NOX_TP','T_OIL','T_W_I','T_W_O','MF_FUEL'
    # get 'SPEED','N','MD','NOX_EO','NOX_TP','T_OIL','T_W_I','T_W_O','MF_FUEL'

    def get_size(self):
        rows = self.mdf.get('SPEED')
        return len(rows)