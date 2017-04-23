# SEQUENCE LD/SEQUENCE LDHOT
Record added by Jurg Ott (the original Rockefeller list)

## Description
The program sequenceLD analyzes sequence data. It obtains an approximation to the likelihood of a summary of the data (as such it can be thought of as a marginal likelihood approach). It does not use all the information in the data, but computationally it can be substantially more efficient than the full-likelihood methods (and hence able to analyze larger data sets).
The program sequenceLDhot is a method for detecting recombination hotspots from population genetic data. It takes as input phased (i.e. haplotype) data, together with an estimate of the background recombination rate within the region (this is allowed to vary across the region). Then sequenceLDhot considers a grid of putative hotspot positions, and for each putative hotspot calculates a likelihood ratio statistics for the presence of a hotspot.

## Author
Paul Fearnhead (Department of Mathematics, Statistics, Lancaster University, UK)

## URL
http://www.maths.lancs.ac.uk/~fearnhea/Software.html

## Reference
* Fearnhead, Donnelly (2002), "Approximate likelihood methods for estimating local recombination rates", Journal of the Royal Statistical Society series B, 64:657-680.
* Fearnhead (2006), "SequenceLDhot: detecting recombination hotspots", Bioinformatics, 22:3061-3066.