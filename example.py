sen_1='''Uncertainty principle, also called Heisenberg uncertainty principle or indeterminacy principle, statement, articulated (1927) by the German physicist Werner Heisenberg, that the position and the velocity of an object cannot both be measured exactly, at the same time, even in theory. The very concepts of exact position and exact velocity together, in fact, have no meaning in nature.Ordinary experience provides no clue of this principle. It is easy to measure both the position and the velocity of, say, an automobile, because the uncertainties implied by this principle for ordinary objects are too small to be observed. The complete rule stipulates that the product of the uncertainties in position and velocity is equal to or greater than a tiny physical quantity, or constant (h/(4π), where h is Planck’s constant, or about 6.6 × 10−34 joule-second). Only for the exceedingly small masses of atoms and subatomic particles does the product of the uncertainties become significant.
Any attempt to measure precisely the velocity of a subatomic particle, such as an electron, will knock it about in an unpredictable way, so that a simultaneous measurement of its position has no validity. This result has nothing to do with inadequacies in the measuring instruments, the technique, or the observer; it arises out of the intimate connection in nature between particles and waves in the realm of subatomic dimensions.'''
sen_2=''' uncertainty principle is one of the most famous (and probably misunderstood) ideas in physics. It tells us that there is a fuzziness in nature, a fundamental limit to what we can know about the behaviour of quantum particles and, therefore, the smallest scales of nature. Of these scales, the most we can hope for is to calculate probabilities for where things are and how they will behave. Unlike Isaac Newton's clockwork universe, where everything follows clear-cut laws on how to move and prediction is easy if you know the starting conditions, the uncertainty principle enshrines a level of fuzziness into quantum theory.

Werner Heisenberg's simple idea tells us why atoms don't implode, how the sun manages to shine and, strangely, that the vacuum of space is not actually empty.

An early incarnation of the uncertainty principle appeared in a 1927 paper by Heisenberg, a German physicist who was working at Niels Bohr's institute in Copenhagen at the time, titled "On the Perceptual Content of Quantum Theoretical Kinematics and Mechanics". The more familiar form of the equation came a few years later when he had further refined his thoughts in subsequent lectures and papers.

Heisenberg was working through the implications of quantum theory, a strange new way of explaining how atoms behaved that had been developed by physicists, including Niels Bohr, Paul Dirac and Erwin Schrödinger, over the previous decade. Among its many counter-intuitive ideas, quantum theory proposed that energy was not continuous but instead came in discrete packets (quanta) and that light could be described as both a wave and a stream of these

quanta. In fleshing out this radical worldview, Heisenberg discovered a problem in the way that the basic physical properties of a particle in a quantum system could be measured. In one of his regular letters to a colleague, Wolfgang Pauli, he presented the inklings of an idea that has since became a fundamental part of the quantum description of the world.

The uncertainty principle says that we cannot measure the position (x) and the momentum (p) of a particle with absolute precision. The more accurately we know one of these values, the less accurately we know the other. Multiplying together the errors in the measurements of these values (the errors are represented by the triangle symbol in front of each property, the Greek letter "delta") has to give a number greater than or equal to half of a constant called "h-bar". This is equal to Planck's constant (usually written as h) divided by 2π. Planck's constant is an important number in quantum theory, a way to measure the granularity of the world at its smallest scales and it has the value 6.626 x 10-34 joule seconds.

One way to think about the uncertainty principle is as an extension of how we see and measure things in the everyday world. You can read these words because particles of light, photons, have bounced off the screen or paper and reached your eyes. Each photon on that path carries with it some information about the surface it has bounced from, at the speed of light. Seeing a subatomic particle, such as an electron, is not so simple. You might similarly bounce a photon off it and then hope to detect that photon with an instrument. But chances are that the photon will impart some momentum to the electron as it hits it and change the path of the particle you are trying to measure. Or else, given that quantum particles often move so fast, the electron may no longer be in the place it was when the photon originally bounced off it. Either way, your observation of either position or momentum will be inaccurate and, more important, the act of observation affects the particle being observed.

The uncertainty principle is at the heart of many things that we observe but cannot explain using classical (non-quantum) physics. Take atoms, for example, where negatively-charged electrons orbit a positively-charged nucleus. By classical logic, we might expect the two opposite charges to attract each other, leading everything to collapse into a ball of particles. The uncertainty principle explains why this doesn't happen: if an electron got too close to the nucleus, then its position in space would be precisely known and, therefore, the error in measuring its position would be minuscule. This means that the error in measuring its momentum (and, by inference, its velocity) would be enormous. In that case, the electron could be moving fast enough to fly out of the atom altogether.

Heisenberg's idea can also explain a type of nuclear radiation called alpha decay. Alpha particles are two protons and two neutrons emitted by some heavy nuclei, such as uranium-238. Usually these are bound inside the heavy nucleus and would need lots of energy to break the bonds keeping them in place. But, because an alpha particle inside a nucleus has a very well-defined velocity, its position is not so well-defined. That means there is a small, but non-zero, chance that the particle could, at some point, find itself outside the nucleus, even though it technically does not have enough energy to escape. When this happens – a process metaphorically known as "quantum tunneling" because the escaping particle has to somehow dig its way through an energy barrier that it cannot leap over – the alpha particle escapes and we see radioactivity.

A similar quantum tunnelling process happens, in reverse, at the centre of our sun, where protons fuse together and release the energy that allows our star to shine. The temperatures at the core of the sun are not high enough for the protons to have enough energy to overcome their mutual electric repulsion. But, thanks to the uncertainty principle, they can tunnel their way through the energy barrier.

Perhaps the strangest result of the uncertainty principle is what it says about vacuums. Vacuums are often defined as the absence of everything. But not so in quantum theory. There is an inherent uncertainty in the amount of energy involved in quantum processes and in the time it takes for those processes to happen. Instead of position and momentum, Heisenberg's equation can also be expressed in terms of energy and time. Again, the more constrained one variable is, the less constrained the other is. It is therefore possible that, for very, very short periods of time, a quantum system's energy can be highly uncertain, so much that particles can appear out of the vacuum. These "virtual particles" appear in pairs – an electron and its antimatter pair, the positron, say – for a short while and then annihilate each other. This is well within the laws of quantum physics, as long as the particles only exist fleetingly and disappear when their time is up. Uncertainty, then, is nothing to worry about in quantum physics and, in fact, we wouldn't be here if this principle didn't exist.'''


k=[]
def arr(sen,a):
    exclude=[',',' ', ':', ';' , '?','"','-', '(', ')']
    if len(sen)==1:
        if sen in exclude:
            return a
        else:
            a.append(sen)
            if sen not in k:
                k.append(a)
            return a
    elif sen[0] in exclude:
        return arr(sen[1:],a)
    else:
        for i in range(len(sen)):
            if sen[i] in exclude:
                a.append(sen[:i])
                if sen[:i] not in k:
                    k.append(sen[:i])
                return arr(sen[i+1:],a)
                
        
            
li_1=[]
li_2=[]

arr(sen_1,li_1)
arr(sen_2,li_2)


d_1={}
for i in k:
    d_1[i]=0
d_2=d_1.copy()


for i in li_1:
    d_1[i]=+1
    
for i in li_2:
    d_2[i]=+1


dot=0
for i in k:
    dot=dot+d_1[i]*d_2[i]

def sq_rt(d):
    sum=0
    for value in d.values():
        sum=sum+value**2
    sum=sum**0.5
    return sum

theta=(dot/(sq_rt(d_1)*sq_rt(d_2)))*100
print('the similarity is', theta)



    
         
