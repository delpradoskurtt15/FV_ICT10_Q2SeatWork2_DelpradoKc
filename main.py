from pyscript import Element
def general_weighted_average(e):
    science = float(document.getElementById('science').value)
    english = float(document.getElementById('english').value)
    pe = float(document.getElementById('pe').value)
    math = float(document.getElementById('math').value) 
    filipino = float(document.getElementById('filipino').value) 
    ict = float(document.getElementById('ict').value) 
    
    weights = {
     'science': 0.5,
    'english': 0.5, 
    'pe': 0.1,
    'math':0.5,
    'filipino': 0.3,
    'ict': 0.2,
    }
   
weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
total_units = (5 * 3) + 3 + 2 + 1
gwa = weighted_sum / total_units
Element('result').write(f'General Weighted Average: {gwa:.2f}') 

display(f'Name: {first_name} {last_name}')
display(summary, target='summary')
display(f'Your general weighted average is {gwa:.2f}', target='output')
