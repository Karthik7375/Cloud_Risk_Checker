#Improting the neccessary librabies
import json
from risk_rules import check_s3_buckets
from risk_rules import check_security_groups
from risk_rules import check_iam_of_users

import time

from synthetic_cloud_data_generator import cloud_data_generator
def load_data(file):
    try:
        with open(file) as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        
def main():
    s3_data = load_data("mock_data/s3_buckets.json")
    sg_data = load_data("mock_data/security_groups.json")
    iam_data = load_data("mock_data/iam_users.json")
    
    print("=== S3 RISK CHECKS ===")
    check_s3_buckets(s3_data)
    
    print("\n\n\n")
    
    print("=== SECURITY GROUP RISK CHECKS === ")
    check_security_groups(sg_data)
    
    print("\n\n\n")
    print("=== IAM (Identity and Access Management) USER CHECKS === ")
    check_iam_of_users(iam_data)

if __name__ == "__main__":
    cloud_data_generator()
    
    print("Scanning the json files")
    time.sleep(5)
    
    main()
