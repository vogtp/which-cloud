import json
import os
import pickle

import netaddr


def load_aws(data_dir):
    aws_file = os.path.join(data_dir, "aws.json")
    with open(aws_file, "r") as f:
        data = json.load(f)
        ips = netaddr.IPSet()
        for e in data["prefixes"]:
            ips.add(e.get("ip_prefix"))
            print(".",end="")
        for e in data["ipv6_prefixes"]:
            print(".",end="")
            ips.add(e.get("ipv6_prefix"))
        return ips


def load_azure(data_dir):
    azure_file = os.path.join(data_dir, "azure.json")
    with open(azure_file, "r") as f:
        data = json.load(f)
        ips = netaddr.IPSet()
        for v in data["values"]:
            print(".",end="")
            ips.update(v["properties"]["addressPrefixes"])
        return ips


def load_gcp(data_dir):
    gcp_file = os.path.join(data_dir, "gcp.json")
    with open(gcp_file, "r") as f:
        data = json.load(f)
        ips = netaddr.IPSet()
        for e in data["prefixes"]:
            if e.get("ipv4Prefix"):
                print(".",end="")
                ips.add(e.get("ipv4Prefix"))
        return ips


def main(input_data_dir, output_data_dir):
    print( "loading AWS" )
    aws_ips = load_aws(input_data_dir)
    print( "loading Azure" )
    azure_ips = load_azure(input_data_dir)
    print( "loading GCP" )
    gcp_ips = load_gcp(input_data_dir)

    print( "Processing..." )
    output_file = os.path.join(output_data_dir, "data.pickle")
    with open(output_file, "wb") as f:
        pickle.dump((aws_ips, azure_ips, gcp_ips), f)


if __name__ == "__main__":
    pkg_dir = os.path.abspath(os.path.dirname(__file__))
    input_data_dir = os.path.join(pkg_dir, "data")
    output_data_dir = os.path.join(pkg_dir, "../which_cloud/data")
    main(input_data_dir, output_data_dir)
