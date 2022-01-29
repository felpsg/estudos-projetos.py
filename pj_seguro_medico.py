# Add your code here
 def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

  def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print(“Seu IMC está na faixa de obesidade. Para reduzir seu custo, você deve reduzir significativamente seu IMC.”)
    elif bmi_value >= 25 and bmi_value <= 30:
      print(“Seu IMC está na faixa de sobrepeso. Para diminuir seu custo, você deve diminuir seu IMC.”)
    elif bmi_value >= 18.5 and bmi_value < 25:
      print(“Seu IMC está em uma faixa saudável.”)
      else:
        print(“Seu IMC está na faixa abaixo do peso. Aumentar seu IMC não ajudará a reduzir seu custo, mas ajudará a melhorar sua saúde.”)

   
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
