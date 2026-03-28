import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

suhu = ctrl.Antecedent(np.arange(0, 41), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 101), 'kelembaban')
kecepatan = ctrl.Consequent(np.arange(0, 101), 'kecepatan')

suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Sedang'] = fuzz.trimf(suhu.universe, [10, 20, 40])
suhu['Panas'] = fuzz.trimf(suhu.universe, [20, 40, 40])

kelembaban['Kering'] = fuzz.trimf(kelembaban.universe, [0, 0, 50])
kelembaban['Lembab'] = fuzz.trimf(kelembaban.universe, [0, 50, 100])
kelembaban['Basah'] = fuzz.trimf(kelembaban.universe, [50, 100, 100])

kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [0, 50, 100])
kecepatan['Cepat'] = fuzz.trimf(kecepatan.universe, [50, 100, 100])

aturan1 = ctrl.Rule(suhu['Dingin'] & kelembaban['Kering'], kecepatan['Lambat'])
aturan2 = ctrl.Rule(suhu['Dingin'] & kelembaban['Lembab'], kecepatan['Sedang'])
aturan3 = ctrl.Rule(suhu['Sedang'] & kelembaban['Kering'], kecepatan['Sedang'])
aturan4 = ctrl.Rule(suhu['Sedang'] & kelembaban['Lembab'], kecepatan['Sedang'])
aturan5 = ctrl.Rule(suhu['Panas'] & kelembaban['Kering'], kecepatan['Cepat'])
aturan6 = ctrl.Rule(suhu['Panas'] & kelembaban['Basah'], kecepatan['Cepat'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)
system.input['suhu'] = 25
system.input['kelembaban'] = 60
system.compute()
print(system.output['kecepatan'])
kecepatan.view(sim=system)
input("Tekan ENTER untuk melanjutkan")