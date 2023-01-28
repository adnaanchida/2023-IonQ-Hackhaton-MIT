# Adnaan Chida
# adnaan.chida@gmail.com

# part 2

# function to encode image
def encode(image):
    circuit=cirq.Circuit()
    # if statement for image 
    if image[0][0]==0:
        circuit.append(cirq.rx(np.pi).on(cirq.LineQubit(0)))
    # return circuit
    return circuit

# function to run part 2 with image parametet
def run_part2(image):

    #load the quantum classifier circuit
    with open('part2.pickle', 'rb') as f:
        classifier=pickle.load(f)
    
    #encode image into circuit
    circuit=encode(image)
    
    #append with classifier circuit
    
    circuit.append(classifier)
    
    #simulate circuit
    histogram=simulate(circuit)
        
    #convert histogram to category
    label=histogram_to_category(histogram)
        
    # return label and circuit
    return circuit
    return label
