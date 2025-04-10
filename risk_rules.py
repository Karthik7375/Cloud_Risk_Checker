def check_s3_buckets(list_of_buckets):
    for bucket in list_of_buckets:
        if bucket['public']:
            print(f"[!] Public Bucket Detected: {bucket['name']}")


def check_security_groups(groups):
    
    for sg in groups:
        #if cidr representation of the ip addr is 0.0.0.0/0 it's open to the world
        if sg['cidr'] == "0.0.0.0/0":
            print(f"[!] Security Group {sg['group']} open publicly!")


def check_iam_of_users(users):
    for user in users:
        if not user['mfa_enabled']:
            print(f"[!] Multi Factor Authentication is not enabled for user: {user['username']}")
        if "*" in user['policies']:
            print(f"[!] Over-permissive policy for user: {user['username']}")
            