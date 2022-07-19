# Función 1
import scipy

def build_population(N, p):
    """
    Se pretende generar una población con un número de individuos determinados (N) 
    donde cada uno de ellos posea dos alelos ("A": dominante o "a": recesivo) al azar (random),
    que a su vez pueden formar un par homocigoto ("AA", "aa") o heterocigoto ("Aa", "aA").
    
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population
    
# Función 2
def compute_frequencies(population):
    """
    Se contabiliza los distintos tipos de genotipos (AA, Aa, aA, aa) que se generan a partir del número de individuos
    que forman parte de la población generando una frecuencia (número) de cada uno de ellos.
    
    AA: dominante-dominante
    Aa: dominante-recesivo
    aA: recesivo-dominante
    aa: recesivo-recesivo
    
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})
    
# Función 3
def reproduce_population(population):
    """
    Se generan descendencias (reproducción) a partir de una selección al azar (random) de padres (mamá y papá),
    donde cada nueva generación posee características otorgadas por el cromosoma entregado de cada uno de los padres.
    Además, cada nueva generación depende de su población antecesora.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation