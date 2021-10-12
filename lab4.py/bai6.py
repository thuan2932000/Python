# Cau 6: Return the particle from particle_to_probability with the lowest probablity.
def least_likely(particle_to_probability):
    smallest = 1
    name = ''
    for particle in particle_to_probability:
        probability = particle_to_probability[particle]
        if probability < smallest:
            smallest = probability
            name = particle
    return name
least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14})