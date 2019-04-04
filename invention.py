import timeseriesFeatureExtractionTI as tfe
import argparse

#~ Positional arguments for the runner
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-feature', help="Select item")
parser.add_argument('-home', help="Select house")
parser.add_argument("-num", help="Define the amount of clusters", default=12)
args = parser.parse_args()

# Perform the algorithm
tfe.perform_cluster(args.home, args.feature, args.num)
