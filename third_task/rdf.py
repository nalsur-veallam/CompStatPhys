from ovito.io import import_file
from ovito.modifiers import CoordinationAnalysisModifier
import numpy
from sys import argv

#data = numpy.loadtxt("liquid.T1.5.rho0.64.data", skiprows=19, max_rows=3375)
#data = data[:, :4]
#data[:, 0] = 1
#numpy.savetxt("liquid.T1.5.rho0.64.data", data)

# Load a simulation trajectory consisting of several frames:

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]

for rho in rhos:
    for T in Ts:
        pipeline = import_file('liquid.T'+str(T)+'.rho'+str(rho)+'.data')

        # Insert the modifier into the pipeline:
        modifier = CoordinationAnalysisModifier(cutoff = 15.0, number_of_bins = 300)
        pipeline.modifiers.append(modifier)

        # Initialize array for accumulated RDF histogram to zero:
        total_rdf = numpy.zeros((modifier.number_of_bins, 2))

        # Iterate over all frames of the sequence.
        for frame in range(pipeline.source.num_frames):
            # Evaluate pipeline to let the modifier compute the RDF of the current frame:
            data = pipeline.compute(frame)
            # Accumulate RDF histograms:
            total_rdf += data.tables['coordination-rdf'].xy()

        # Averaging:
        total_rdf /= pipeline.source.num_frames

        # Export the average RDF to a text file:
        numpy.savetxt('rdf.T'+str(T)+'.rho'+str(rho)+'.txt', total_rdf)
